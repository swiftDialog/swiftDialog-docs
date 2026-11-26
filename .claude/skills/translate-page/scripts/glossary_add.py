#!/usr/bin/env python3
"""Add one language's lines to the glossary (src/i18n/glossary.md) in a single run.

Usage:
  glossary_add.py <lang> <entries.json> [--force]
  glossary_add.py --check <lang>

<lang> is the language's key in the glossary, the same as its file name in src/i18n/
(e.g. de, zh-hans, pt-BR). Case doesn't matter when matching existing lines.

entries.json maps each term, as written in its "### <term>" heading, to the line text:
  {"dialog": "caixa de diálogo. \\"dialog window\\" → janela de diálogo. Not \\"conversa\\".",
   "button": "botão. Not \\"tecla\\"."}
Each becomes "- <lang>: <text>", placed after the last language line in that term's section.

Nothing is written if a term has no section, or already has a line for <lang>
(--force replaces such lines instead). After writing, and with --check, the script lists
the terms that still have no line for <lang>.

Exit code 0 = every term has a line, 2 = some terms are missing a line, 1 = error.
"""
import argparse
import json
import re
import sys

from glossary_lint import GLOSSARY, LANG_LINE_RE

TERM_RE = re.compile(r"^###\s+(.+?)\s*$")


def sections(lines):
    """[(term, start, end)] for each "### term" section; end is exclusive."""
    heads = [(i, TERM_RE.match(l).group(1)) for i, l in enumerate(lines) if TERM_RE.match(l)]
    out = []
    for k, (i, term) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        # Stop at the next "## " heading too, so nothing lands in a later part of the file.
        for j in range(i + 1, end):
            if lines[j].startswith("## "):
                end = j
                break
        out.append((term, i, end))
    return out


def lang_lines(lines, start, end, lang=None):
    """Indexes of language lines in a section, optionally only those for `lang`."""
    found = []
    for j in range(start + 1, end):
        m = LANG_LINE_RE.match(lines[j])
        if m and (lang is None or m.group(1).lower() == lang.lower()):
            found.append(j)
    return found


def missing(lines, lang):
    return [term for term, s, e in sections(lines) if not lang_lines(lines, s, e, lang)]


def report(lines, lang):
    gaps = missing(lines, lang)
    total = len(sections(lines))
    if gaps:
        print("%s: %d of %d terms have no line:" % (lang, len(gaps), total))
        for t in gaps:
            print("  - " + t)
        return 2
    print("%s: all %d terms have a line." % (lang, total))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("lang", nargs="?", help="language key, e.g. pt-BR")
    ap.add_argument("entries", nargs="?", help="JSON file: term -> line text")
    ap.add_argument("--check", metavar="LANG", help="only list terms with no line for LANG")
    ap.add_argument("--force", action="store_true", help="replace existing lines for this language")
    a = ap.parse_args()

    lines = GLOSSARY.read_text(encoding="utf-8").split("\n")
    if a.check:
        sys.exit(report(lines, a.check))
    if not (a.lang and a.entries):
        ap.error("give <lang> <entries.json>, or --check <lang>")
    if not re.fullmatch(r"[a-z]{2}(?:-[a-z]{2,4})?", a.lang, re.I):
        sys.exit("language key %r doesn't look like de, pt-BR or zh-hans" % a.lang)

    with open(a.entries, encoding="utf-8") as f:
        entries = json.load(f)
    if not isinstance(entries, dict) or not all(isinstance(v, str) and v.strip() for v in entries.values()):
        sys.exit("entries file must be a JSON object of term -> non-empty text")

    secs = {term.lower(): (s, e) for term, s, e in sections(lines)}
    unknown = [t for t in entries if t.lower() not in secs]
    if unknown:
        sys.exit("no '### <term>' section for: %s" % ", ".join(unknown))
    clash = [t for t in entries if lang_lines(lines, *secs[t.lower()], a.lang)]
    if clash and not a.force:
        sys.exit("already have a %s line (pass --force to replace): %s" % (a.lang, ", ".join(clash)))

    # Edit from the bottom of the file up, so earlier line numbers stay valid.
    for term in sorted(entries, key=lambda t: secs[t.lower()][0], reverse=True):
        s, e = secs[term.lower()]
        new = "- %s: %s" % (a.lang, entries[term].strip())
        existing = lang_lines(lines, s, e, a.lang)
        if existing:
            lines[existing[0]] = new
            for j in reversed(existing[1:]):
                del lines[j]
            continue
        others = lang_lines(lines, s, e)
        if others:
            at = others[-1] + 1
        else:
            # No language lines yet: after the section's last bullet, or right after the heading.
            bullets = [j for j in range(s + 1, e) if lines[j].lstrip().startswith("- ")]
            at = (bullets[-1] if bullets else s) + 1
        lines.insert(at, new)

    GLOSSARY.write_text("\n".join(lines), encoding="utf-8")
    print("wrote %d %s line(s) to %s" % (len(entries), a.lang, GLOSSARY.name))
    sys.exit(report(lines, a.lang))


if __name__ == "__main__":
    main()
