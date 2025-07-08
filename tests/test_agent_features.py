from agents.builder import BuilderAgent
from memory.storage import Memory


def test_set_verbose_and_describe(tmp_path):
    db_path = tmp_path / "test.db"
    memory = Memory(db_path)
    agent = BuilderAgent("B", memory)
    agent.set_verbose(True)
    assert agent.verbose is True
    desc = agent.describe()
    assert agent.name in desc and agent.id in desc
    memory.close()


def test_get_memory_keys(tmp_path):
    db_path = tmp_path / "test.db"
    memory = Memory(db_path)
    agent = BuilderAgent("B", memory)
    agent.perform_task("build")
    assert agent.get_memory_keys() == ["build"]
    memory.close()
