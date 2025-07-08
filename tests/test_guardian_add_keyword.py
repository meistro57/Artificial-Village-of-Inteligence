from agents.guardian import GuardianAgent
from memory.storage import Memory


def test_add_banned_keyword(tmp_path):
    db_path = tmp_path / "test.db"
    memory = Memory(db_path)
    GuardianAgent.add_banned_keyword("virus")
    agent = GuardianAgent("G", memory)
    result = agent.perform_task("launch virus")
    assert result == "Guardian G blocked unsafe task"
    memory.close()
