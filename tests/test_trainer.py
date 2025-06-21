from agents.trainer import TrainerAgent
from knowledge_base.local_kb import KnowledgeBase
from memory.storage import Memory


def test_trainer_adds_fact(tmp_path):
    db_path = tmp_path / "test.db"
    memory = Memory(db_path)
    kb = KnowledgeBase()
    agent = TrainerAgent("Teacher", memory, kb)

    result = agent.perform_task("math basics")

    assert result == "Trainer Teacher taught 'math basics'"
    assert kb.query("math basics") == "taught by Teacher"

    memory.close()
