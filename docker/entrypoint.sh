#!/bin/sh
set -eu

APP_DIR="${APP_DIR:-/usr/src/app}"
TARGET_PATH="${CREDS_JSON_PATH:-$APP_DIR/creds.json}"

if [ "${CREDS_JSON_B64:-}" ]; then
  mkdir -p "$(dirname "$TARGET_PATH")"

  # Avoid pipeline; write to a temp file then decode
  tmp="/tmp/creds.b64"
  printf "%s" "$CREDS_JSON_B64" > "$tmp"

  if command -v base64 >/dev/null 2>&1; then
    base64 -d "$tmp" > "$TARGET_PATH"
  elif command -v openssl >/dev/null 2>&1; then
    openssl base64 -d -A -in "$tmp" -out "$TARGET_PATH"
  elif command -v python3 >/dev/null 2>&1; then
    python3 - "$tmp" "$TARGET_PATH" <<'PY'
import sys, base64, pathlib
raw = pathlib.Path(sys.argv[1]).read_text()
pathlib.Path(sys.argv[2]).write_bytes(base64.b64decode(raw))
PY
  else
    echo "No decoder available (base64/openssl/python3)." >&2
    exit 1
  fi

  rm -f "$tmp"
  chmod 600 "$TARGET_PATH" || true
else
  echo "Warning: CREDS_JSON_B64 is not set; creds.json not created." >&2
fi

exec "$@"