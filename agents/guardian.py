from .base import Agent


class GuardianAgent(Agent):
    def perform_task(self, task: str):
        result = f"Guardian {self.name} secured '{task}'"
        self.remember(task, result)
        return result
