#!/usr/bin/env python3
"""SoT file readiness scorer. See scripts/_readiness/sot.py for logic
and docs/READINESS_PROTOCOL.md for the schema.

Usage:
  compute-sot-readiness.py <sot-file|all> [--repo PATH] [--output PATH] [--verbose]
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _readiness.sot import main_cli

if __name__ == "__main__":
    sys.exit(main_cli())
