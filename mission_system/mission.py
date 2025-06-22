from typing import List, Any, Optional


class Mission:
    def __init__(self, tasks: List[str]):
        self.tasks = tasks
        self.completed = []

    def next_task(self) -> Optional[str]:
        if not self.tasks:
            return None
        return self.tasks.pop(0)

    def complete_task(self, task: str, result: Any) -> None:
        self.completed.append((task, result))

    def is_finished(self) -> bool:
        return not self.tasks

    def progress_summary(self) -> str:
        """Return a human readable summary of mission progress."""
        total = len(self.completed) + len(self.tasks)
        completed = len(self.completed)
        return f"{completed}/{total} tasks completed"
