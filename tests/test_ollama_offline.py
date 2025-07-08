from llm.ollama_client import is_ollama_available


def test_is_ollama_available_returns_bool():
    assert isinstance(is_ollama_available(), bool)
