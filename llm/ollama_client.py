"""Thin wrapper around the Ollama Python client."""

import os
import ollama


def is_ollama_available() -> bool:
    """Return True if the Ollama server is reachable."""
    try:
        ollama.list_models()
        return True
    except Exception:
        return False

DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "llama3")


def generate_response(prompt: str, model: str | None = None) -> str:
    """Return the response from the Ollama model.

    Parameters
    ----------
    prompt : str
        The user prompt to send to the model.
    model : str, optional
        The model to use. If not provided, the ``OLLAMA_MODEL`` environment
        variable is used, falling back to ``llama3``.
    """
    if model is None:
        model = DEFAULT_MODEL
    if not is_ollama_available():
        return "[ollama offline]"
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        return response.get("message", {}).get("content", "").strip()
    except Exception as exc:
        return f"[ollama error: {exc}]"
