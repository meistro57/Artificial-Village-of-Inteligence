import uuid
from typing import Any

class Agent:
    """Base class for all agents."""
    def __init__(self, name: str, memory: 'Memory'):
        self.name = name
        self.id = str(uuid.uuid4())
        self.memory = memory

    def remember(self, key: str, value: Any) -> None:
        self.memory.store(f"{self.id}:{key}", value)

    def recall(self, key: str) -> Any:
        return self.memory.get(f"{self.id}:{key}")

    def act(self, mission: 'Mission') -> None:
        """Perform a single step for the mission."""
        task = mission.next_task()
        if task is None:
            return
        result = self.perform_task(task)
        mission.complete_task(task, result)

    def perform_task(self, task: str) -> Any:
        """Override in subclasses with actual behavior."""
        raise NotImplementedError
