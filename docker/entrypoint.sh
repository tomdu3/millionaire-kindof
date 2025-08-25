#!/bin/sh
set -euo pipefail

APP_DIR="${APP_DIR:-/usr/src/app}"
TARGET_PATH="${CREDS_JSON_PATH:-$APP_DIR/creds.json}"

if [ -n "${CREDS_JSON_B64:-}" ]; then
  mkdir -p "$(dirname "$TARGET_PATH")"
  if command -v base64 >/dev/null 2>&1; then
    printf "%s" "$CREDS_JSON_B64" | base64 -d > "$TARGET_PATH"
  else
    # Fallback if base64 is missing
    printf "%s" "$CREDS_JSON_B64" | openssl base64 -d -A > "$TARGET_PATH"
  fi
  chmod 600 "$TARGET_PATH"
else
  echo "Warning: CREDS_JSON_B64 is not set; creds.json will not be created." >&2
fi

exec "$@"