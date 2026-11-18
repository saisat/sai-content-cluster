#!/usr/bin/env bash
# Install the sai-cc skill pack into a workspace or globally.
# Usage:
#   ./install.sh <workspace-dir>          # symlink into <workspace>/.claude/skills (default)
#   ./install.sh <workspace-dir> --copy   # copy instead of symlink
#   ./install.sh --global [--copy]        # install into ~/.claude/skills
#   ./install.sh <target> --uninstall     # remove sai-cc-* entries from the target
set -euo pipefail
PACK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODE=link; TARGET=""; UNINSTALL=0
for arg in "$@"; do
  case "$arg" in
    --copy) MODE=copy ;;
    --global) TARGET="$HOME" ;;
    --uninstall) UNINSTALL=1 ;;
    -h|--help) sed -n 2,8p "$0"; exit 0 ;;
    *) TARGET="$arg" ;;
  esac
done
[ -n "$TARGET" ] || { echo "Usage: ./install.sh <workspace-dir>|--global [--copy|--uninstall]"; exit 1; }
DEST="$(cd "$TARGET" && pwd)/.claude/skills"
mkdir -p "$DEST"
for skill in "$PACK_DIR"/sai-cc-*/; do
  name="$(basename "$skill")"
  rm -rf "${DEST:?}/$name"
  [ "$UNINSTALL" = 1 ] && { echo "removed $name"; continue; }
  if [ "$MODE" = copy ]; then cp -R "$skill" "$DEST/$name"; else ln -s "${skill%/}" "$DEST/$name"; fi
  echo "$MODE  $name → $DEST/$name"
done
[ "$UNINSTALL" = 1 ] || echo "Done. Restart Claude Code in the workspace, then run /sai-cc-setup (or /sai-cc-start)."
