import os
from memory.storage import Memory


def test_store_and_get(tmp_path):
    db_path = tmp_path / "test.db"
    memory = Memory(db_path)
    memory.store("foo", "bar")
    assert memory.get("foo") == "bar"
    memory.close()
    os.remove(db_path)
