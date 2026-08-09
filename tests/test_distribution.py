"""Distribution contracts for direct install and plugin-native initialization.

These tests exercise only isolated temporary repositories. They establish that repository-owned
PRD/SoT authority is not a downstream seed, that reinstall is non-destructive, and that the
generated plugin contains everything needed to produce the same consumer scaffold.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / ".claude" / "install-manifest.yaml"
DIRECT_INSTALLER = REPO_ROOT / "install.sh"
CANONICAL_PLUGIN_INSTALLER = REPO_ROOT / "scripts" / "prd-ce-init.sh"
PLUGIN_ROOT = REPO_ROOT / "plugins" / "prd-ce"
PLUGIN_INSTALLER = PLUGIN_ROOT / "scripts" / "prd-ce-init.sh"

EXCLUDED_DOCS = {
    "PRD_CE_V2_BUILD_PLAN.md",
    "GEARHEARTAI_PRD_CE_V2_SITE_BRIEF.md",
    "MASTER_AI_NATIVE_PRODUCT_ENGINEERING_V2_IMPLEMENTATION_BLUEPRINT.md",
    "PRD_CE_V2_LIVE_PROJECT_EVALUATION_PROMPT.md",
}
EXCLUDED_DISTRIBUTABLE_FILES = {
    *EXCLUDED_DOCS,
    "IMPROVEMENT_SUMMARY.md",
    "PHASE_2_EXECUTION_PLAN.md",
    "package-plugin.sh",
    "check-plugin-sync.sh",
    "check-stage-gate.sh",
    "stage-gate-validation.md",
}
ALLOWED_DOCS = {"DEVELOPMENT_GRAPH.md", "READINESS_PROTOCOL.md"}
DOC_SEED_SOURCES = {"DEVELOPMENT_GRAPH.seed.md", "READINESS_PROTOCOL.seed.md"}
DIRECT_SOURCE_ONLY_PATHS = {
    "install.sh",
    "BLUEPRINT.md",
    ".claude/install-manifest.yaml",
    ".claude/skills/ghm-self-install",
    ".claude/skills/init",
    "scripts/_merge_settings.py",
    "scripts/prd-ce-init.sh",
}
MUTABLE_SEED_DESTINATIONS = {
    "README.md",
    "PRD.md",
    "epics/EPIC_TEMPLATE.md",
    "epics/README.md",
    "SoT",
    "docs/DEVELOPMENT_GRAPH.md",
    "docs/READINESS_PROTOCOL.md",
    ".claude/domain-profile.yaml",
    ".claude/agents/devlab/MEMORY.md",
    ".claude/agents/horizon/MEMORY.md",
    ".claude/agents/metro/MEMORY.md",
    ".claude/agents/studio/MEMORY.md",
}
LEGACY_FRAMEWORK_BASELINE = "1e31c170d42de6bcc9f8a57a7a10f0a75b8244a7"
AUTHORITY_IDS = {
    "BR-001", "BR-002", "BR-003", "BR-004", "BR-005",
    "ARC-001", "ARC-002", "ARC-003", "ARC-004",
}
FORBIDDEN_TEXT = {
    "temp/v2-model-evaluation",
    "temp/v0.6-architecture/kuzu-sot-evaluation",
    "codex/prd-ce-v2-product-model",
    "The Product Model",
    "GearHeartAI",
    "GearHeart-specific",
    "GearHeart portfolio",
    "GearHeart standard",
    "GearHeart methodology",
    "GearHeart",
    *EXCLUDED_DOCS,
}
# SHA-256 fingerprints keep known private/downstream markers out of tracked source while still
# preventing them from re-entering reusable files. Candidates are normalized to lowercase words;
# one-, two-, and three-word windows are checked below.
PRIVATE_MARKER_FINGERPRINTS = {
    "8e34b6192b5255126dcbec7c69fb7b950d5ad3cd740b47afbb1ae02b7825abaf",
    "b592fe7889fd739ad6f720dfeb0ef8d374d12429a72a435fafe41c4c5b5be918",
    "94a34373f1f01e3f5522ecd06c3f0411c729c7316b233ee0eac979981ec7db90",
    "98570456f5d61ee6bdb4db144d2565112de9fcd119914a562fba2ee0e6cba2a8",
    "6b20e9b742e448a5040d026ac2543b7e1901731b50790eea284f575bfccba943",
    "716b4f08c3153fc30e1c40206cc804cbf3f65946ff37f0fd301ef4c2d9f58184",
    "99c67912c59f3e5b4fe02242ba718fd3a9a4b891f0bfafc0b48893f4a72070e8",
    "cb346ff499f5c63aa2791d0cb1afde2cdc77bcef9770c4de0f8f40b69bbecc38",
    "45f3e4d8e97404251fc5cbd4c7c074f6df3be1c7a21cabb7c5ec6d5835f768e8",
    "4d3902332981f1c3ff7c50da3068c48d0c4d683e59882d1f440be8e3b7c14823",
}
FORBIDDEN_PATTERNS = {
    "macOS absolute home path": re.compile(r"/Users/[A-Za-z0-9._-]+(?:/|$)"),
    "Linux absolute home path": re.compile(r"(?i)/home/[a-z0-9._-]+(?:/|$)"),
    "Windows absolute home path": re.compile(r"(?i)\b[a-z]:\\users\\[^\\\s]+\\"),
}
SOURCE_INTERFACE_FORBIDDEN_TEXT = {
    "temp/v2-model-evaluation",
    "temp/v0.6-architecture/kuzu-sot-evaluation",
    "v2-model-evaluation",
    "kuzu-sot-evaluation",
    "PRD_CE_V2_LIVE_PROJECT_EVALUATION_PROMPT.md",
}


def _run(cmd: list[str], *, cwd: Path | None = None,
         env: dict[str, str] | None = None,
         input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd or REPO_ROOT,
        env=env,
        input=input_text,
        capture_output=True,
        text=True,
        timeout=90,
    )


def _parse_section(section: str) -> list[str]:
    entries: list[str] = []
    grab = False
    for raw in MANIFEST.read_text().splitlines():
        if raw == f"{section}:":
            grab = True
            continue
        if re.match(r"^[A-Za-z_]+:", raw):
            grab = False
        if grab and re.match(r"^\s*-\s+", raw):
            item = re.sub(r"^\s*-\s+", "", raw)
            item = re.sub(r"\s+#.*$", "", item).strip()
            if item:
                entries.append(item)
    return entries


def _seed_mapping() -> list[tuple[str, str]]:
    mapped: list[tuple[str, str]] = []
    for entry in _parse_section("template_seed"):
        if " -> " in entry:
            src, dst = entry.split(" -> ", 1)
        else:
            src = dst = entry
        mapped.append((src, dst))
    return mapped


def _direct_framework_files() -> list[tuple[Path, Path]]:
    excluded = _parse_section("direct_exclude")

    def is_excluded(relative: str) -> bool:
        return any(
            relative == item or relative.startswith(item.rstrip("/") + "/")
            for item in excluded
        )

    mapped: list[tuple[Path, Path]] = []
    for entry in _parse_section("framework"):
        source = REPO_ROOT / entry
        if source.is_file() and not is_excluded(entry):
            mapped.append((source, Path(entry)))
        elif source.is_dir():
            mapped.extend(
                (path, path.relative_to(REPO_ROOT))
                for path in source.rglob("*")
                if path.is_file() and not is_excluded(str(path.relative_to(REPO_ROOT)))
            )
    return sorted(mapped, key=lambda pair: str(pair[1]))


def _profile_skill_names(profile: Path) -> set[str]:
    text = profile.read_text()
    block = text.split("\nskills:\n", 1)[1].split("\n# --- Agent Registry", 1)[0]
    return set(re.findall(r"^    - ([A-Za-z0-9_-]+)$", block, re.MULTILINE))


def _install_direct(
    target: Path, *, force: bool = False, profile: str | None = None,
) -> None:
    cmd = ["bash", str(DIRECT_INSTALLER), "--target", str(target)]
    if force:
        cmd.append("--force")
    if profile:
        cmd.extend(["--profile", profile])
    result = _run(cmd)
    assert result.returncode == 0, result.stdout + result.stderr


def _install_plugin(target: Path, *, profile: str | None = None) -> None:
    env = os.environ.copy()
    env["CLAUDE_PLUGIN_ROOT"] = str(PLUGIN_ROOT)
    cmd = ["bash", str(PLUGIN_INSTALLER), "--target", str(target)]
    if profile:
        cmd.extend(["--profile", profile])
    result = _run(
        cmd,
        cwd=target,
        env=env,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def _assert_same(left: Path, right: Path) -> None:
    if left.is_file() and right.is_file():
        assert left.read_bytes() == right.read_bytes(), f"file mismatch: {left} != {right}"
        return
    assert left.is_dir() and right.is_dir(), f"type mismatch: {left} != {right}"
    left_files = sorted(p.relative_to(left) for p in left.rglob("*") if p.is_file())
    right_files = sorted(p.relative_to(right) for p in right.rglob("*") if p.is_file())
    assert left_files == right_files, f"tree paths differ: {left} != {right}"
    for rel in left_files:
        assert (left / rel).read_bytes() == (right / rel).read_bytes(), f"tree mismatch: {rel}"


def _tree_digest(path: Path) -> str:
    digest = hashlib.sha256()
    if path.is_file():
        digest.update(path.read_bytes())
        return digest.hexdigest()
    for child in sorted(p for p in path.rglob("*") if p.is_file()):
        digest.update(str(child.relative_to(path)).encode())
        digest.update(b"\0")
        digest.update(child.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


@pytest.fixture
def direct_repo(tmp_path: Path) -> Path:
    target = tmp_path / "direct"
    target.mkdir()
    _install_direct(target)
    return target


@pytest.fixture
def plugin_repo(tmp_path: Path) -> Path:
    target = tmp_path / "plugin"
    target.mkdir()
    _install_plugin(target)
    return target


def test_clean_direct_install_uses_generic_authority_seeds(direct_repo: Path) -> None:
    assert (direct_repo / "PRD.md").read_bytes() == (REPO_ROOT / "PRD_template.md").read_bytes()
    assert (direct_repo / "PRD.md").read_bytes() != (REPO_ROOT / "PRD.md").read_bytes()
    _assert_same(direct_repo / "SoT", REPO_ROOT / "SoT_template")
    assert (direct_repo / "SoT").resolve() != (REPO_ROOT / "SoT").resolve()

    installed_docs = {
        str(p.relative_to(direct_repo / "docs"))
        for p in (direct_repo / "docs").rglob("*") if p.is_file()
    }
    assert installed_docs == ALLOWED_DOCS
    assert not (direct_repo / "CLAUDE_plugin_stub.md").exists()
    assert not (direct_repo / ".claude" / "skills" / "init").exists()
    assert not (direct_repo / ".claude" / "skills" / "ghm-template-sync").exists()
    assert not (direct_repo / ".claude" / "skills" / "SKILL_TEMPLATE").exists()
    assert not (direct_repo / ".claude" / "skills" / "README.md").exists()
    assert not (direct_repo / ".claude" / "skills" / "skills-inventory.md").exists()
    for relative in DIRECT_SOURCE_ONLY_PATHS:
        assert not (direct_repo / relative).exists(), relative
    for relative in ("README_template.md", "PRD_template.md", "SoT_template"):
        _assert_same(direct_repo / relative, REPO_ROOT / relative)
    for excluded in EXCLUDED_DISTRIBUTABLE_FILES:
        assert not any(p.name == excluded for p in direct_repo.rglob("*"))


def test_clean_direct_install_contains_every_effective_framework_file(
    direct_repo: Path,
) -> None:
    expected = _direct_framework_files()
    assert expected
    for source, relative in expected:
        installed = direct_repo / relative
        assert installed.is_file(), relative
        assert installed.read_bytes() == source.read_bytes(), relative


def test_excluded_maintainer_artifacts_are_not_distributable() -> None:
    reusable = _iter_reusable_source_files()
    assert not ({p.name for p in reusable} & EXCLUDED_DISTRIBUTABLE_FILES)
    assert not ({p.name for p in PLUGIN_ROOT.rglob("*")} & EXCLUDED_DISTRIBUTABLE_FILES)


def test_direct_and_plugin_consumer_scaffolds_are_equivalent(
    direct_repo: Path, plugin_repo: Path,
) -> None:
    for _, destination in _seed_mapping():
        _assert_same(direct_repo / destination, plugin_repo / destination)
    _assert_same(
        direct_repo / ".claude" / "domain-profile.yaml",
        plugin_repo / ".claude" / "domain-profile.yaml",
    )
    for doc in ALLOWED_DOCS:
        _assert_same(direct_repo / "docs" / doc, plugin_repo / "docs" / doc)
    assert {p.name for p in (plugin_repo / "docs").iterdir()} == ALLOWED_DOCS


def test_every_mutable_seed_has_a_distinct_source_and_canonical_plugin_init_uses_it(
    tmp_path: Path,
) -> None:
    mapping = _seed_mapping()
    assert {destination for _, destination in mapping} == MUTABLE_SEED_DESTINATIONS
    assert all(source != destination for source, destination in mapping)
    target = tmp_path / "canonical-plugin-init"
    target.mkdir()
    env = os.environ.copy()
    env.pop("CLAUDE_PLUGIN_ROOT", None)

    result = _run(
        ["bash", str(CANONICAL_PLUGIN_INSTALLER), "--target", str(target)],
        cwd=target,
        env=env,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    for source, destination in mapping:
        _assert_same(REPO_ROOT / source, target / destination)


def test_seeded_profile_registers_only_shipped_runtime_skills(direct_repo: Path) -> None:
    names = _profile_skill_names(direct_repo / ".claude" / "domain-profile.yaml")
    assert names
    assert "SKILL_TEMPLATE" not in names
    missing_direct = {
        name for name in names
        if not (direct_repo / ".claude" / "skills" / name / "SKILL.md").is_file()
    }
    missing_plugin = {
        name for name in names
        if not (PLUGIN_ROOT / "skills" / name / "SKILL.md").is_file()
    }
    assert not missing_direct
    assert not missing_plugin


def test_non_default_profile_is_equivalent_and_only_applies_to_new_seed(tmp_path: Path) -> None:
    direct = tmp_path / "direct-profile"
    plugin = tmp_path / "plugin-profile"
    direct.mkdir()
    plugin.mkdir()
    _install_direct(direct, profile="library")
    _install_plugin(plugin, profile="library")
    _assert_same(
        direct / ".claude" / "domain-profile.yaml",
        plugin / ".claude" / "domain-profile.yaml",
    )
    assert "profile: library" in (direct / ".claude" / "domain-profile.yaml").read_text()


def test_plugin_init_requires_python_before_writing(tmp_path: Path) -> None:
    target = tmp_path / "target"
    minimal_bin = tmp_path / "bin"
    target.mkdir()
    minimal_bin.mkdir()
    (minimal_bin / "dirname").symlink_to("/usr/bin/dirname")
    result = _run(
        ["/bin/bash", str(PLUGIN_INSTALLER), "--target", str(target), "--profile", "library"],
        cwd=target,
        env={**os.environ, "PATH": str(minimal_bin), "CLAUDE_PLUGIN_ROOT": str(PLUGIN_ROOT)},
    )
    assert result.returncode != 0
    assert "python3 is required; no files were seeded" in result.stderr
    assert list(target.iterdir()) == []


def test_plugin_init_requires_awk_before_writing(tmp_path: Path) -> None:
    target = tmp_path / "target"
    minimal_bin = tmp_path / "bin"
    target.mkdir()
    minimal_bin.mkdir()
    for name in ("dirname", "python3"):
        resolved = shutil.which(name)
        assert resolved
        (minimal_bin / name).symlink_to(resolved)
    result = _run(
        ["/bin/bash", str(PLUGIN_INSTALLER), "--target", str(target)],
        cwd=target,
        env={**os.environ, "PATH": str(minimal_bin), "CLAUDE_PLUGIN_ROOT": str(PLUGIN_ROOT)},
    )
    assert result.returncode != 0
    assert "awk is required; no files were seeded" in result.stderr
    assert list(target.iterdir()) == []


@pytest.mark.parametrize("installer", ["direct", "plugin"])
def test_invalid_profile_fails_before_writing(tmp_path: Path, installer: str) -> None:
    target = tmp_path / installer
    target.mkdir()
    if installer == "direct":
        cmd = ["bash", str(DIRECT_INSTALLER), "--target", str(target),
               "--profile", "prodcut"]
        env = os.environ.copy()
    else:
        cmd = ["bash", str(PLUGIN_INSTALLER), "--target", str(target),
               "--profile", "prodcut"]
        env = {**os.environ, "CLAUDE_PLUGIN_ROOT": str(PLUGIN_ROOT)}
    result = _run(cmd, cwd=target, env=env)
    assert result.returncode == 2
    assert "unknown profile" in result.stderr.casefold()
    assert list(target.iterdir()) == []


@pytest.mark.parametrize(
    ("link_relative", "outside_is_directory"),
    [
        (Path(".claude/settings.json"), False),
        (Path(".claude/hooks"), True),
    ],
)
def test_direct_installer_refuses_symlink_destinations_before_any_write(
    tmp_path: Path, link_relative: Path, outside_is_directory: bool,
) -> None:
    target = tmp_path / "direct-target"
    outside = tmp_path / "outside"
    target.mkdir()
    link = target / link_relative
    link.parent.mkdir(parents=True, exist_ok=True)
    if outside_is_directory:
        outside.mkdir()
        sentinel = outside / "sentinel.txt"
        sentinel.write_text("outside directory sentinel\n")
        link.symlink_to(outside, target_is_directory=True)
    else:
        outside.write_text('{"hooks": {}, "sentinel": "outside settings"}\n')
        sentinel = outside
        link.symlink_to(outside)
    before = sentinel.read_bytes()

    result = _run([
        "bash", str(DIRECT_INSTALLER), "--target", str(target), "--force",
    ])

    assert result.returncode != 0
    assert "refusing symlink" in (result.stdout + result.stderr)
    assert sentinel.read_bytes() == before
    assert not (target / "CLAUDE.md").exists()
    assert not (target / "README.md").exists()
    assert not (target / ".claude" / "VERSION").exists()


def test_plugin_init_refuses_symlink_seed_ancestor_before_any_write(tmp_path: Path) -> None:
    target = tmp_path / "plugin-target"
    outside = tmp_path / "outside-sot"
    target.mkdir()
    outside.mkdir()
    sentinel = outside / "sentinel.txt"
    sentinel.write_text("outside SoT sentinel\n")
    (target / "SoT").symlink_to(outside, target_is_directory=True)
    env = os.environ.copy()
    env.pop("CLAUDE_PLUGIN_ROOT", None)

    result = _run(
        ["bash", str(CANONICAL_PLUGIN_INSTALLER), "--target", str(target)],
        cwd=target,
        env=env,
    )

    assert result.returncode != 0
    assert "refusing symlink" in (result.stdout + result.stderr)
    assert sentinel.read_text() == "outside SoT sentinel\n"
    assert not (target / "README.md").exists()
    assert not (target / "PRD.md").exists()
    assert not (target / "CLAUDE.md").exists()
    assert not (target / ".claude").exists()


@pytest.mark.parametrize(
    ("installer", "ancestor"),
    [
        ("direct", Path(".claude")),
        ("direct", Path("docs")),
        ("plugin", Path(".claude")),
        ("plugin", Path("docs")),
    ],
)
def test_installers_refuse_non_directory_seed_ancestors_before_any_write(
    tmp_path: Path, installer: str, ancestor: Path,
) -> None:
    target = tmp_path / f"{installer}-{ancestor.name}"
    target.mkdir()
    conflict = target / ancestor
    conflict.write_text("consumer ancestor sentinel\n")
    if installer == "direct":
        cmd = ["bash", str(DIRECT_INSTALLER), "--target", str(target)]
        env = os.environ.copy()
    else:
        cmd = ["bash", str(CANONICAL_PLUGIN_INSTALLER), "--target", str(target)]
        env = os.environ.copy()
        env.pop("CLAUDE_PLUGIN_ROOT", None)

    result = _run(cmd, cwd=target, env=env)

    assert result.returncode != 0
    assert "refusing non-directory target ancestor" in (result.stdout + result.stderr)
    assert conflict.read_text() == "consumer ancestor sentinel\n"
    assert sorted(path.relative_to(target) for path in target.rglob("*") if path.is_file()) == [
        ancestor,
    ]
    assert not (target / "CLAUDE.md").exists()
    assert not (target / "README.md").exists()


def test_agent_memory_seeds_are_empty_starters() -> None:
    memories = sorted((REPO_ROOT / ".claude" / "agents").glob("*/MEMORY.md"))
    assert len(memories) == 4
    reference_body = memories[0].read_text().splitlines()[1:]
    for memory in memories:
        payload = [
            line for line in memory.read_text().splitlines()[1:]
            if line.strip()
            and not line.startswith(">")
            and not line.startswith("## ")
            and not line.startswith("<!--")
        ]
        assert payload == [], f"prepopulated downstream memory: {memory}"
    for memory in memories[1:]:
        assert memory.read_text().splitlines()[1:] == reference_body


def _write_consumer_sentinels(repo: Path) -> dict[Path, str]:
    sentinels = {
        repo / "README.md": "consumer README\n",
        repo / "PRD.md": "consumer PRD\n",
        repo / "SoT" / "consumer-owned.md": "consumer SoT\n",
        repo / "epics" / "EPIC-999-consumer-owned.md": "consumer EPIC\n",
        repo / ".claude" / "agents" / "horizon" / "MEMORY.md": "consumer memory\n",
        repo / ".claude" / "domain-profile.yaml": "profile: consumer-owned\n",
        repo / "docs" / "consumer-owned.md": "consumer docs\n",
        repo / "docs" / "DEVELOPMENT_GRAPH.md": "consumer development-graph notes\n",
        repo / "docs" / "READINESS_PROTOCOL.md": "consumer readiness-protocol notes\n",
        repo / "scripts" / "consumer-owned.sh": "#!/bin/sh\n# consumer script\n",
        repo / ".claude" / "skills" / "consumer-owned" / "SKILL.md": "# Consumer skill\n",
        repo / ".claude" / "hooks" / "consumer-owned.sh": "#!/bin/sh\n# consumer hook\n",
        repo / ".claude" / "rules" / "consumer-owned.md": "# Consumer rule\n",
    }
    for path, content in sentinels.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    return sentinels


@pytest.mark.parametrize("installer", ["direct", "plugin"])
def test_reinstall_preserves_consumer_owned_content(tmp_path: Path, installer: str) -> None:
    target = tmp_path / installer
    target.mkdir()
    if installer == "direct":
        _install_direct(target)
    else:
        _install_plugin(target)

    sentinels = _write_consumer_sentinels(target)
    sot_before = _tree_digest(target / "SoT")
    if installer == "direct":
        _install_direct(target, force=True, profile="research")
    else:
        _install_plugin(target, profile="research")

    for path, content in sentinels.items():
        assert path.read_text() == content, f"reinstall overwrote {path.relative_to(target)}"
    assert _tree_digest(target / "SoT") == sot_before


def test_brownfield_direct_install_merges_canonical_closure_and_preserves_custom_files(
    tmp_path: Path,
) -> None:
    target = tmp_path / "brownfield"
    target.mkdir()
    custom = {
        target / ".claude" / "hooks" / "custom-hook.sh": "#!/bin/sh\n# custom hook\n",
        target / ".claude" / "skills" / "custom-skill" / "SKILL.md": "# Custom skill\n",
        target / ".claude" / "rules" / "custom-rule.md": "# Custom rule\n",
    }
    for path, content in custom.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    canonical_drift = target / ".claude" / "hooks" / "context-density-gate.sh"
    canonical_drift.write_text("#!/bin/sh\n# consumer-modified canonical hook\n")
    settings_path = target / ".claude" / "settings.json"
    settings_path.write_text(json.dumps({
        "hooks": {
            "Stop": [{"hooks": [{"type": "command", "command": "bash custom-stop.sh"}]}],
        },
        "permissions": {"allow": ["Custom(permission)"]},
        "consumer_key": True,
    }, indent=2) + "\n")

    _install_direct(target)

    for path, content in custom.items():
        assert path.read_text() == content
    for source, relative in _direct_framework_files():
        if relative == Path(".claude/settings.json"):
            continue
        installed = target / relative
        assert installed.is_file(), relative
        if relative == Path(".claude/hooks/context-density-gate.sh"):
            assert installed.read_text() == "#!/bin/sh\n# consumer-modified canonical hook\n"
            continue
        assert installed.read_bytes() == source.read_bytes(), relative

    canonical_settings = json.loads((REPO_ROOT / ".claude" / "settings.json").read_text())
    installed_settings = json.loads(settings_path.read_text())
    installed_commands = {
        handler.get("command")
        for groups in installed_settings["hooks"].values()
        for group in groups
        for handler in group.get("hooks", [])
    }
    canonical_commands = {
        handler["command"]
        for groups in canonical_settings["hooks"].values()
        for group in groups
        for handler in group.get("hooks", [])
        if handler.get("command")
    }
    assert canonical_commands <= installed_commands
    assert "bash custom-stop.sh" in installed_commands
    assert installed_settings["permissions"] == {"allow": ["Custom(permission)"]}
    assert installed_settings["consumer_key"] is True
    for command in canonical_commands:
        for relative in re.findall(r"\.claude/hooks/[A-Za-z0-9_.-]+", command):
            assert (target / relative).is_file(), relative


def test_no_force_rejects_hook_file_type_conflict_before_copy_and_force_repairs_it(
    tmp_path: Path,
) -> None:
    target = tmp_path / "hook-type-conflict"
    conflict = target / ".claude" / "hooks" / "context-validation.sh"
    conflict.mkdir(parents=True)
    sentinel = conflict / "consumer-sentinel.txt"
    sentinel.write_text("consumer hook conflict\n")

    result = _run(["bash", str(DIRECT_INSTALLER), "--target", str(target)])

    assert result.returncode != 0
    assert "framework hook destination is not a file" in result.stderr
    assert sentinel.read_text() == "consumer hook conflict\n"
    assert not (target / "CLAUDE.md").exists()
    assert not (target / "README.md").exists()
    assert not (target / ".claude" / "VERSION").exists()

    forced = _run([
        "bash", str(DIRECT_INSTALLER), "--target", str(target), "--force",
    ])
    assert forced.returncode == 0, forced.stdout + forced.stderr
    assert conflict.is_file()
    assert conflict.read_bytes() == (
        REPO_ROOT / ".claude" / "hooks" / "context-validation.sh"
    ).read_bytes()


def test_source_run_boundary_prevents_consumer_a_seed_customizations_from_reaching_b(
    tmp_path: Path,
) -> None:
    consumer_a = tmp_path / "consumer-a"
    consumer_b = tmp_path / "consumer-b"
    consumer_a.mkdir()
    consumer_b.mkdir()
    _install_direct(consumer_a)

    assert {destination for _, destination in _seed_mapping()} == MUTABLE_SEED_DESTINATIONS

    for relative in DIRECT_SOURCE_ONLY_PATHS:
        assert not (consumer_a / relative).exists(), relative
    for relative in ("README_template.md", "PRD_template.md", "SoT_template"):
        _assert_same(consumer_a / relative, REPO_ROOT / relative)

    for _, destination in _seed_mapping():
        path = consumer_a / destination
        if path.is_dir():
            shutil.rmtree(path)
            path.mkdir()
            (path / "consumer-a-sentinel.txt").write_text("consumer A private seed mutation\n")
        else:
            path.write_text(f"consumer A private seed mutation: {destination}\n")

    for relative in ("README_template.md", "PRD_template.md", "SoT_template"):
        _assert_same(consumer_a / relative, REPO_ROOT / relative)

    # Consumer A is not an install authority; B is independently installed from trusted source.
    _install_direct(consumer_b)
    for source, destination in _seed_mapping():
        _assert_same(REPO_ROOT / source, consumer_b / destination)
        if (consumer_b / destination).is_file():
            assert "consumer A private seed mutation" not in (
                consumer_b / destination
            ).read_text(errors="replace")
        else:
            assert not (consumer_b / destination / "consumer-a-sentinel.txt").exists()


def test_force_upgrade_retires_only_fingerprinted_framework_artifacts(tmp_path: Path) -> None:
    target = tmp_path / "upgrade"
    target.mkdir()
    _install_direct(target)

    scan_roots = _parse_section("obsolete_framework_scan_roots")
    fingerprints = set(_parse_section("obsolete_framework_fingerprints"))
    historical = _run([
        "git", "ls-tree", "-r", "-t", "--full-tree",
        LEGACY_FRAMEWORK_BASELINE, "--", *scan_roots,
    ])
    assert historical.returncode == 0, historical.stderr
    resolved: dict[str, str] = {}
    for line in historical.stdout.splitlines():
        metadata, rel = line.split("\t", 1)
        object_type = metadata.split()[1]
        if hashlib.sha256(rel.encode()).hexdigest() in fingerprints:
            resolved[rel] = object_type
    assert {
        hashlib.sha256(rel.encode()).hexdigest() for rel in resolved
    } == fingerprints

    retired_paths: list[Path] = []
    for rel in sorted(resolved, key=lambda item: item.count("/")):
        path = target / rel
        retired_paths.append(path)
        if resolved[rel] == "tree":
            path.mkdir(parents=True, exist_ok=True)
            (path / "legacy-artifact.txt").write_text("retired framework artifact\n")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("retired framework artifact\n")

    custom_doc = target / "docs" / "consumer-owned.md"
    custom_script = target / "scripts" / "consumer-owned.sh"
    custom_doc.write_text("consumer doc\n")
    custom_script.write_text("#!/bin/sh\n# consumer script\n")

    settings_path = target / ".claude" / "settings.json"
    settings = json.loads(settings_path.read_text())
    settings.setdefault("hooks", {})["Stop"] = [
        {"hooks": [{
            "type": "command",
            "command": 'bash "$CLAUDE_PROJECT_DIR"/.claude/hooks/sot-update-trigger.sh',
        }]},
        {"hooks": [{"type": "command", "command": "bash custom-stop.sh"}]},
        {"hooks": [{
            "type": "command",
            "command": 'bash custom-wrapper.sh --note=.claude/hooks/sot-update-trigger.sh',
        }]},
        {"hooks": [{
            "type": "command",
            "command": 'bash "$CLAUDE_PROJECT_DIR"/.claude/hooks/sot-update-trigger.sh.backup',
        }]},
    ]
    settings_path.write_text(json.dumps(settings, indent=2) + "\n")

    _install_direct(target, force=True)

    assert retired_paths
    assert not [path for path in retired_paths if path.exists()]
    assert custom_doc.read_text() == "consumer doc\n"
    assert custom_script.read_text() == "#!/bin/sh\n# consumer script\n"
    upgraded = json.loads(settings_path.read_text())
    stop_commands = {
        handler.get("command")
        for group in upgraded.get("hooks", {}).get("Stop", [])
        for handler in group.get("hooks", [])
    }
    assert "bash custom-stop.sh" in stop_commands
    assert 'bash custom-wrapper.sh --note=.claude/hooks/sot-update-trigger.sh' in stop_commands
    assert (
        'bash "$CLAUDE_PROJECT_DIR"/.claude/hooks/sot-update-trigger.sh.backup'
        in stop_commands
    )
    assert (
        'bash "$CLAUDE_PROJECT_DIR"/.claude/hooks/sot-update-trigger.sh'
        not in stop_commands
    )


def test_settings_merge_refreshes_framework_groups_and_preserves_custom_handlers(
    tmp_path: Path,
) -> None:
    source_path = REPO_ROOT / ".claude" / "settings.json"
    source = json.loads(source_path.read_text())
    canonical_group = source["hooks"]["SessionStart"][0]
    canonical_command = canonical_group["hooks"][0]["command"]
    target_path = tmp_path / "settings.json"
    target_path.write_text(json.dumps({
        "hooks": {
            "SessionStart": [{
                "matcher": "stale-framework-metadata",
                "hooks": [
                    {"type": "command", "command": canonical_command, "timeout": 999},
                    {"type": "command", "command": "bash custom-session-start.sh", "timeout": 3},
                ],
            }],
            "Stop": [{
                "matcher": "consumer-owned-noncanonical-event",
                "hooks": [{
                    "type": "command",
                    "command": canonical_command,
                    "timeout": 17,
                }],
            }],
        },
        "permissions": {"allow": ["Custom(permission)"]},
        "consumer_key": True,
    }, indent=2) + "\n")

    result = _run([
        sys.executable,
        str(REPO_ROOT / "scripts" / "_merge_settings.py"),
        str(source_path),
        str(target_path),
    ])
    assert result.returncode == 0, result.stdout + result.stderr
    merged = json.loads(target_path.read_text())
    groups = merged["hooks"]["SessionStart"]
    assert canonical_group in groups
    canonical_handlers = [
        handler
        for group in groups
        for handler in group.get("hooks", [])
        if handler.get("command") == canonical_command
    ]
    assert canonical_handlers == canonical_group["hooks"]
    assert any(
        handler.get("command") == "bash custom-session-start.sh"
        for group in groups for handler in group.get("hooks", [])
    )
    assert {
        "matcher": "consumer-owned-noncanonical-event",
        "hooks": [{
            "type": "command",
            "command": canonical_command,
            "timeout": 17,
        }],
    } in merged["hooks"]["Stop"]
    assert merged["permissions"] == {"allow": ["Custom(permission)"]}
    assert merged["consumer_key"] is True


def test_installer_rejects_invalid_target_settings_before_writing(tmp_path: Path) -> None:
    target = tmp_path / "invalid-settings"
    settings = target / ".claude" / "settings.json"
    settings.parent.mkdir(parents=True)
    settings.write_text("{ invalid json\n")

    result = _run([
        "bash", str(DIRECT_INSTALLER), "--target", str(target), "--force",
    ])
    assert result.returncode != 0
    assert "invalid target settings JSON" in result.stderr
    assert settings.read_text() == "{ invalid json\n"
    assert not (target / "CLAUDE.md").exists()
    assert not (target / "README.md").exists()


def test_installer_rejects_malformed_hook_schema_before_writing(tmp_path: Path) -> None:
    target = tmp_path / "malformed-hooks"
    settings = target / ".claude" / "settings.json"
    settings.parent.mkdir(parents=True)
    malformed = json.dumps({
        "hooks": {"SessionStart": {"hooks": []}},
        "permissions": {"allow": ["Custom(permission)"]},
    }, indent=2) + "\n"
    settings.write_text(malformed)

    result = _run([
        "bash", str(DIRECT_INSTALLER), "--target", str(target), "--force",
    ])

    assert result.returncode != 0
    assert "invalid target settings JSON" in result.stderr
    assert "each hooks event must map to a list of groups" in result.stderr
    assert settings.read_text() == malformed
    assert sorted(path.relative_to(target) for path in target.rglob("*") if path.is_file()) == [
        Path(".claude/settings.json"),
    ]


def test_installer_rejects_null_hook_command_before_writing(tmp_path: Path) -> None:
    target = tmp_path / "null-hook-command"
    settings = target / ".claude" / "settings.json"
    settings.parent.mkdir(parents=True)
    malformed = json.dumps({
        "hooks": {
            "SessionStart": [{"hooks": [{"type": "command", "command": None}]}],
        },
    }, indent=2) + "\n"
    settings.write_text(malformed)

    result = _run([
        "bash", str(DIRECT_INSTALLER), "--target", str(target), "--force",
    ])

    assert result.returncode != 0
    assert "handler command must be a string" in result.stderr
    assert settings.read_text() == malformed
    assert sorted(path.relative_to(target) for path in target.rglob("*") if path.is_file()) == [
        Path(".claude/settings.json"),
    ]


def test_direct_installer_reports_missing_readiness_dependency(tmp_path: Path) -> None:
    target = tmp_path / "target"
    bin_dir = tmp_path / "bin"
    target.mkdir()
    bin_dir.mkdir()
    real_python = shutil.which("python3")
    assert real_python
    wrapper = bin_dir / "python3"
    wrapper.write_text(
        "#!/bin/sh\n"
        "if [ \"$1\" = \"-c\" ] && [ \"$2\" = \"import yaml\" ]; then exit 1; fi\n"
        f'exec "{real_python}" "$@"\n'
    )
    wrapper.chmod(0o755)

    result = _run(
        ["bash", str(DIRECT_INSTALLER), "--target", str(target), "--dry-run"],
        env={**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}"},
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "readiness dependency missing: PyYAML" in result.stdout
    assert "scripts/requirements.txt" in result.stdout
    assert list(target.iterdir()) == []


def test_readiness_missing_startup_dependency_exits_three_and_removes_stale_output(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "missing-readiness-dependency"
    readiness_path = repo / "status" / "readiness.json"
    readiness_path.parent.mkdir(parents=True)
    readiness_path.write_text('{"sentinel": "stale readiness must not survive"}\n')

    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    env["PYTHONNOUSERSITE"] = "1"
    result = _run(
        [
            sys.executable,
            "-S",
            str(REPO_ROOT / "scripts" / "readiness.py"),
            "run",
            "--repo",
            str(repo),
            "--quiet",
        ],
        cwd=repo,
        env=env,
    )

    assert result.returncode == 3, result.stdout + result.stderr
    assert "startup dependency/import failed" in result.stderr
    assert "PyYAML" in result.stderr
    assert "scripts/requirements.txt" in result.stderr
    assert not readiness_path.exists()


def test_readiness_missing_scorer_invalidates_run_but_status_remains_read_only(
    tmp_path: Path,
) -> None:
    runtime = tmp_path / "incomplete-runtime"
    runtime.mkdir()
    isolated_readiness = runtime / "readiness.py"
    shutil.copy2(REPO_ROOT / "scripts" / "readiness.py", isolated_readiness)

    repo = tmp_path / "consumer"
    readiness_path = repo / "status" / "readiness.json"
    readiness_path.parent.mkdir(parents=True)
    stale = '{"sentinel": "status must not mutate existing evidence"}\n'
    readiness_path.write_text(stale)

    failed_run = _run([
        sys.executable,
        str(isolated_readiness),
        "run",
        "--repo",
        str(repo),
        "--quiet",
    ], cwd=repo)

    assert failed_run.returncode == 3, failed_run.stdout + failed_run.stderr
    assert "one or more scorer scripts missing" in failed_run.stderr
    assert not readiness_path.exists()

    readiness_path.write_text(stale)
    status = _run([
        sys.executable,
        str(isolated_readiness),
        "status",
        "--repo",
        str(repo),
        "--quiet",
    ], cwd=repo)

    assert status.returncode == 0, status.stdout + status.stderr
    assert readiness_path.read_text() == stale


@pytest.mark.parametrize(
    ("framework_path", "protected_path", "source_file"),
    [
        ("PRD.md", "PRD.md", "PRD.md"),
        ("epics", "epics/EPIC-*.md", "epics/README.md"),
    ],
)
def test_installer_rejects_framework_never_touch_overlap(
    tmp_path: Path, framework_path: str, protected_path: str, source_file: str,
) -> None:
    source = tmp_path / "invalid-source"
    target = tmp_path / "target"
    (source / ".claude").mkdir(parents=True)
    target.mkdir()
    shutil.copy2(DIRECT_INSTALLER, source / "install.sh")
    collision_source = source / source_file
    collision_source.parent.mkdir(parents=True, exist_ok=True)
    collision_source.write_text("framework collision\n")
    (source / ".claude" / "install-manifest.yaml").write_text(
        f"framework:\n  - {framework_path}\ntemplate_seed: []\n"
        f"never_touch:\n  - {protected_path}\n"
    )
    result = _run(["bash", str(source / "install.sh"), "--target", str(target)])
    assert result.returncode != 0
    assert "manifest ownership overlap" in result.stderr
    assert not (target / framework_path).exists()


def test_installer_rejects_broad_framework_root_before_writing(tmp_path: Path) -> None:
    source = tmp_path / "unsafe-source"
    target = tmp_path / "target"
    (source / ".claude").mkdir(parents=True)
    target.mkdir()
    shutil.copy2(DIRECT_INSTALLER, source / "install.sh")
    (source / ".claude" / "install-manifest.yaml").write_text(
        "framework:\n  - .\ndirect_exclude: []\ntemplate_seed: []\nnever_touch: []\n"
    )

    result = _run(["bash", str(source / "install.sh"), "--target", str(target)])

    assert result.returncode != 0
    assert "unsafe framework path: '.'" in result.stderr
    assert list(target.iterdir()) == []


def test_installer_rejects_obsolete_never_touch_overlap(tmp_path: Path) -> None:
    source = tmp_path / "invalid-source"
    target = tmp_path / "target"
    (source / ".claude").mkdir(parents=True)
    target.mkdir()
    shutil.copy2(DIRECT_INSTALLER, source / "install.sh")
    protected_digest = hashlib.sha256(b"PRD.md").hexdigest()
    (source / ".claude" / "install-manifest.yaml").write_text(
        "framework: []\nobsolete_framework_scan_roots:\n  - docs\n"
        f"obsolete_framework_fingerprints:\n  - {protected_digest}\n"
        "template_seed: []\nnever_touch:\n  - PRD.md\n"
    )
    result = _run(["bash", str(source / "install.sh"), "--target", str(target), "--force"])
    assert result.returncode != 0
    assert "obsolete fingerprint intersects protected path" in result.stderr


def test_installer_rejects_obsolete_current_framework_overlap(tmp_path: Path) -> None:
    source = tmp_path / "invalid-source"
    target = tmp_path / "target"
    (source / ".claude").mkdir(parents=True)
    target.mkdir()
    shutil.copy2(DIRECT_INSTALLER, source / "install.sh")
    framework_digest = hashlib.sha256(b"install.sh").hexdigest()
    (source / ".claude" / "install-manifest.yaml").write_text(
        "framework:\n  - install.sh\ndirect_exclude: []\n"
        "obsolete_framework_scan_roots:\n  - scripts\n"
        f"obsolete_framework_fingerprints:\n  - {framework_digest}\n"
        "template_seed: []\nnever_touch: []\n"
    )
    result = _run(["bash", str(source / "install.sh"), "--target", str(target), "--force"])
    assert result.returncode != 0
    assert "obsolete fingerprint intersects current framework path" in result.stderr
    assert not (target / "install.sh").exists()


def test_clean_sot_seed_has_no_accepted_template_ids(direct_repo: Path) -> None:
    content_files = sorted(
        p for p in (direct_repo / "SoT").glob("SoT.*.md")
        if p.name not in {"SoT.README.md", "SoT.UNIQUE_ID_SYSTEM.md"}
    )
    assert content_files
    for path in content_files:
        assert "template_state: uninitialized" in path.read_text(), path

    scope = [str(path.relative_to(direct_repo)) for path in content_files]
    result = _run(
        ["bash", str(direct_repo / "scripts" / "validate-ids.sh"), "--scope", *scope],
        cwd=direct_repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(direct_repo)},
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Definitions: 0" in result.stdout


@pytest.mark.parametrize("fixture_name", ["direct_repo", "plugin_repo"])
def test_default_id_validation_is_clean_on_new_scaffold(
    request: pytest.FixtureRequest, fixture_name: str,
) -> None:
    repo = request.getfixturevalue(fixture_name)
    validator = repo / "scripts" / "validate-ids.sh"
    if not validator.exists():
        validator = PLUGIN_ROOT / "scripts" / "validate-ids.sh"
    result = _run(
        ["bash", str(validator), "--quiet"],
        cwd=repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)},
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_default_id_validation_handles_empty_repo(tmp_path: Path) -> None:
    empty_repo = tmp_path / "empty"
    empty_repo.mkdir()
    result = _run(
        ["bash", str(REPO_ROOT / "scripts" / "validate-ids.sh"), "--quiet"],
        cwd=empty_repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(empty_repo)},
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_explicit_empty_id_registry_fails_closed(tmp_path: Path) -> None:
    repo = tmp_path / "closed-registry"
    (repo / ".claude").mkdir(parents=True)
    (repo / ".claude" / "domain-profile.yaml").write_text(
        "profile: product\nid_prefixes: {}\n"
    )

    env = {**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)}
    pattern = _run(
        ["bash", str(REPO_ROOT / "scripts" / "generate-id-pattern.sh")],
        cwd=repo,
        env=env,
    )
    assert pattern.returncode == 2
    assert pattern.stdout == ""
    assert "declares no readable id_prefixes" in pattern.stderr

    validation = _run(
        ["bash", str(REPO_ROOT / "scripts" / "validate-ids.sh"), "--quiet"],
        cwd=repo,
        env=env,
    )
    assert validation.returncode == 2
    assert "unable to load registered ID prefixes" in validation.stderr


def test_explicit_id_registry_is_closed_for_shell_validation(tmp_path: Path) -> None:
    repo = tmp_path / "custom-registry"
    (repo / ".claude").mkdir(parents=True)
    (repo / "SoT").mkdir()
    (repo / ".claude" / "domain-profile.yaml").write_text(
        "profile: custom\n"
        "id_prefixes:\n"
        "  ZZZ: { file: \"SoT/SoT.CUSTOM.md\", description: \"custom\" }\n"
    )
    (repo / "epics").mkdir()
    (repo / "PRD.md").write_text(
        "# PRD\n\nAccepted: ZZZ-001. Outside registry: BR-001 and EPIC-01.\n"
    )
    (repo / "SoT" / "SoT.CUSTOM.md").write_text(
        "## ZZZ-001: Registered record\n\nDefined only in the explicit custom registry.\n"
    )
    (repo / "epics" / "EPIC-01.md").write_text("# EPIC-01 Unregistered execution record\n")

    env = {**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)}
    pattern = _run(
        ["bash", str(REPO_ROOT / "scripts" / "generate-id-pattern.sh")],
        cwd=repo,
        env=env,
    )
    assert pattern.returncode == 0, pattern.stderr
    assert pattern.stdout.strip() == "(ZZZ)"

    validation = _run(
        ["bash", str(REPO_ROOT / "scripts" / "validate-ids.sh")],
        cwd=repo,
        env=env,
    )
    assert validation.returncode == 0, validation.stdout + validation.stderr
    assert "Definitions: 1" in validation.stdout
    assert "References:  1" in validation.stdout


def test_epic_only_registry_does_not_create_an_empty_general_id_arm(tmp_path: Path) -> None:
    repo = tmp_path / "epic-only-registry"
    (repo / ".claude").mkdir(parents=True)
    (repo / "SoT").mkdir()
    (repo / "epics").mkdir()
    (repo / ".claude" / "domain-profile.yaml").write_text(
        "profile: execution\n"
        "id_prefixes:\n"
        "  EPIC: { file: \"epics/\", description: \"execution\" }\n"
    )
    (repo / "PRD.md").write_text("# PRD\n\nApproved: EPIC-01. Malformed: -001.\n")
    (repo / "epics" / "EPIC-01.md").write_text("# EPIC-01 Valid execution record\n")
    (repo / "SoT" / "SoT.TESTING.md").write_text("## -001: Must not be a definition\n")

    result = _run(
        ["bash", str(REPO_ROOT / "scripts" / "validate-ids.sh")],
        cwd=repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)},
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Definitions: 1" in result.stdout
    assert "References:  1" in result.stdout


def test_compound_ids_use_registered_base_and_exactly_three_digits(tmp_path: Path) -> None:
    repo = tmp_path / "compound"
    (repo / ".claude").mkdir(parents=True)
    (repo / "SoT").mkdir()
    shutil.copy2(REPO_ROOT / ".claude" / "domain-profile.yaml", repo / ".claude")
    (repo / "PRD.md").write_text("# PRD\n\nAccepted: ADO-STAGE-001\n")
    (repo / "SoT" / "SoT.ADOPTION.md").write_text(
        "---\ntemplate_state: active\n---\n\n"
        "## ADO-STAGE-001: Adoption stage\n\nAccepted product record with rationale and evidence.\n"
    )

    prefix_result = _run(
        ["bash", str(REPO_ROOT / "scripts" / "generate-id-pattern.sh")],
        cwd=repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)},
    )
    assert prefix_result.returncode == 0
    full_pattern = prefix_result.stdout.strip() + r"(-[A-Z][A-Z0-9]*)?-[0-9]{3}"
    assert re.fullmatch(full_pattern, "ADO-STAGE-001")
    assert not re.fullmatch(full_pattern, "ADO-STAGE-01")

    result = _run(
        ["bash", str(REPO_ROOT / "scripts" / "validate-ids.sh"),
         "--scope", "PRD.md", "SoT/SoT.ADOPTION.md"],
        cwd=repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)},
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Definitions: 1" in result.stdout


def test_epic_ids_preserve_two_digit_execution_compatibility(tmp_path: Path) -> None:
    repo = tmp_path / "epic-ids"
    (repo / ".claude").mkdir(parents=True)
    (repo / "epics").mkdir()
    shutil.copy2(REPO_ROOT / ".claude" / "domain-profile.yaml", repo / ".claude")
    (repo / "PRD.md").write_text("# PRD\n\nApproved execution: EPIC-01\n")
    (repo / "epics" / "EPIC-01-foundations.md").write_text(
        "# EPIC-01 Foundations\n\nApproved implementation context with acceptance criteria.\n"
    )
    result = _run(
        ["bash", str(REPO_ROOT / "scripts" / "validate-ids.sh"),
         "--scope", "PRD.md", "epics/EPIC-01-foundations.md"],
        cwd=repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)},
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Definitions: 1" in result.stdout
    assert "References:  1" in result.stdout


def test_shell_id_validator_ignores_malformed_compounds_and_adjacent_text(tmp_path: Path) -> None:
    repo = tmp_path / "malformed-ids"
    (repo / ".claude").mkdir(parents=True)
    (repo / "SoT").mkdir()
    shutil.copy2(REPO_ROOT / ".claude" / "domain-profile.yaml", repo / ".claude")
    malformed = [
        "ADO-STAGE-EXTRA-001", "EPIC-SUB-001", "BR-001st", "EPIC-01x",
        "BR-001-extra",
    ]
    (repo / "PRD.md").write_text("# PRD\n\n" + " ".join(malformed) + "\n")
    (repo / "SoT" / "SoT.TESTING.md").write_text(
        "---\ntemplate_state: active\n---\n\n"
        + "\n\n".join(f"## {value}: malformed" for value in malformed)
        + "\n"
    )
    result = _run(
        ["bash", str(REPO_ROOT / "scripts" / "validate-ids.sh"),
         "--scope", "PRD.md", "SoT/SoT.TESTING.md"],
        cwd=repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)},
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Definitions: 0" in result.stdout
    assert "References:  0" in result.stdout


def test_shell_validator_includes_readme_owned_kpi_definitions(tmp_path: Path) -> None:
    repo = tmp_path / "readme-kpi"
    (repo / ".claude").mkdir(parents=True)
    shutil.copy2(REPO_ROOT / ".claude" / "domain-profile.yaml", repo / ".claude")
    (repo / "README.md").write_text(
        "# Dashboard\n\n## KPI-001: Activation\n\nAccepted metric definition and target.\n"
    )
    (repo / "PRD.md").write_text("# PRD\n\nTracks KPI-001.\n")

    result = _run(
        ["bash", str(REPO_ROOT / "scripts" / "validate-ids.sh")],
        cwd=repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)},
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Definitions: 1" in result.stdout
    assert "References:  1" in result.stdout
    assert "Issues:      0" in result.stdout


def test_shell_validator_excludes_nested_sot_archives(tmp_path: Path) -> None:
    repo = tmp_path / "nested-sot"
    (repo / ".claude").mkdir(parents=True)
    (repo / "SoT" / "archive").mkdir(parents=True)
    shutil.copy2(REPO_ROOT / ".claude" / "domain-profile.yaml", repo / ".claude")
    active = "## BR-001: Active rule\n\nAccepted rule with rationale and enforcement.\n"
    (repo / "SoT" / "SoT.BUSINESS_RULES.md").write_text(active)
    (repo / "SoT" / "archive" / "SoT.BUSINESS_RULES.md").write_text(active)
    (repo / "PRD.md").write_text("# PRD\n\nAccepts BR-001.\n")

    result = _run(
        ["bash", str(REPO_ROOT / "scripts" / "validate-ids.sh")],
        cwd=repo,
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(repo)},
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Definitions: 1" in result.stdout
    assert "Issues:      0" in result.stdout


def test_root_authority_graph_exposes_only_the_accepted_snapshot() -> None:
    result = _run(
        ["bash", str(REPO_ROOT / "scripts" / "validate-ids.sh")],
        env={**os.environ, "PRD_CE_PROJECT_ROOT": str(REPO_ROOT)},
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Definitions: 9" in result.stdout
    assert "References:  9" in result.stdout
    assert "Issues:      0" in result.stdout

    accepted_files = {"SoT.BUSINESS_RULES.md", "SoT.TECHNICAL_DECISIONS.md"}
    guide_files = {"SoT.README.md", "SoT.UNIQUE_ID_SYSTEM.md"}
    nonaccepted = sorted(
        path for path in (REPO_ROOT / "SoT").glob("SoT.*.md")
        if path.name not in accepted_files | guide_files
    )
    assert len(nonaccepted) == 10
    for markdown in nonaccepted:
        assert "template_state: uninitialized" in markdown.read_text(), markdown
        companion = REPO_ROOT / "SoT" / "html" / f"{markdown.stem}.html"
        assert companion.is_file(), companion
        rendered = companion.read_text().casefold()
        assert "uninitialized" in rendered and "non-authoritative" in rendered, companion


def test_context_hook_is_lifecycle_aware_and_ignores_epic_template(direct_repo: Path) -> None:
    hook = direct_repo / ".claude" / "hooks" / "context-validation.sh"
    nested = direct_repo / "src" / "nested"
    nested.mkdir(parents=True)
    hook_env = {**os.environ, "CLAUDE_PROJECT_DIR": str(direct_repo)}

    pre_build = _run(
        ["bash", str(hook)], cwd=nested, env=hook_env, input_text="{}",
    )
    assert pre_build.returncode == 0, pre_build.stderr
    pre_context = json.loads(pre_build.stdout)["hookSpecificOutput"]["additionalContext"]
    assert "Accepted `SoT/` records" in pre_context
    assert "EPICs not yet created (pre-v0.7)" in pre_context
    assert "EPIC_TEMPLATE" not in pre_context

    prd = direct_repo / "PRD.md"
    prd.write_text(prd.read_text().replace("version: 0.1", "version: 0.7", 1))
    malformed_epic = direct_repo / "epics" / "EPIC-0junk.md"
    malformed_epic.write_text("# EPIC-0junk\n\n> **State**: `In Progress`\n")
    missing = _run(["bash", str(hook)], cwd=nested, env=hook_env, input_text="{}")
    assert missing.returncode == 0, missing.stderr
    missing_context = json.loads(missing.stdout)["hookSpecificOutput"]["additionalContext"]
    assert "Missing active EPIC at lifecycle v0.7" in missing_context
    assert "EPIC_TEMPLATE" not in missing_context

    epic = direct_repo / "epics" / "EPIC-01-foundations.md"
    epic.write_text("# EPIC-01 Foundations\n\n> **State**: `In Progress`\n")
    active = _run(["bash", str(hook)], cwd=nested, env=hook_env, input_text="{}")
    assert active.returncode == 0, active.stderr
    active_context = json.loads(active.stdout)["hookSpecificOutput"]["additionalContext"]
    assert "epics/EPIC-01-foundations.md" in active_context


def test_subagent_memory_hooks_handle_plugin_scope_and_stop_retry(plugin_repo: Path) -> None:
    load_hook = PLUGIN_ROOT / "hooks" / "subagent-memory-load.sh"
    save_hook = PLUGIN_ROOT / "hooks" / "subagent-memory-save.sh"
    scoped = "prd-ce:horizon"
    nested = plugin_repo / "src" / "nested"
    nested.mkdir(parents=True)
    hook_env = {**os.environ, "CLAUDE_PROJECT_DIR": str(plugin_repo)}

    loaded = _run(
        ["bash", str(load_hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"agent_type": scoped}),
    )
    assert loaded.returncode == 0, loaded.stderr
    load_context = json.loads(loaded.stdout)["hookSpecificOutput"]["additionalContext"]
    assert ".claude/agents/horizon/MEMORY.md" in load_context
    assert "prd-ce:horizon" not in load_context

    bare = _run(
        ["bash", str(load_hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"agent_type": "horizon"}),
    )
    assert bare.returncode == 0, bare.stderr
    assert ".claude/agents/horizon/MEMORY.md" in json.loads(
        bare.stdout
    )["hookSpecificOutput"]["additionalContext"]

    invalid = _run(
        ["bash", str(load_hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"agent_type": "prd-ce:../horizon"}),
    )
    assert invalid.returncode == 0 and invalid.stdout == ""

    assert _run(["git", "init", "-q"], cwd=plugin_repo).returncode == 0
    memory = plugin_repo / ".claude" / "agents" / "horizon" / "MEMORY.md"
    memory_rel = str(memory.relative_to(plugin_repo))
    assert _run(["git", "add", memory_rel], cwd=plugin_repo).returncode == 0
    memory.write_text(memory.read_text() + "\n## Feedback\n\n- Extracted memory.\n")

    first = _run(
        ["bash", str(save_hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"agent_type": scoped, "stop_hook_active": False}),
    )
    assert first.returncode == 0, first.stderr
    first_context = json.loads(first.stdout)["hookSpecificOutput"]["additionalContext"]
    assert "MANDATORY: Memory Extraction Before Return" in first_context
    assert _run(["git", "diff", "--quiet", "--", memory_rel], cwd=plugin_repo).returncode == 1

    retry = _run(
        ["bash", str(save_hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"agent_type": scoped, "stop_hook_active": True}),
    )
    assert retry.returncode == 0, retry.stderr
    assert retry.stdout == ""
    assert _run(["git", "diff", "--quiet", "--", memory_rel], cwd=plugin_repo).returncode == 0

    foreign_load = _run(
        ["bash", str(load_hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"agent_type": "other-plugin:horizon"}),
    )
    assert foreign_load.returncode == 0 and foreign_load.stdout == ""

    memory.write_text(memory.read_text() + "\n- Foreign plugin must not stage this.\n")
    assert _run(["git", "diff", "--quiet", "--", memory_rel], cwd=plugin_repo).returncode == 1
    foreign_save = _run(
        ["bash", str(save_hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"agent_type": "other-plugin:horizon", "stop_hook_active": True}),
    )
    assert foreign_save.returncode == 0 and foreign_save.stdout == ""
    assert _run(["git", "diff", "--quiet", "--", memory_rel], cwd=plugin_repo).returncode == 1

    invalid_save = _run(
        ["bash", str(save_hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"agent_type": "prd-ce:../horizon", "stop_hook_active": False}),
    )
    assert invalid_save.returncode == 0 and invalid_save.stdout == ""


def test_subagent_memory_hook_json_round_trips_controls_and_unicode(plugin_repo: Path) -> None:
    memory = plugin_repo / ".claude" / "agents" / "horizon" / "MEMORY.md"
    control_fragment = "tab:\tvalue\r\nunicode: café ☃"
    memory.write_bytes(memory.read_bytes() + ("\n" + control_fragment).encode())
    nested = plugin_repo / "src" / "nested"
    nested.mkdir(parents=True)
    hook_env = {**os.environ, "CLAUDE_PROJECT_DIR": str(plugin_repo)}

    invocations = (
        (
            PLUGIN_ROOT / "hooks" / "subagent-memory-load.sh",
            {"agent_type": "prd-ce:horizon"},
        ),
        (
            PLUGIN_ROOT / "hooks" / "subagent-memory-save.sh",
            {"agent_type": "prd-ce:horizon", "stop_hook_active": False},
        ),
    )
    for hook, payload in invocations:
        result = _run(
            ["bash", str(hook)],
            cwd=nested,
            env=hook_env,
            input_text=json.dumps(payload),
        )
        assert result.returncode == 0, result.stderr
        assert "\t" not in result.stdout and "\r" not in result.stdout
        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        assert control_fragment in context


def test_traceability_and_sync_hooks_gate_product_config_from_nested_cwd(
    direct_repo: Path,
) -> None:
    trace_hook = direct_repo / ".claude" / "hooks" / "traceability-gate.sh"
    sync_hook = direct_repo / ".claude" / "hooks" / "sot-sync-reminder.sh"
    nested = direct_repo / "src" / "nested"
    nested.mkdir(parents=True, exist_ok=True)
    hook_env = {**os.environ, "CLAUDE_PROJECT_DIR": str(direct_repo)}

    planned = direct_repo / "epics" / "EPIC-02-planned.md"
    planned.write_text("# EPIC-02 Planned\n\n> **State**: `Planned`\n")
    malformed = direct_repo / "epics" / "EPIC-0junk.md"
    malformed.write_text("# EPIC-0junk\n\n> **State**: `In Progress`\n")
    product_input = json.dumps({"tool_input": {"file_path": "package.json"}})
    gated = _run(
        ["bash", str(trace_hook)], cwd=nested, env=hook_env, input_text=product_input,
    )
    assert gated.returncode == 0, gated.stderr
    decision = json.loads(gated.stdout)["hookSpecificOutput"]
    assert decision["permissionDecision"] == "ask"
    assert "found 0" in decision["permissionDecisionReason"]

    absolute_config = str(direct_repo / "config" / "app.yaml")
    config_input = json.dumps({"tool_input": {"file_path": absolute_config}})
    reminder = _run(
        ["bash", str(sync_hook)], cwd=nested, env=hook_env, input_text=config_input,
    )
    assert reminder.returncode == 0, reminder.stderr
    assert "SoT/ files should be updated" in json.loads(
        reminder.stdout
    )["hookSpecificOutput"]["additionalContext"]

    methodology_input = json.dumps({
        "tool_input": {"file_path": str(direct_repo / ".claude" / "domain-profile.yaml")}
    })
    for hook in (trace_hook, sync_hook):
        result = _run(
            ["bash", str(hook)], cwd=nested, env=hook_env, input_text=methodology_input,
        )
        assert result.returncode == 0 and result.stdout == ""

    active = direct_repo / "epics" / "EPIC-01-active.md"
    active.write_text("# EPIC-01 Active\n\n> **State**: `In Progress`\n")
    allowed = _run(
        ["bash", str(trace_hook)], cwd=nested, env=hook_env, input_text=product_input,
    )
    assert allowed.returncode == 0 and allowed.stdout == ""

    second = direct_repo / "epics" / "EPIC-003-other.md"
    second.write_text("# EPIC-003 Other\n\n> **State**: In Progress\n")
    ambiguous = _run(
        ["bash", str(trace_hook)], cwd=nested, env=hook_env, input_text=product_input,
    )
    assert ambiguous.returncode == 0, ambiguous.stderr
    assert "found 2" in json.loads(
        ambiguous.stdout
    )["hookSpecificOutput"]["permissionDecisionReason"]


def test_context_density_handles_epic_numbers_missing_files_and_sparse_epics(
    direct_repo: Path,
) -> None:
    hook = direct_repo / ".claude" / "hooks" / "context-density-gate.sh"
    nested = direct_repo / "src" / "nested"
    nested.mkdir(parents=True, exist_ok=True)
    hook_env = {**os.environ, "CLAUDE_PROJECT_DIR": str(direct_repo)}
    for number in ("08", "09", "001", "100"):
        suffix = "" if number == "08" else "-fixture"
        (direct_repo / "epics" / f"EPIC-{number}{suffix}.md").write_text(
            f"# EPIC-{number} Fixture\n\nShort context without accepted IDs.\n"
        )
        result = _run(
            ["bash", str(hook)], cwd=nested, env=hook_env,
            input_text=json.dumps({"prompt": f"continue EPIC-{number}"}),
        )
        assert result.returncode == 0, result.stderr
        context = json.loads(result.stdout)["hookSpecificOutput"]["additionalContext"]
        assert f"EPIC-{number}" in context
        assert "SPARSE" in context

    missing = _run(
        ["bash", str(hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"prompt": "continue EPIC-07"}),
    )
    assert missing.returncode == 0, missing.stderr
    missing_context = json.loads(missing.stdout)["hookSpecificOutput"]["additionalContext"]
    assert "EPIC-07" in missing_context and "Epic file not found" in missing_context

    profile = direct_repo / ".claude" / "domain-profile.yaml"
    profile.write_text(
        "profile: custom\n"
        "id_prefixes:\n"
        "  ZZZ: { file: \"SoT/SoT.TESTING.md\", description: \"custom\" }\n"
    )
    epic_08 = direct_repo / "epics" / "EPIC-08.md"
    epic_08.write_text("# EPIC-08 Fixture\n\nShort context with unregistered BR-001.\n")
    custom_registry = _run(
        ["bash", str(hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"prompt": "continue EPIC-08"}),
    )
    assert custom_registry.returncode == 0, custom_registry.stderr
    custom_context = json.loads(
        custom_registry.stdout
    )["hookSpecificOutput"]["additionalContext"]
    assert "SPARSE" in custom_context, "hook restored an unregistered BR fallback"

    profile.write_text("profile: invalid\nid_prefixes: {}\n")
    invalid_registry = _run(
        ["bash", str(hook)], cwd=nested, env=hook_env,
        input_text=json.dumps({"prompt": "continue EPIC-08"}),
    )
    assert invalid_registry.returncode == 0, invalid_registry.stderr
    invalid_context = json.loads(
        invalid_registry.stdout
    )["hookSpecificOutput"]["additionalContext"]
    assert "Registry Configuration Error" in invalid_context
    assert "SPARSE" not in invalid_context


def test_cascade_checklist_accepts_nonseekable_line_separated_stdin(direct_repo: Path) -> None:
    helper = direct_repo / ".claude" / "hooks" / "cascade_checklist.py"
    result = _run(
        [sys.executable, str(helper)], cwd=direct_repo,
        input_text="src/app.py\npackage.json\n",
    )
    assert result.returncode == 0, result.stderr
    assert "Cascade Checklist" in result.stdout
    assert "Config Changes" in result.stdout


def test_direct_installed_readiness_is_complete_and_runnable(direct_repo: Path) -> None:
    result = _run(
        [sys.executable, str(direct_repo / "scripts" / "readiness.py"),
         "run", "--repo", str(direct_repo), "--quiet"],
        cwd=direct_repo,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    assert result.returncode in {0, 1, 2}, result.stdout + result.stderr
    readiness_path = direct_repo / "status" / "readiness.json"
    assert readiness_path.is_file()
    readiness = json.loads(readiness_path.read_text())
    assert readiness.get("schema_version")
    assert readiness.get("sot_files")
    assert readiness.get("stages")
    assert all(block.get("entry_count") == 0 for block in readiness["sot_files"].values())


def test_plugin_payload_is_complete_and_runnable(plugin_repo: Path) -> None:
    templates = PLUGIN_ROOT / "templates"
    assert (templates / "PRD_template.md").is_file()
    assert (templates / "SoT_template").is_dir()
    assert not (templates / "PRD.md").exists()
    assert not (templates / "SoT").exists()
    assert (PLUGIN_ROOT / "scripts" / "_readiness" / "common.py").is_file()
    assert (PLUGIN_ROOT / "scripts" / "requirements.txt").is_file()
    assert "pyyaml" in (PLUGIN_ROOT / "scripts" / "requirements.txt").read_text().lower()
    assert (PLUGIN_ROOT / "hooks" / "metrics_drift_check.py").is_file()
    assert (PLUGIN_ROOT / "hooks" / "HOOK_CONTRACT.md").is_file()
    assert (PLUGIN_ROOT / "rules" / "08-skill-execution-modes.md").is_file()
    assert not (PLUGIN_ROOT / "skills" / "ghm-self-install").exists()
    assert not (PLUGIN_ROOT / "skills" / "ghm-template-sync").exists()
    assert not (PLUGIN_ROOT / "skills" / "SKILL_TEMPLATE").exists()
    assert not (PLUGIN_ROOT / "skills" / "README.md").exists()
    assert not (PLUGIN_ROOT / "skills" / "skills-inventory.md").exists()
    assert (templates / ".claude" / "install-manifest.yaml").read_bytes() == MANIFEST.read_bytes()
    assert {p.name for p in (templates / "docs").iterdir()} == ALLOWED_DOCS | DOC_SEED_SOURCES
    assert set(_parse_section("plugin_review_alias")) == {
        "docs/DEVELOPMENT_GRAPH.md",
        "docs/READINESS_PROTOCOL.md",
        ".claude/domain-profile.yaml",
    }
    for name in ALLOWED_DOCS:
        seed_name = name.replace(".md", ".seed.md")
        assert (templates / "docs" / name).read_bytes() == (
            templates / "docs" / seed_name
        ).read_bytes()
    assert (templates / ".claude" / "domain-profile.yaml").read_bytes() == (
        templates / ".claude" / "domain-profile.seed.yaml"
    ).read_bytes()

    expected_scripts: set[Path] = set()
    for entry in _parse_section("framework"):
        if not entry.startswith("scripts/"):
            continue
        source = REPO_ROOT / entry
        if source.is_file():
            expected_scripts.add(source.relative_to(REPO_ROOT / "scripts"))
        elif source.is_dir():
            expected_scripts.update(
                path.relative_to(REPO_ROOT / "scripts")
                for path in source.rglob("*") if path.is_file()
            )
    actual_scripts = {
        path.relative_to(PLUGIN_ROOT / "scripts")
        for path in (PLUGIN_ROOT / "scripts").rglob("*") if path.is_file()
    }
    assert actual_scripts == expected_scripts
    assert "epic-01-readiness-inputs" not in (
        REPO_ROOT / "scripts" / "readiness.py"
    ).read_text()
    assert "epic-01-readiness-inputs" not in (
        PLUGIN_ROOT / "scripts" / "readiness.py"
    ).read_text()

    result = _run(
        [sys.executable, str(PLUGIN_ROOT / "scripts" / "readiness.py"),
         "run", "--repo", str(plugin_repo), "--quiet"],
        cwd=plugin_repo,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    assert result.returncode in {0, 1, 2}, result.stdout + result.stderr
    readiness_path = plugin_repo / "status" / "readiness.json"
    assert readiness_path.is_file()
    readiness = json.loads(readiness_path.read_text())
    assert readiness.get("schema_version")
    assert readiness.get("sot_files")
    assert readiness.get("stages")
    assert all(block.get("entry_count") == 0 for block in readiness["sot_files"].values())
    assert all(
        any(cap.get("rule") == "placeholder_file" for cap in block.get("caps", []))
        for block in readiness["sot_files"].values()
    )
    stage = next(iter(readiness["stages"].values()))
    required = stage["dimensions"]["required_ids_present"]
    assert required.get("score") == 0.0
    assert any("Found 0 CFD- entries" in item["reason"] for item in stage["unmet_criteria"])

    profile = plugin_repo / ".claude" / "domain-profile.yaml"
    profile.write_text(profile.read_text().replace(
        "id_prefixes:\n", "id_prefixes:\n  ZZZ: { file: \"SoT/SoT.TESTING.md\", description: \"test\" }\n", 1
    ))
    env = os.environ.copy()
    env["CLAUDE_PROJECT_DIR"] = str(plugin_repo)
    pattern = _run(
        ["bash", str(PLUGIN_ROOT / "scripts" / "generate-id-pattern.sh")],
        cwd=plugin_repo,
        env=env,
    )
    assert pattern.returncode == 0, pattern.stderr
    assert "ZZZ" in pattern.stdout, "packaged script ignored the consumer domain profile"


def test_plugin_generated_runtime_dependencies_are_closed() -> None:
    hooks = json.loads((PLUGIN_ROOT / "hooks" / "hooks.json").read_text())
    commands = [
        hook["command"]
        for groups in hooks["hooks"].values()
        for group in groups
        for hook in group.get("hooks", [])
        if "command" in hook
    ]
    assert all(".claude/hooks/" not in command for command in commands)
    assert all("${CLAUDE_PLUGIN_ROOT}" in command for command in commands)
    referenced_hooks = {
        match.group(1)
        for command in commands
        for match in re.finditer(r"\$\{CLAUDE_PLUGIN_ROOT\}\"?/hooks/([^\"\s]+)", command)
    }
    assert referenced_hooks
    assert not {name for name in referenced_hooks if not (PLUGIN_ROOT / "hooks" / name).is_file()}

    save_hook = (PLUGIN_ROOT / "hooks" / "subagent-memory-save.sh").read_text()
    assert "metrics_drift_check.py" in save_hook
    assert (PLUGIN_ROOT / "hooks" / "metrics_drift_check.py").is_file()

    canonical_rules = sorted((REPO_ROOT / ".claude" / "rules").glob("*.md"))
    packaged_rules = sorted((PLUGIN_ROOT / "rules").glob("*.md"))
    assert [p.name for p in packaged_rules] == [p.name for p in canonical_rules]
    for canonical in canonical_rules:
        expected = canonical.read_text().replace("(../../docs/", "(../templates/docs/")
        assert (PLUGIN_ROOT / "rules" / canonical.name).read_text() == expected


def test_packager_refuses_preexisting_custom_output(tmp_path: Path) -> None:
    output = tmp_path / "existing-output"
    sentinel = output / "skills" / "consumer-owned.txt"
    sentinel.parent.mkdir(parents=True)
    sentinel.write_text("preserve me\n")

    result = _run([
        "bash", str(REPO_ROOT / "scripts" / "package-plugin.sh"),
        "--output", str(output),
    ])
    assert result.returncode != 0
    assert "custom output must not already exist" in result.stdout
    assert sentinel.read_text() == "preserve me\n"


def test_packager_refuses_symlink_default_output_without_touching_outside_sentinel(
    tmp_path: Path,
) -> None:
    source = tmp_path / "source"
    outside = tmp_path / "outside-plugin"
    (source / "scripts").mkdir(parents=True)
    (source / ".claude").mkdir()
    (source / "plugins").mkdir()
    (outside / ".claude-plugin").mkdir(parents=True)
    (outside / ".claude-plugin" / "plugin.json").write_text("{}\n")
    sentinel = outside / "skills" / "consumer-owned.txt"
    sentinel.parent.mkdir()
    sentinel.write_text("outside plugin sentinel\n")
    shutil.copy2(REPO_ROOT / "scripts" / "package-plugin.sh", source / "scripts")
    (source / "plugins" / "prd-ce").symlink_to(outside, target_is_directory=True)

    result = _run(["bash", str(source / "scripts" / "package-plugin.sh")], cwd=source)

    assert result.returncode != 0
    assert "refusing symlink in default plugin output path" in (result.stdout + result.stderr)
    assert sentinel.read_text() == "outside plugin sentinel\n"
    assert not (outside / "hooks").exists()
    assert not (outside / "scripts").exists()


def test_packager_supports_new_isolated_output(tmp_path: Path) -> None:
    output = tmp_path / "generated-plugin"
    result = _run([
        "bash", str(REPO_ROOT / "scripts" / "package-plugin.sh"),
        "--output", str(output),
    ])
    assert result.returncode == 0, result.stdout + result.stderr
    assert (output / "hooks" / "hooks.json").is_file()
    assert (output / "scripts" / "readiness.py").is_file()
    assert (output / "scripts" / "prd-ce-init.sh").is_file()
    assert (output / "templates" / "PRD_template.md").is_file()
    assert {p.name for p in (output / "templates" / "docs").iterdir()} == (
        ALLOWED_DOCS | DOC_SEED_SOURCES
    )
    for name in ALLOWED_DOCS:
        seed_name = name.replace(".md", ".seed.md")
        assert (output / "templates" / "docs" / name).read_bytes() == (
            output / "templates" / "docs" / seed_name
        ).read_bytes()
    assert (output / "templates" / ".claude" / "domain-profile.yaml").read_bytes() == (
        output / "templates" / ".claude" / "domain-profile.seed.yaml"
    ).read_bytes()
    review_docs = sorted((output / "templates" / "docs" / name) for name in ALLOWED_DOCS)
    assert not (
        broken := _broken_local_links(output / "templates", review_docs)
    ), "\n".join(broken)


def test_generated_plugin_payload_is_in_sync() -> None:
    result = _run(["bash", str(REPO_ROOT / "scripts" / "check-plugin-sync.sh")])
    assert result.returncode == 0, result.stdout + result.stderr


MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def _broken_local_links(root: Path, paths: list[Path]) -> list[str]:
    broken: list[str] = []
    for markdown in paths:
        for raw_target in MARKDOWN_LINK_RE.findall(markdown.read_text(errors="replace")):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target or any(marker in target for marker in ("{", "}", "*", "$")):
                continue
            candidate = (markdown.parent / target).resolve()
            if not candidate.exists():
                broken.append(f"{markdown.relative_to(root)} -> {raw_target}")
    return broken


@pytest.mark.parametrize("fixture_name", ["direct_repo", "plugin_repo"])
def test_installed_markdown_links_resolve(
    request: pytest.FixtureRequest, fixture_name: str,
) -> None:
    repo = request.getfixturevalue(fixture_name)
    paths = sorted(repo.rglob("*.md"))
    assert not (broken := _broken_local_links(repo, paths)), "\n".join(broken)


def test_plugin_live_markdown_links_resolve() -> None:
    paths = sorted(
        path
        for surface in ("skills", "rules", "agents", "hooks")
        for path in (PLUGIN_ROOT / surface).rglob("*.md")
    )
    assert not (broken := _broken_local_links(PLUGIN_ROOT, paths)), "\n".join(broken)


def _iter_reusable_source_files() -> list[Path]:
    roots: set[Path] = set()
    for entry in _parse_section("framework") + [src for src, _ in _seed_mapping()]:
        roots.add(REPO_ROOT / entry)
    files: list[Path] = []
    excluded = _parse_section("direct_exclude")

    def is_excluded(path: Path) -> bool:
        rel = str(path.relative_to(REPO_ROOT))
        return any(rel == item or rel.startswith(item.rstrip("/") + "/") for item in excluded)

    for root in sorted(roots):
        if root.is_file():
            if not is_excluded(root):
                files.append(root)
        elif root.is_dir():
            files.extend(
                p for p in root.rglob("*")
                if p.is_file() and "__pycache__" not in p.parts and not is_excluded(p)
            )
    return files


def _iter_source_run_public_interface_files() -> list[Path]:
    roots = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "BLUEPRINT.md",
        REPO_ROOT / "install.sh",
        REPO_ROOT / ".claude" / "install-manifest.yaml",
        REPO_ROOT / ".claude" / "skills" / "ghm-self-install",
        REPO_ROOT / ".claude-plugin" / "marketplace.json",
    ]
    files: list[Path] = []
    for root in roots:
        if root.is_file():
            files.append(root)
        elif root.is_dir():
            files.extend(path for path in root.rglob("*") if path.is_file())
    return sorted(files)


def _sensitive_hits(
    root: Path,
    paths: list[Path],
    *,
    forbidden_text: set[str] = FORBIDDEN_TEXT,
) -> list[str]:
    hits: list[str] = []

    def scan_value(relative: str, surface: str, value: str) -> None:
        folded = value.casefold()
        for marker in forbidden_text:
            if marker.casefold() in folded:
                hits.append(f"{relative} ({surface}): {marker}")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(value):
                hits.append(f"{relative} ({surface}): {label}")
        words = re.findall(r"[a-z0-9]+", folded)
        for width in (1, 2, 3):
            for index in range(len(words) - width + 1):
                candidate = " ".join(words[index:index + width])
                digest = hashlib.sha256(candidate.encode()).hexdigest()
                if digest in PRIVATE_MARKER_FINGERPRINTS:
                    hits.append(
                        f"{relative} ({surface}): private marker fingerprint {digest[:12]}"
                    )
                    return

    for path in paths:
        relative = path.relative_to(root).as_posix()
        scan_value(relative, "path", relative)
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        scan_value(relative, "content", text)
    return hits


def test_reusable_sources_and_generated_package_have_no_sensitive_references() -> None:
    source_files = _iter_reusable_source_files()
    assert not (hits := _sensitive_hits(REPO_ROOT, source_files)), "\n".join(hits)

    plugin_files = [p for p in PLUGIN_ROOT.rglob("*") if p.is_file()]
    assert not (hits := _sensitive_hits(PLUGIN_ROOT, plugin_files)), "\n".join(hits)


def test_source_run_public_interfaces_have_no_private_or_machine_specific_references() -> None:
    files = _iter_source_run_public_interface_files()
    assert files
    assert not (
        hits := _sensitive_hits(
            REPO_ROOT,
            files,
            forbidden_text=SOURCE_INTERFACE_FORBIDDEN_TEXT,
        )
    ), "\n".join(hits)


@pytest.mark.parametrize("fixture_name", ["direct_repo", "plugin_repo"])
def test_clean_output_has_no_sensitive_references(
    request: pytest.FixtureRequest, fixture_name: str,
) -> None:
    repo = request.getfixturevalue(fixture_name)
    files = [p for p in repo.rglob("*") if p.is_file()]
    assert not (hits := _sensitive_hits(repo, files)), "\n".join(hits)


def test_authority_ids_are_registered_and_html_companions_match() -> None:
    prd = (REPO_ROOT / "PRD.md").read_text()
    business = (REPO_ROOT / "SoT" / "SoT.BUSINESS_RULES.md").read_text()
    technical = (REPO_ROOT / "SoT" / "SoT.TECHNICAL_DECISIONS.md").read_text()
    business_html = (REPO_ROOT / "SoT" / "html" / "SoT.BUSINESS_RULES.html").read_text()
    technical_html = (REPO_ROOT / "SoT" / "html" / "SoT.TECHNICAL_DECISIONS.html").read_text()

    definitions = set(re.findall(r"^## (?:BR|ARC)-\d{3}\b", business + "\n" + technical, re.M))
    definition_ids = {re.search(r"(BR|ARC)-\d{3}", line).group(0) for line in definitions}
    assert definition_ids == AUTHORITY_IDS
    for authority_id in AUTHORITY_IDS:
        assert authority_id in prd
        html = business_html if authority_id.startswith("BR-") else technical_html
        assert f'id="{authority_id}"' in html
        assert re.search(rf'<a class="id" href="[^"]*{authority_id}">{authority_id}</a>', html)

    for source, predicate, target in (
        (business, "depends-on →", "BR-005"),
        (business, "depends-on →", "BR-003"),
        (technical, "depends-on →", "ARC-001"),
        (technical, "depends-on →", "ARC-002"),
        (technical, "driven-by →", "BR-002"),
    ):
        assert predicate in source and target in source

    generic = (REPO_ROOT / "PRD_template.md").read_text()
    generic += "\n" + "\n".join(
        p.read_text(errors="replace") for p in (REPO_ROOT / "SoT_template").rglob("*") if p.is_file()
    )
    assert "Product Management Is the Sole V2 Lifecycle" not in generic
    assert "Repository Authority and Downstream Seeds Are Separate" not in generic
