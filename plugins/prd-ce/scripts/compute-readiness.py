#!/usr/bin/env python3
"""EPIC readiness scorer. See scripts/_readiness/epic.py for logic
and docs/READINESS_PROTOCOL.md for the schema.

Usage:
  compute-readiness.py <epic-file> [--inputs YAML] [--merge] [--repo PATH]
                                   [--output PATH] [--verbose]
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _readiness.epic import main_cli

if __name__ == "__main__":
    sys.exit(main_cli())
