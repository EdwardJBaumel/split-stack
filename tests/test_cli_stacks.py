import json

from local_llm_router.cli import main


def test_stacks_json_includes_complex_alt_for_16gb(capsys):
    exit_code = main(["stacks", "--profile", "workstation_16gb", "--json"])
    payload = json.loads(capsys.readouterr().out.strip())
    assert exit_code == 0
    assert payload["tiers"]["complex_alt"] == "qwen3:14b"
    assert payload["tier_slots"]["complex"] == "qwen3.6:35b-a3b"
    assert payload["tier_slots"]["complex_alt"] == "qwen3:14b"
