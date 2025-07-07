import ollama


def generate_response(prompt: str, model: str = "llama3") -> str:
    """Return the response from the Ollama model.

    Parameters
    ----------
    prompt : str
        The user prompt to send to the model.
    model : str, optional
        The model to use, by default "llama3".
    """
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        return response.get("message", {}).get("content", "").strip()
    except Exception as exc:
        return f"[ollama error: {exc}]"
