#!/usr/bin/env bash
# List English docs pages that have no translation for the given language.
#
# Usage:
#   ./list_untranslated.sh de        # pages missing a German translation
#   ./list_untranslated.sh fr        # pages missing a French translation
#
# Compares src/content/docs/<slug>.md against src/content/docs/<lang>/<slug>.md.
# Prints one missing slug per line. Exit 0 always (even if nothing is missing).

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
DOCS="$REPO/src/content/docs"

LANG="${1:?usage: $0 <lang>}"

if [[ ! -d "$DOCS/$LANG" ]]; then
  echo "no translation folder: $DOCS/$LANG" >&2
  exit 0
fi

comm -13 \
  <(find "$DOCS/$LANG" -name '*.md' | sed "s|^$DOCS/$LANG/||" | sort) \
  <(find "$DOCS" -name '*.md' -not -path "*/$LANG/*" -not -path '*/fr/*' | sed "s|^$DOCS/||" | sort)
