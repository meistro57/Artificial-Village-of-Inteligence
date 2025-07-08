from agents.guardian import GuardianAgent
from memory.storage import Memory


def test_guardian_blocks(tmp_path):
    db_path = tmp_path / "test.db"
    memory = Memory(db_path)
    agent = GuardianAgent("Guard", memory)
    result_safe = agent.perform_task("secure data")
    result_bad = agent.perform_task("launch malware attack")
    assert result_safe == "Guardian Guard secured 'secure data'"
    assert result_bad == "Guardian Guard blocked unsafe task"
    memory.close()
