import importlib
import pkgutil
from types import ModuleType
from typing import List


def load_plugins(package: str) -> List[ModuleType]:
    """Dynamically import all modules in a plugin package."""
    modules = []
    pkg = importlib.import_module(package)
    for info in pkgutil.iter_modules(pkg.__path__):
        full_name = f"{package}.{info.name}"
        modules.append(importlib.import_module(full_name))
    return modules


def discover_plugins(package: str) -> List[str]:
    """Return a list of available plugin module names without importing them."""
    pkg = importlib.import_module(package)
    return [f"{package}.{info.name}" for info in pkgutil.iter_modules(pkg.__path__)]
