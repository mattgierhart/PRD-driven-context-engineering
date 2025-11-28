#!/usr/bin/env python3
"""GHM Session State Validator

Validates that EPIC files have properly maintained Session State sections.

Usage:
    python tools/validate-sessions.py --epic epics/EPIC-03.md
    python tools/validate-sessions.py --all
    python tools/validate-sessions.py --all --strict
"""

import argparse
import re
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional


class SessionValidator:
    """Validates EPIC Session State compliance."""

    # Patterns for parsing Session State
    SECTION_0_PATTERN = re.compile(r'^## 0\. Session State', re.MULTILINE)
    SESSION_DATE_PATTERN = re.compile(r'\*\*Session Date\*\*\s*\|\s*(\d{4}-\d{2}-\d{2}|\{.*\})')
    STOPPED_AT_PATTERN = re.compile(r'### Stopped At', re.MULTILINE)
    NEXT_SESSION_PATTERN = re.compile(r'### Next Session Should', re.MULTILINE)
    FILES_CHANGED_PATTERN = re.compile(r'### Files Changed', re.MULTILINE)
    SESSION_HISTORY_PATTERN = re.compile(r'### Session History', re.MULTILINE)
    PLACEHOLDER_PATTERN = re.compile(r'\{[A-Z\-_#/]+\}')

    def __init__(self, strict: bool = False, max_stale_days: int = 7):
        """
        Initialize validator.

        Args:
            strict: If True, fail on warnings (not just errors)
            max_stale_days: Sessions older than this are flagged as stale
        """
        self.strict = strict
        self.max_stale_days = max_stale_days

    def validate_epic(self, epic_path: Path) -> Dict:
        """
        Validate a single EPIC file.

        Args:
            epic_path: Path to EPIC markdown file

        Returns:
            Dict with 'valid', 'errors', 'warnings', and 'info' keys
        """
        result = {
            'file': str(epic_path),
            'valid': True,
            'errors': [],
            'warnings': [],
            'info': []
        }

        if not epic_path.exists():
            result['valid'] = False
            result['errors'].append(f"File not found: {epic_path}")
            return result

        content = epic_path.read_text()

        # Check for Section 0
        if not self.SECTION_0_PATTERN.search(content):
            result['valid'] = False
            result['errors'].append("Missing Section 0 (Session State)")
            return result

        result['info'].append("Section 0 (Session State) present")

        # Extract Section 0 content (up to Section 1)
        section_0_match = re.search(
            r'## 0\. Session State.*?(?=## 1\.|$)',
            content,
            re.DOTALL
        )

        if not section_0_match:
            result['valid'] = False
            result['errors'].append("Could not parse Section 0 content")
            return result

        section_0 = section_0_match.group(0)

        # Check for required subsections
        checks = [
            (self.STOPPED_AT_PATTERN, "Stopped At", True),
            (self.NEXT_SESSION_PATTERN, "Next Session Should", True),
            (self.FILES_CHANGED_PATTERN, "Files Changed", False),
            (self.SESSION_HISTORY_PATTERN, "Session History", False),
        ]

        for pattern, name, required in checks:
            if pattern.search(section_0):
                result['info'].append(f"'{name}' section present")
            elif required:
                result['valid'] = False
                result['errors'].append(f"Missing required '{name}' section")
            else:
                result['warnings'].append(f"Missing optional '{name}' section")

        # Check for unfilled placeholders
        placeholders = self.PLACEHOLDER_PATTERN.findall(section_0)
        template_placeholders = [p for p in placeholders if p not in ['{#}', '{N}']]
        if template_placeholders:
            result['warnings'].append(
                f"Unfilled placeholders found: {', '.join(set(template_placeholders)[:5])}"
            )

        # Check session date for staleness
        date_match = self.SESSION_DATE_PATTERN.search(section_0)
        if date_match:
            date_str = date_match.group(1)
            if not date_str.startswith('{'):
                try:
                    session_date = datetime.strptime(date_str, '%Y-%m-%d')
                    days_old = (datetime.now() - session_date).days
                    if days_old > self.max_stale_days:
                        result['warnings'].append(
                            f"Session State is {days_old} days old (threshold: {self.max_stale_days})"
                        )
                    else:
                        result['info'].append(f"Session date: {date_str} ({days_old} days ago)")
                except ValueError:
                    result['warnings'].append(f"Could not parse session date: {date_str}")

        # Check "Stopped At" has actual content (not just template)
        stopped_at_match = re.search(
            r'### Stopped At.*?(?=###|\Z)',
            section_0,
            re.DOTALL
        )
        if stopped_at_match:
            stopped_at_content = stopped_at_match.group(0)
            # Check if it's just the template example
            if 'Example:' in stopped_at_content and stopped_at_content.count('\n') < 5:
                result['warnings'].append("'Stopped At' section may only contain template example")
            # Check for specificity indicators (file paths, line numbers)
            if re.search(r'[a-zA-Z0-9_/]+\.(ts|js|py|md|json)|\:\d+', stopped_at_content):
                result['info'].append("'Stopped At' contains specific file/line references")

        # Check "Next Session Should" has actionable items
        next_session_match = re.search(
            r'### Next Session Should.*?(?=###|\Z)',
            section_0,
            re.DOTALL
        )
        if next_session_match:
            next_content = next_session_match.group(0)
            # Count numbered items
            numbered_items = re.findall(r'^\d+\.', next_content, re.MULTILINE)
            if len(numbered_items) >= 2:
                result['info'].append(f"'Next Session Should' has {len(numbered_items)} action items")
            elif len(numbered_items) == 0:
                result['warnings'].append("'Next Session Should' has no numbered action items")

        # Apply strict mode
        if self.strict and result['warnings']:
            result['valid'] = False

        return result

    def validate_all(self, epics_dir: Path) -> List[Dict]:
        """
        Validate all EPIC files in a directory.

        Args:
            epics_dir: Directory containing EPIC files

        Returns:
            List of validation results
        """
        results = []
        epic_files = list(epics_dir.glob('EPIC-*.md'))

        if not epic_files:
            return [{
                'file': str(epics_dir),
                'valid': True,
                'errors': [],
                'warnings': ['No EPIC files found'],
                'info': []
            }]

        for epic_file in sorted(epic_files):
            results.append(self.validate_epic(epic_file))

        return results


def print_result(result: Dict, verbose: bool = False):
    """Print a validation result with colors."""
    # ANSI colors
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'

    status = f"{GREEN}PASS{NC}" if result['valid'] else f"{RED}FAIL{NC}"
    print(f"\n{result['file']}: {status}")

    for error in result['errors']:
        print(f"  {RED}ERROR:{NC} {error}")

    for warning in result['warnings']:
        print(f"  {YELLOW}WARN:{NC} {warning}")

    if verbose:
        for info in result['info']:
            print(f"  {BLUE}INFO:{NC} {info}")


def main():
    parser = argparse.ArgumentParser(
        description='Validate EPIC Session State compliance',
        epilog='See CLAUDE.md Section 10 for Session Protocol details'
    )
    parser.add_argument(
        '--epic',
        type=Path,
        help='Path to specific EPIC file to validate'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Validate all EPICs in epics/ directory'
    )
    parser.add_argument(
        '--epics-dir',
        type=Path,
        default=Path('epics'),
        help='Directory containing EPIC files (default: epics/)'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors'
    )
    parser.add_argument(
        '--max-stale-days',
        type=int,
        default=7,
        help='Flag sessions older than N days as stale (default: 7)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show info messages, not just errors/warnings'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as JSON'
    )

    args = parser.parse_args()

    if not args.epic and not args.all:
        parser.error("Must specify --epic <path> or --all")

    validator = SessionValidator(
        strict=args.strict,
        max_stale_days=args.max_stale_days
    )

    results = []

    if args.epic:
        results.append(validator.validate_epic(args.epic))
    elif args.all:
        results = validator.validate_all(args.epics_dir)

    if args.json:
        import json
        print(json.dumps(results, indent=2))
    else:
        print("=" * 60)
        print("GHM Session State Validator")
        print("=" * 60)

        for result in results:
            print_result(result, verbose=args.verbose)

        # Summary
        total = len(results)
        passed = sum(1 for r in results if r['valid'])
        failed = total - passed
        warnings = sum(len(r['warnings']) for r in results)

        print("\n" + "=" * 60)
        print(f"Summary: {passed}/{total} passed", end="")
        if warnings:
            print(f", {warnings} warnings")
        else:
            print()

        if args.strict:
            print("(strict mode: warnings treated as errors)")

    # Exit code
    if any(not r['valid'] for r in results):
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
