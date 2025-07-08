from .base import Agent


class GuardianAgent(Agent):
    banned_keywords = {"harm", "malware", "attack"}

    def perform_task(self, task: str):
        if any(bad in task.lower() for bad in self.banned_keywords):
            result = f"Guardian {self.name} blocked unsafe task"
        else:
            result = f"Guardian {self.name} secured '{task}'"
        self.remember(task, result)
        return result
