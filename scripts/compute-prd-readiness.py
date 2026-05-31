#!/usr/bin/env python3
"""PRD stage readiness scorer. See scripts/_readiness/stage.py for logic
and docs/READINESS_PROTOCOL.md for the schema.

Usage:
  compute-prd-readiness.py [--gate vX.Y] [--repo PATH] [--output PATH] [--verbose]
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _readiness.stage import main_cli

if __name__ == "__main__":
    sys.exit(main_cli())
