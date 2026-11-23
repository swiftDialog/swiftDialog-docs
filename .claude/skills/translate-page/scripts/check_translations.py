#!/usr/bin/env python3
"""Find translated pages whose English original changed after the translation.

A translation counts as up to date when the English page's last change is no more
than THRESHOLD after the translation's last change. A translation's last change is
the later of its last git commit (or file time, if it has uncommitted edits) and the
`translationSynced` date in its frontmatter. Updating that date marks a page as
checked even when the English change needed no translation change.

Usage:
  check_translations.py [--lang de] [--threshold 2h] [--diff] [--glossary] [--json] [page ...]

  page        optional slugs or paths to limit the check (e.g. basic-use/message)
  --lang      only check this language (default: every src/i18n/<lang>.json)
  --threshold how far the English may be ahead before flagging: 90m, 2h, 1d (default 2h)
  --diff      print the English changes since each stale translation was synced
  --glossary  also list words the glossary says not to use (src/i18n/glossary.md).
              These are warnings: some are fine in context, e.g. "Taste" for a
              keyboard key. They don't change the exit code.
  --json      machine-readable output

Exit code 0 = everything up to date, 2 = something needs checking.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

import glossary_lint

REPO = Path(__file__).resolve().parents[4]
DOCS = REPO / "src/content/docs"
SYNC_RE = re.compile(r"^translationSynced:\s*['\"]?([^'\"\s]+)['\"]?\s*$", re.M)


def git(*args):
    r = subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True)
    return r.stdout.strip()


def changed_at(path):
    """(epoch seconds, how we know) for the file's last change."""
    rel = str(path.relative_to(REPO))
    if git("status", "--porcelain", "--", rel):
        return path.stat().st_mtime, "uncommitted"
    t = git("log", "-1", "--format=%ct", "--", rel)
    return (int(t), "committed") if t else (path.stat().st_mtime, "untracked")


def synced_at(path):
    m = SYNC_RE.search(path.read_text(encoding="utf-8").split("\n---", 1)[0])
    if not m:
        return None
    try:
        return dt.datetime.fromisoformat(m.group(1).replace("Z", "+00:00")).timestamp()
    except ValueError:
        return None


def parse_threshold(s):
    m = re.fullmatch(r"(\d+(?:\.\d+)?)\s*([mhd]?)", s.strip())
    if not m:
        sys.exit("bad --threshold %r (use e.g. 90m, 2h, 1d)" % s)
    return float(m.group(1)) * {"m": 60, "h": 3600, "d": 86400, "": 3600}[m.group(2)]


def fmt_time(ts):
    return dt.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")


def fmt_delta(sec):
    sec = int(sec)
    d, rem = divmod(sec, 86400)
    h, rem = divmod(rem, 3600)
    m = rem // 60
    return " ".join(p for p in ("%dd" % d if d else "", "%dh" % h if h else "", "%dm" % m) if p)


def english_changes(en, since):
    rel = str(en.relative_to(REPO))
    commits = git("log", "--since=@%d" % int(since), "--format=%h %cs %s", "--", rel).splitlines()
    base = git("log", "-1", "--format=%H", "--before=@%d" % int(since), "--", rel)
    diff = git("diff", base, "--", rel) if base else ""
    return commits, diff


def languages():
    return sorted(p.stem for p in (REPO / "src/i18n").glob("*.json"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pages", nargs="*")
    ap.add_argument("--lang")
    ap.add_argument("--threshold", default="2h")
    ap.add_argument("--diff", action="store_true")
    ap.add_argument("--glossary", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    limit = parse_threshold(a.threshold)
    langs = [a.lang] if a.lang else languages()
    wanted = {re.sub(r"\.mdx?$", "", p.replace("src/content/docs/", "")).strip("/") for p in a.pages}

    terms = glossary_lint.load_terms() if a.glossary else {}
    warnings = []
    results = []
    for code in langs:
        root = DOCS / code
        for tr in sorted(root.rglob("*.md*")) if root.is_dir() else []:
            rel = tr.relative_to(root)
            slug = re.sub(r"\.mdx?$", "", str(rel))
            if wanted and slug not in wanted:
                continue
            en = DOCS / rel
            item = {"lang": code, "page": str(rel), "translation": str(tr.relative_to(REPO))}
            if a.glossary:
                for no, term, text in glossary_lint.scan(tr.read_text(encoding="utf-8"), terms.get(code, [])):
                    warnings.append({"lang": code, "page": str(rel), "line": no, "term": term, "text": text[:200]})
            if not en.exists():
                item.update(status="orphan", note="English page no longer exists")
                results.append(item)
                continue
            en_t, en_how = changed_at(en)
            tr_t, tr_how = changed_at(tr)
            sync = synced_at(tr)
            last = max(tr_t, sync or 0)
            ahead = en_t - last
            item.update(
                english_changed=fmt_time(en_t), english_source=en_how,
                translation_changed=fmt_time(last),
                translation_source="translationSynced" if sync and sync >= tr_t else tr_how,
                english_ahead=fmt_delta(ahead) if ahead > 0 else "",
                status="stale" if ahead > limit else "ok",
            )
            if item["status"] == "stale":
                commits, diff = english_changes(en, last)
                item["english_commits_since"] = commits
                if en_how == "uncommitted":
                    item["english_commits_since"] = commits + ["(plus uncommitted edits)"]
                if a.diff:
                    item["english_diff"] = diff
            results.append(item)

    stale = [r for r in results if r["status"] != "ok"]
    if a.json:
        out = {"threshold": a.threshold, "checked": len(results), "needs_checking": stale}
        if a.glossary:
            out["glossary_warnings"] = warnings
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        for code in langs:
            mine = [r for r in results if r["lang"] == code]
            bad = [r for r in mine if r["status"] != "ok"]
            print("%s: %d of %d translations need checking (English more than %s ahead)" % (code, len(bad), len(mine), a.threshold))
            for r in bad:
                if r["status"] == "orphan":
                    print("  %-28s %s" % (r["page"], r["note"]))
                    continue
                print("  %-28s English %s (%s), translation %s (%s), English ahead %s" % (
                    r["page"], r["english_changed"], r["english_source"],
                    r["translation_changed"], r["translation_source"], r["english_ahead"]))
                for c in r["english_commits_since"]:
                    print("      " + c)
                if a.diff and r.get("english_diff"):
                    print("\n".join("      | " + l for l in r["english_diff"].splitlines()))
        if a.glossary:
            print("\nglossary: %d possible slips (check each in context)" % len(warnings))
            for w in warnings:
                print("  %s/%s:%d  %s  | %s" % (w["lang"], w["page"], w["line"], w["term"], w["text"][:120]))
    sys.exit(2 if stale else 0)


if __name__ == "__main__":
    main()
