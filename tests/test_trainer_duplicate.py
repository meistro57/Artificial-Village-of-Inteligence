from agents.trainer import TrainerAgent
from knowledge_base.local_kb import KnowledgeBase
from memory.storage import Memory


def test_trainer_handles_duplicate(tmp_path):
    db_path = tmp_path / "test.db"
    memory = Memory(db_path)
    kb = KnowledgeBase()
    agent = TrainerAgent("Teach", memory, kb)

    first = agent.perform_task("math")
    second = agent.perform_task("math")

    assert first == "Trainer Teach taught 'math'"
    assert second == "Trainer Teach already knew 'math'"
    memory.close()
