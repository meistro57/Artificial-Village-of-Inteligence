import importlib
import pkgutil
from types import ModuleType
from typing import List
from pathlib import Path


def load_plugins(package: str) -> List[ModuleType]:
    """Dynamically import all modules in a plugin package."""
    modules = []
    pkg = importlib.import_module(package)
    for info in pkgutil.iter_modules(pkg.__path__):
        full_name = f"{package}.{info.name}"
        modules.append(importlib.import_module(full_name))
    return modules
