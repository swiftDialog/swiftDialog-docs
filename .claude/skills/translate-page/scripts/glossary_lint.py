"""Find words the glossary says not to use in a translation.

The glossary (src/i18n/glossary.md) lists, per language, words that must not stand
in for a term, e.g. `- de: Schaltfläche. Not "Taste" or "Knopf".` This module reads
those lists and reports where a page uses them. Some hits are fine in context
("Taste" for a keyboard key), so callers report them as warnings for review.

Matching is case-insensitive at the start of a word, so "Knopf" also catches
"Knopfgröße". A capitalised term must keep its capital, and a match followed by a
digit or a capital is skipped, so identifiers like "button1", "buttonsize" or
"ButtonBar" don't count.
Code, HTML tags, link targets and URLs are ignored, as is a match right after
"SF" or right before "SF" (SF Symbols keep their name: "SF-Symbol", "symbole SF").
A match inside the language's preferred translation is skipped too, so in languages
written without spaces the forbidden "对话" doesn't flag the preferred "对话框".
"""
import re
from pathlib import Path

GLOSSARY = Path(__file__).resolve().parents[4] / "src/i18n/glossary.md"

LANG_LINE_RE = re.compile(r"^\s*-\s+([a-z]{2,3}(?:-[a-z0-9]{2,4})?):\s(.*)$", re.I)
NOT_RE = re.compile(r"\bNot\s+(.*)$")
QUOTED_RE = re.compile(r'"([^"]+)"')
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
IGNORE_RE = re.compile(r"`[^`\n]+`|\]\([^)\s]*\)|https?://\S+|<[^>\n]+>")
FM_KEEP = ("title:", "description:")


def load_terms(path=GLOSSARY):
    """{lang: [forbidden word, ...]} from the glossary's "Not" lists."""
    terms = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = LANG_LINE_RE.match(line)
        if not m:
            continue
        n = NOT_RE.search(m.group(2))
        if n:
            lst = terms.setdefault(m.group(1).lower(), [])
            lst.extend(t for t in QUOTED_RE.findall(n.group(1)) if t not in lst)
    return terms


PREFERRED_RE = re.compile(r"^([^.(（\"]+)")
ARROW_RE = re.compile(r"→\s*([^.\s(（]+)")


def load_preferred(path=GLOSSARY):
    """{lang: [preferred translation, ...]}: the start of each language line, plus "→ x" targets."""
    keep = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        m = LANG_LINE_RE.match(line)
        if not m:
            continue
        body = NOT_RE.split(m.group(2))[0]
        found = [w.strip() for w in PREFERRED_RE.findall(body) + ARROW_RE.findall(body) if w.strip()]
        lst = keep.setdefault(m.group(1).lower(), [])
        lst.extend(w for w in found if w not in lst)
    return keep


def _pattern(term):
    # Start of a word. "SF Symbol", "SF-Symbol" and French "symbole SF" name SF Symbols, not a slip.
    # A capitalised term (a German noun) must match its capital, so identifiers such as
    # "buttonsize" don't count; neither does one followed by a digit ("Button1").
    first = re.escape(term[0]) if term[0].isupper() else "(?i:%s)" % re.escape(term[0])
    return re.compile(r"(?<![\w])(?<!SF )(?<!SF-)" + first + "(?i:" + re.escape(term[1:]) + r")(?![\dA-Z])(?!\w*\s+SF\b)")


def scan(text, terms, keep=()):
    """[(line number, term, line text)] for each forbidden word in prose.

    `keep` lists the language's preferred translations (load_preferred). Occurrences of a
    preferred word that contains a forbidden one, such as "对话框" containing "对话", are
    blanked out before matching.
    """
    pats = [(t, _pattern(t)) for t in terms]
    lowered = [t.lower() for t in terms]
    keep = sorted((k for k in keep if any(f in k.lower() and len(k) > len(f) for f in lowered)), key=len, reverse=True)
    keep_re = re.compile("|".join(re.escape(k) for k in keep), re.I) if keep else None
    hits = []
    lines = text.split("\n")
    in_fm = bool(lines) and lines[0].strip() == "---"
    fence = None
    for no, line in enumerate(lines, 1):
        if in_fm:
            if no > 1 and line.strip() == "---":
                in_fm = False
            if not line.lstrip().startswith(FM_KEEP):
                continue
        f = FENCE_RE.match(line)
        if f:
            mark = f.group(1)[0]
            fence = None if fence == mark else (fence or mark)
            continue
        if fence:
            continue
        prose = IGNORE_RE.sub(" ", line)
        if keep_re:
            prose = keep_re.sub(" ", prose)
        for term, pat in pats:
            if pat.search(prose):
                hits.append((no, term, line.strip()))
    return hits
