# Artificial-Village-of-Inteligence
# 🌐 Artificial Village of Intelligence

Welcome to the **Artificial Village of Intelligence** — a living, breathing digital ecosystem where intelligent agents collaborate, evolve, and co-create a new frontier of automation, knowledge, and digital consciousness.

## 🧠 What Is This?

Imagine a self-sustaining village, but instead of humans, it's populated by AI agents—each with unique roles, memories, and missions. This is not just software. This is a **distributed society of intelligence**, built to:

- Learn and adapt over time
- Share information via communal memory (database or LLM)
- Operate independently or in cooperative multi-agent chains
- Tackle complex tasks from coding to simulation, self-optimization, and exploration

## 🏗️ Project Vision

This is the foundation of a sandbox-style ecosystem for intelligent agents. We’re building:

- 🧱 Modular agent architecture (Builder, Thinker, Artist, Guardian, etc.)
- 🧬 Persistent memory using SQLite (with future support for MySQL or Redis)
- 📚 Local knowledge base + self-learning loop
- ⚙️ Event-driven behaviors, mission triggers, and growth protocols
- 🧩 Plugin-ready system to add roles, logic, and behavior profiles
- 🛡️ Guardian failsafe blocks unsafe tasks
- 🌐 Ollama usage falls back gracefully when offline

## 🚀 Goals

- **Self-evolving agent clusters**
- **Offline-first architecture** with future support for online sync
- **Mission system** for structured growth and experimentation
- **Failsafe guardian logic** to ensure ethical growth and avoid runaway behavior

## 🔧 Tech Stack (Initial Implementation)

- Python 3 (no external dependencies except `pytest` for tests)
- SQLite for persistent memory
- Simple plugin loader for extensibility
- [Ollama](https://ollama.com) for local LLM interaction (uses the `llama3` model by default)

## 🛠️ Ubuntu Installation

Run the provided `install.sh` script to set up a Python virtual environment and install dependencies. The script also executes the test suite to verify the installation.

```bash
bash install.sh
```

## ▶️ Running the Demo

1. Install dependencies (for testing):

   ```bash
   pip install -r requirements.txt
   ```

2. Run the demo script:

   ```bash
   python main.py
   ```

3. Run the extended demo (takes longer to complete):

   ```bash
   python long_demo.py
   ```

4. Try the sample demo with progress output:

   ```bash
   python demo_sample.py -v
   ```

5. Run continuously with evolving tasks:

   ```bash
   python auto_run.py -v
   ```

6. Load plugin agents using `--plugin-package`:

   ```bash
   python main.py --plugin-package plugins.agents
   ```

   This script runs missions in an endless loop, creating a new set of tasks on
   each iteration. Stop it with `Ctrl+C`.

### Ollama Support

The `ThinkerAgent` uses the [Ollama](https://ollama.com) service for language
generation. Make sure the Ollama server is running and that you have pulled a
model, for example:


```bash
ollama pull llama3
ollama serve &  # start the Ollama server in the background
```

By default the Thinker agent uses the model specified in the ``OLLAMA_MODEL``
environment variable (``llama3`` if unset). You can override it when launching
the application:

```bash
export OLLAMA_MODEL=mistral
python main.py
```

Without Ollama running, the Thinker agent will return an error message in place
of a response.

The demo spawns five agents—Builder, Thinker, Artist, Guardian, and Trainer—who work together on a simple mission. Results are printed to the console and stored in a local SQLite database (`memory/memory.db`). The Trainer agent also records learned facts in the in-memory knowledge base. The extended demo runs through 20 tasks with a short delay after each agent action to make the process take noticeably longer.

## 🧪 Running Tests

This project uses `pytest` for a minimal test suite:

```bash
pytest
```

---

> *This repo is in its primordial phase. Come back often, or contribute. The village is just beginning to awaken...*
