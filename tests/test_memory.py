import os
from memory.storage import Memory


def test_store_and_get(tmp_path):
    db_path = tmp_path / "test.db"
    memory = Memory(db_path)
    memory.store("foo", "bar")
    assert memory.get("foo") == "bar"
    memory.close()
    os.remove(db_path)


def test_delete_and_keys(tmp_path):
    db_path = tmp_path / "test.db"
    memory = Memory(db_path)
    memory.store("a", "1")
    memory.store("b", "2")
    assert set(memory.keys()) == {"a", "b"}
    memory.delete("a")
    assert memory.get("a") is None
    assert set(memory.keys()) == {"b"}
    memory.close()


def test_clear(tmp_path):
    db_path = tmp_path / "test.db"
    memory = Memory(db_path)
    memory.store("x", "1")
    memory.store("y", "2")
    memory.clear()
    assert memory.keys() == []
    memory.close()
