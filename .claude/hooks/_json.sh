#!/usr/bin/env bash
# Shared JSON string encoder for Bash hooks. Encodes every C0 control byte, quotes, and
# backslashes without requiring Python or a third-party package.

json_escape() {
  LC_ALL=C printf '%s' "$1" \
    | od -An -v -t u1 \
    | LC_ALL=C awk '
        {
          for (i = 1; i <= NF; i++) {
            byte = $i + 0
            if (byte == 8)       printf "\\b"
            else if (byte == 9)  printf "\\t"
            else if (byte == 10) printf "\\n"
            else if (byte == 12) printf "\\f"
            else if (byte == 13) printf "\\r"
            else if (byte == 34) printf "\\\""
            else if (byte == 92) printf "\\\\"
            else if (byte < 32)  printf "\\u%04x", byte
            else                 printf "%c", byte
          }
        }
      '
}
