from dragon_cli.__init__ import AGENT_CONFIG


def test_droid_agent_registered_with_expected_defaults():
    assert "droid" in AGENT_CONFIG
    config = AGENT_CONFIG["droid"]
    assert config["folder"] == ".factory/commands/"
    assert config["requires_cli"] is True
    assert config["install_url"]
