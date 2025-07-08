from __future__ import annotations

import uuid
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from memory.storage import Memory
    from mission_system.mission import Mission


from colorama import Fore, Style, init


class Agent:
    """Base class for all agents."""
    def __init__(self, name: str, memory: 'Memory'):
        self.name = name
        self.id = str(uuid.uuid4())
        self.memory = memory
        self.verbose = False

    def set_verbose(self, verbose: bool) -> None:
        """Enable or disable verbose debug output."""
        self.verbose = verbose

    def describe(self) -> str:
        """Return a short description of the agent."""
        return f"{self.name} ({self.id})"

    def _debug(self, message: str) -> None:
        if self.verbose:
            init(autoreset=True)
            print(f"{Fore.CYAN}{message}{Style.RESET_ALL}")

    def remember(self, key: str, value: Any) -> None:
        self.memory.store(f"{self.id}:{key}", value)

    def recall(self, key: str) -> Any:
        return self.memory.get(f"{self.id}:{key}")

    def get_memory_keys(self) -> list[str]:
        """Return all memory keys stored for this agent."""
        prefix = f"{self.id}:"
        return [k[len(prefix):] for k in self.memory.keys() if k.startswith(prefix)]

    def act(self, mission: 'Mission') -> None:
        """Perform a single step for the mission."""
        task = mission.next_task()
        if task is None:
            return
        self._debug(f"{self.name} starting '{task}'")
        result = self.perform_task(task)
        mission.complete_task(task, result)
        self._debug(f"{self.name} finished '{task}'")

    def perform_task(self, task: str) -> Any:
        """Override in subclasses with actual behavior."""
        raise NotImplementedError
