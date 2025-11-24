"""Provenance tracking for generated artifacts

Captures git SHA, config hash, and build metadata to ensure reproducibility.
"""

import subprocess
import hashlib
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any


def get_git_sha() -> str:
    """Get current git commit SHA.

    Returns:
        Full commit SHA, or 'unknown' if not in git repo
    """
    try:
        result = subprocess.run(
            ['git', 'rev-parse', 'HEAD'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return 'unknown'


def get_git_sha_short() -> str:
    """Get short git commit SHA (first 8 chars).

    Returns:
        Short commit SHA, or 'unknown' if not in git repo
    """
    sha = get_git_sha()
    return sha[:8] if sha != 'unknown' else 'unknown'


def get_config_hash(config: Dict[str, Any]) -> str:
    """Hash config to detect changes.

    Args:
        config: Configuration dict

    Returns:
        First 8 chars of SHA256 hash of config
    """
    config_str = json.dumps(config, sort_keys=True)
    return hashlib.sha256(config_str.encode()).hexdigest()[:8]


def get_tool_version() -> str:
    """Get tool version from package."""
    try:
        from tools import __version__
        return __version__
    except ImportError:
        return '1.0.0'


def create_provenance(config: Dict[str, Any]) -> Dict[str, str]:
    """Create provenance metadata dict.

    Args:
        config: Configuration used for generation

    Returns:
        Dict with build metadata
    """
    return {
        'build_time': datetime.utcnow().isoformat() + 'Z',
        'git_commit': get_git_sha(),
        'git_commit_short': get_git_sha_short(),
        'config_hash': get_config_hash(config),
        'tool_version': get_tool_version(),
    }


def write_provenance(output_dir: Path, config: Dict[str, Any]):
    """Write .provenance file with build metadata.

    Args:
        output_dir: Directory to write .provenance file
        config: Configuration used for generation
    """
    provenance = create_provenance(config)
    provenance_path = output_dir / '.provenance'
    provenance_path.write_text(json.dumps(provenance, indent=2))
    return provenance_path
