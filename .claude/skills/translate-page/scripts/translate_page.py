#!/usr/bin/env python3
"""Draft-translate one Starlight docs page with a local TranslateGemma model.

Only prose goes to the model. Code blocks, imports, JSX/HTML lines, inline code,
URLs and link targets are kept unchanged, so the page structure can't be broken
or cut short. Internal doc links get the /<lang>/ prefix so readers stay in their
language.

Usage:
  translate_page.py <source.md[x] | slug> <lang> [--out PATH] [--force] [--lang-name NAME]
                    [--endpoint NAME] [--dry-run]

The model endpoint comes from endpoint.py (the current saved endpoint, or --endpoint).
TRANSLATE_API_URL and TRANSLATE_MODEL override the saved URL and model for one run.

Writes the draft and prints a JSON report on stdout. Progress goes to stderr.
Exit code 0 = clean, 2 = draft written but needs attention (see report), 1 = failed,
3 = no endpoint set up yet (run endpoint.py add).
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

import endpoint

LANG_NAMES = {
    "de": "German", "fr": "French", "es": "Spanish", "it": "Italian", "nl": "Dutch",
    "pt": "Portuguese", "pt-br": "Brazilian Portuguese", "sv": "Swedish", "da": "Danish",
    "nb": "Norwegian Bokmål", "fi": "Finnish", "pl": "Polish", "cs": "Czech",
    "ja": "Japanese", "ko": "Korean", "zh-cn": "Simplified Chinese",
    "zh-tw": "Traditional Chinese", "ru": "Russian", "uk": "Ukrainian", "tr": "Turkish",
}

# TranslateGemma's recommended prompt, plus a line about placeholders when the text has any.
PROMPT = (
    "You are a professional English (en) to {name} ({code}) translator. Your goal is to "
    "accurately convey the meaning and nuances of the original English text while adhering "
    "to {name} grammar, vocabulary, and cultural sensitivities.\n"
    "Produce only the {name} translation, without any additional explanations or commentary. "
    "{placeholders}"
    "Please translate the following English text into {name}:\n\n\n{text}"
)


def placeholder_note(text):
    # Mentioning placeholders when there are none makes the model invent one (seen with 12B).
    found = sorted(set(PH_RE.findall(text)), key=int)
    if not found:
        return ""
    return "Keep the markers %s exactly as they are. " % " ".join("⟦%s⟧" % n for n in found)

# Spans the model must never see: inline code, link targets, inline tags, JSX expressions, URLs.
MASK_RE = re.compile(
    r"`[^`\n]+`"
    r"|\]\([^)\s]*(?:\s+\"[^\"]*\")?\)"
    r"|<[^>\n]+>"
    r"|\{[^}\n]*\}"
    r"|https?://[^\s)>\]]+"
)
PH_RE = re.compile("⟦(\\d+)⟧")
LETTER_RE = re.compile(r"[A-Za-z]{2,}")

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
PROTECTED_LINE_RE = re.compile(
    r"^\s*(?:import\s|export\s"            # MDX imports/exports
    r"|</?[A-Za-z][^>]*>\s*$"              # tag-only line
    r"|(?:---|\*\*\*|___)\s*$"             # horizontal rule
    r"|:::)"                               # aside markers
)
HEADING_RE = re.compile(r"^(#{1,6}\s+)(.*)$")
ITEM_RE = re.compile(r"^(\s*(?:[-*+]|\d+[.)])\s+(?:\[[ xX]\]\s+)?|\s*>\s?)(.*)$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")

FM_TRANSLATE_KEYS = ("title", "description", "tagline", "text", "label", "alt")
FM_KEY_RE = re.compile(r"^(\s*(?:-\s+)?)([A-Za-z_]+):(\s*)(.*)$")


def log(msg):
    print(msg, file=sys.stderr, flush=True)


class Translator:
    def __init__(self, code, name, ep, api_key):
        self.code, self.name, self.ep, self.api_key = code, name, ep, api_key
        self.cache = {}
        self.calls = 0
        self.issues = []  # (line, problem, source text)
        self.dry_run = False

    def _call(self, text):
        if self.dry_run:
            self.calls += 1
            return text
        prompt = PROMPT.format(name=self.name, code=self.code, text=text, placeholders=placeholder_note(text))
        out = endpoint.chat(self.ep, self.api_key, prompt)
        self.calls += 1
        out = out.strip()
        # Small models sometimes wrap output in quotes or a code fence.
        if out.startswith("```") and not text.startswith("```"):
            out = re.sub(r"^```\w*\n?|\n?```$", "", out).strip()
        if len(out) > 1 and out[0] == out[-1] == '"' and not text.startswith('"'):
            out = out[1:-1]
        return out

    def masked(self, text, line):
        """Translate text that already contains placeholders. Returns the source text if they get lost."""
        if not LETTER_RE.search(PH_RE.sub("", text)):
            return text
        if text in self.cache:
            return self.cache[text]
        want = sorted(PH_RE.findall(text))
        for attempt in (1, 2):
            out = self._call(text)
            if sorted(PH_RE.findall(out)) == want and "\n" not in out.strip():
                out = match_final_period(text, out)
                self.cache[text] = out
                if (self.calls % 10) == 0:
                    log("  ... %d segments translated (line %d)" % (self.calls, line))
                return out
        self.issues.append((line, "placeholders lost or extra lines; left in English", text))
        return text

    def plain(self, text, line):
        m, saved = mask(text)
        return unmask(self.masked(m, line), saved)


def mask(s):
    saved = []

    def sub(m):
        saved.append(m.group(0))
        return "⟦%d⟧" % (len(saved) - 1)

    return MASK_RE.sub(sub, s), saved


def unmask(s, saved):
    return PH_RE.sub(lambda m: saved[int(m.group(1))], s)


def yaml_value(v, quote):
    if quote:
        return quote + v.replace(quote, "\\" + quote if quote == '"' else "''") + quote
    if re.search(r"[:#]\s|^[\[\]{}&*!|>'\"%@`-]|:$", v):
        return json.dumps(v, ensure_ascii=False)
    return v


def do_frontmatter(lines, tr):
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        m = FM_KEY_RE.match(line)
        if not m or m.group(2) not in FM_TRANSLATE_KEYS:
            out.append(line)
            i += 1
            continue
        prefix, key, sp, val = m.groups()
        lineno = i + 2
        if val.strip() in ("|", ">", "|-", ">-", "|+", ">+"):
            # Block scalar: translate the indented lines as one paragraph.
            base = len(line) - len(line.lstrip())
            j, block = i + 1, []
            while j < len(lines) and (not lines[j].strip() or len(lines[j]) - len(lines[j].lstrip()) > base):
                block.append(lines[j])
                j += 1
            indent = next((b[: len(b) - len(b.lstrip())] for b in block if b.strip()), " " * (base + 2))
            text = " ".join(b.strip() for b in block if b.strip())
            out.append(line)
            out.append(indent + tr.plain(text, lineno))
            i = j
            continue
        v, quote = val.strip(), ""
        if len(v) > 1 and v[0] == v[-1] and v[0] in "'\"":
            quote, v = v[0], v[1:-1]
        if v:
            out.append(prefix + key + ":" + (sp or " ") + yaml_value(tr.plain(v, lineno), quote))
        else:
            out.append(line)
        i += 1
    return out


def do_table_row(line, tr, lineno):
    if TABLE_SEP_RE.match(line):
        return line
    m, saved = mask(line)  # mask first so pipes inside `code` don't split cells
    cells = m.split("|")
    for k, cell in enumerate(cells):
        core = cell.strip()
        if core:
            lead = cell[: len(cell) - len(cell.lstrip())]
            trail = cell[len(cell.rstrip()):]
            cells[k] = lead + tr.masked(core, lineno) + trail
    return unmask("|".join(cells), saved)


def do_body(lines, tr, offset):
    out, para, para_start = [], [], 0
    fence = None
    in_jsx = False

    def flush():
        if para:
            indent = para[0][: len(para[0]) - len(para[0].lstrip())]
            out.append(indent + tr.plain(" ".join(p.strip() for p in para), para_start))
            del para[:]

    for idx, line in enumerate(lines):
        lineno = idx + offset
        fm = FENCE_RE.match(line)
        if fence:
            out.append(line)
            if fm and fm.group(1)[0] == fence[0] and len(fm.group(1)) >= len(fence):
                fence = None
            continue
        if fm:
            flush()
            fence = fm.group(1)
            out.append(line)
            continue
        if in_jsx:
            out.append(line)
            in_jsx = ">" not in line
            continue
        if not line.strip():
            flush()
            out.append(line)
            continue
        if re.match(r"^\s*<[A-Za-z/]", line) and ">" not in line:
            flush()
            in_jsx = True
            out.append(line)
            continue
        if PROTECTED_LINE_RE.match(line):
            flush()
            out.append(line)
            continue
        if line.lstrip().startswith("|"):
            flush()
            out.append(do_table_row(line, tr, lineno))
            continue
        hm = HEADING_RE.match(line)
        if hm:
            flush()
            out.append(hm.group(1) + tr.plain(hm.group(2), lineno))
            continue
        im = ITEM_RE.match(line)
        if im:
            flush()
            out.append(im.group(1) + tr.plain(im.group(2), lineno) if im.group(2).strip() else line)
            continue
        if not para:
            para_start = lineno
        para.append(line)
    flush()
    return out


def match_final_period(src, out):
    """Drop a full stop the model added to text that had none (headings, titles, list items)."""
    if out.endswith(".") and not out.endswith("...") and not src.rstrip().endswith((".", ":", "!", "?", ")")):
        return out[:-1]
    return out


def slugify(text):
    """Heading ID the way Starlight (github-slugger) makes it."""
    text = re.sub(r"<[^>]+>|`", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def heading_ids(lines):
    ids, seen, fence = [], {}, None
    for line in lines:
        fm = FENCE_RE.match(line)
        if fence:
            if fm and fm.group(1)[0] == fence[0]:
                fence = None
            continue
        if fm:
            fence = fm.group(1)
            continue
        hm = HEADING_RE.match(line)
        if hm:
            base = slugify(re.sub(r"\]\([^)]*\)|[\[\]*_]", "", hm.group(2)))
            n = seen.get(base, 0)
            seen[base] = n + 1
            ids.append(base if n == 0 else "%s-%d" % (base, n))
    return ids


def fix_anchors(src_lines, out_lines, text):
    """Point same-page #links at the translated heading IDs (headings are matched by position)."""
    old, new = heading_ids(src_lines), heading_ids(out_lines)
    if len(old) != len(new):
        return text, ["heading count changed (%d -> %d); #anchors not updated" % (len(old), len(new))]
    mapping = {o: n for o, n in zip(old, new) if o != n}
    return re.sub(r"\]\(#([^)\s]+)\)", lambda m: "](#%s)" % mapping.get(m.group(1), m.group(1)), text), []


def set_synced(text):
    """Set translationSynced (read by check_translations.py) to now, in the frontmatter."""
    stamp = "translationSynced: " + dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    if not text.startswith("---\n"):
        return "---\n" + stamp + "\n---\n\n" + text
    end = text.index("\n---", 4)
    fm = re.sub(r"\ntranslationSynced:.*", "", text[:end])
    return fm + "\n" + stamp + text[end:]


def localize_links(text, code, docs_root):
    """Prefix root-relative links to doc pages with /<code>/. Assets in public/ are left alone."""
    def is_doc(path):
        p = path.split("#")[0].split("?")[0].strip("/")
        if p == "":
            return True
        if p.split("/")[0] == code:
            return False
        for cand in (p + ".md", p + ".mdx", p + "/index.md", p + "/index.mdx"):
            if (docs_root / cand).is_file():
                return True
        return False

    def fix(m):
        pre, path = m.group(1), m.group(2)
        return pre + ("/" + code + path if is_doc(path) else path)

    text = re.sub(r"(\]\()(/(?!/)[^)\s]*)", fix, text)
    text = re.sub(r"(href=[\"'])(/(?!/)[^\"'\s]*)", fix, text)
    text = re.sub(r"(^\s*link:\s*)(/(?!/)\S*)", fix, text, flags=re.M)
    return text


def structure(text):
    return {
        "code_fences": sum(1 for l in text.splitlines() if FENCE_RE.match(l)),
        "open_tags": len(re.findall(r"<[A-Za-z][\w.]*[\s>]", text)),
        "close_tags": len(re.findall(r"</[A-Za-z][\w.]*>", text)),
        "inline_code": len(re.findall(r"`[^`\n]+`", text)),
        "headings": sum(1 for l in text.splitlines() if HEADING_RE.match(l)),
        "table_rows": sum(1 for l in text.splitlines() if l.lstrip().startswith("|")),
    }


def resolve_source(arg, repo):
    p = Path(arg)
    if p.is_file():
        return p.resolve()
    docs = repo / "src/content/docs"
    slug = arg.strip("/")
    for cand in (slug + ".md", slug + ".mdx", slug + "/index.md", slug + "/index.mdx"):
        if (docs / cand).is_file():
            return (docs / cand).resolve()
    sys.exit("source not found: " + arg)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", help="English page path, or slug like basic-use/title")
    ap.add_argument("lang", help="locale code as in astro.config.mjs, e.g. de")
    ap.add_argument("--out", help="output path (default: src/content/docs/<lang>/<same path>)")
    ap.add_argument("--force", action="store_true", help="overwrite an existing translation")
    ap.add_argument("--lang-name", help="English name of the language, if not in the built-in list")
    ap.add_argument("--endpoint", help="saved endpoint to use instead of the current one (see endpoint.py list)")
    ap.add_argument("--dry-run", action="store_true", help="don't call the model; echo text back to test parsing")
    a = ap.parse_args()

    ep, api_key = {"name": "dry run", "model": "none"}, ""
    if not a.dry_run:
        try:
            ep = endpoint.resolve(a.endpoint)
        except endpoint.EndpointError as e:
            print(e, file=sys.stderr)
            sys.exit(endpoint.NOT_CONFIGURED)
        api_key = endpoint.api_key(ep)
        if ep["key_env"] and not api_key:
            sys.exit("%s is not set in the environment or in your shell startup files" % ep["key_env"])
    code = a.lang.lower()
    name = a.lang_name or LANG_NAMES.get(code)
    if not name:
        sys.exit("unknown language code %r; pass --lang-name" % code)

    repo = Path(__file__).resolve().parents[4]
    docs_root = repo / "src/content/docs"
    src = resolve_source(a.source, repo)
    rel = src.relative_to(docs_root)
    if rel.parts[0] == code:
        sys.exit("source is already a %s page; pass the English page" % code)
    out_path = Path(a.out) if a.out else docs_root / code / rel
    if out_path.exists() and not a.force:
        sys.exit("%s exists; pass --force to overwrite, or --out for a separate draft" % out_path)

    text = src.read_text(encoding="utf-8")
    lines = text.split("\n")
    tr = Translator(code, name, ep, api_key)
    tr.dry_run = a.dry_run
    log("Translating %s -> %s (%s) with %s on %s" % (rel, code, name, ep["model"], ep["name"]))

    try:
        if lines and lines[0].strip() == "---":
            end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
            result = ["---"] + do_frontmatter(lines[1:end], tr) + ["---"] + do_body(lines[end + 1:], tr, end + 2)
        else:
            result = do_body(lines, tr, 1)
    except endpoint.EndpointError as e:
        sys.exit("model endpoint error (%s): %s" % (ep["name"], e))

    output = localize_links("\n".join(result), code, docs_root)
    output, anchor_notes = fix_anchors(lines, result, output)
    output = set_synced(output)

    s_in, s_out = structure(text), structure(output)
    mismatches = {k: [s_in[k], s_out[k]] for k in s_in if s_in[k] != s_out[k]}
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")

    report = {
        "source": str(src.relative_to(repo)),
        "output": str(out_path.resolve().relative_to(repo)) if out_path.resolve().is_relative_to(repo) else str(out_path),
        "language": "%s (%s)" % (name, code),
        "model_calls": tr.calls,
        "untranslated_segments": [{"line": l, "problem": p, "text": t[:200]} for l, p, t in tr.issues],
        "structure_mismatches": mismatches,
        "notes": anchor_notes,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    sys.exit(2 if tr.issues or mismatches else 0)


if __name__ == "__main__":
    main()
