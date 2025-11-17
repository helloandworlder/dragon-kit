from pathlib import Path

import pytest

from dragon_cli.__init__ import (
    apply_document_overrides,
    resolve_document_override_source,
)


def prepare_repo_file(repo_root: Path, name: str, content: str = "repo") -> Path:
    repo_root.mkdir(parents=True, exist_ok=True)
    target = repo_root / name
    target.write_text(content, encoding="utf-8")
    return target


def prepare_home_file(home_root: Path, name: str, content: str = "home") -> Path:
    spec_dir = home_root / ".specify"
    spec_dir.mkdir(parents=True, exist_ok=True)
    target = spec_dir / name
    target.write_text(content, encoding="utf-8")
    return target


@pytest.mark.parametrize("doc_name", ["AGENTS.md", "CLAUDE.md"])
def test_resolve_document_override_prefers_home(tmp_path: Path, doc_name: str):
    repo_root = tmp_path / "repo"
    prepare_repo_file(repo_root, doc_name, "repo-version")
    home_root = tmp_path / "home"
    preferred = prepare_home_file(home_root, doc_name, "home-version")

    source = resolve_document_override_source(doc_name, repo_root=repo_root, home_root=home_root)

    assert source == preferred


def test_resolve_document_override_falls_back_to_repo(tmp_path: Path):
    repo_root = tmp_path / "repo"
    fallback = prepare_repo_file(repo_root, "AGENTS.md", "repo-version")

    source = resolve_document_override_source("AGENTS.md", repo_root=repo_root, home_root=tmp_path / "home")

    assert source == fallback


def test_apply_document_overrides_copies_selected_docs(tmp_path: Path):
    repo_root = tmp_path / "repo"
    prepare_repo_file(repo_root, "AGENTS.md", "repo-version")
    destination = tmp_path / "project"
    destination.mkdir()

    copied = apply_document_overrides(
        destination,
        {"AGENTS"},
        repo_root=repo_root,
        home_root=tmp_path / "home",
    )

    assert "AGENTS" in copied
    assert (destination / "AGENTS.md").read_text(encoding="utf-8") == "repo-version"
