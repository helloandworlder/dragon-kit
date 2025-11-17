from dragon_cli.__init__ import AGENT_CONFIG, normalize_agent_keys


def test_droid_agent_registered_with_expected_defaults():
    assert "droid" in AGENT_CONFIG
    config = AGENT_CONFIG["droid"]
    assert config["folder"] == ".factory/commands/"
    assert config["requires_cli"] is True
    assert config["install_url"]


def test_normalize_agent_keys_preserves_order_and_deduplicates():
    normalized, invalid = normalize_agent_keys(["copilot", "claude", "copilot"])
    assert normalized == ["copilot", "claude"]
    assert invalid == []


def test_normalize_agent_keys_reports_invalid_entries():
    normalized, invalid = normalize_agent_keys(["unknown", "claude"])
    assert normalized == ["claude"]
    assert invalid == ["unknown"]
