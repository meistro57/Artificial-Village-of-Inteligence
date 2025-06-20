from .base import Agent


class ThinkerAgent(Agent):
    def perform_task(self, task: str):
        result = f"Thinker {self.name} contemplated '{task}'"
        self.remember(task, result)
        return result
