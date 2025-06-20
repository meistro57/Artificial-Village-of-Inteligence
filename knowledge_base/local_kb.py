class KnowledgeBase:
    """Simple in-memory knowledge base."""
    def __init__(self):
        self.facts = {}

    def add_fact(self, key: str, value: str) -> None:
        self.facts[key] = value

    def query(self, key: str) -> str:
        return self.facts.get(key, "")
