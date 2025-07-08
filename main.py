import argparse

from agents.base import Agent
from agents.builder import BuilderAgent
from agents.thinker import ThinkerAgent
from agents.artist import ArtistAgent
from agents.guardian import GuardianAgent
from agents.trainer import TrainerAgent
from plugins.loader import load_plugins
from knowledge_base.local_kb import KnowledgeBase
from memory.storage import Memory
from mission_system.mission import Mission


def main():
    parser = argparse.ArgumentParser(description="Run a short mission")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="enable verbose output",
    )
    parser.add_argument(
        "--plugin-package",
        default=None,
        help="optional plugin package to load agents from",
    )
    args = parser.parse_args()

    memory = Memory()
    kb = KnowledgeBase()
    agents = [
        BuilderAgent("Builder", memory),
        ThinkerAgent("Thinker", memory, model="llama3"),
        ArtistAgent("Artist", memory),
        GuardianAgent("Guardian", memory),
        TrainerAgent("Trainer", memory, kb),
    ]
    if args.plugin_package:
        for module in load_plugins(args.plugin_package):
            for attr in dir(module):
                cls = getattr(module, attr)
                if (
                    isinstance(cls, type)
                    and issubclass(cls, Agent)
                    and cls is not Agent
                ):
                    agents.append(cls(cls.__name__, memory))
    for agent in agents:
        agent.verbose = args.verbose

    mission = Mission([
        "design module",
        "analyze requirements",
        "create logo",
        "check security",
        "teach python",
    ])

    while not mission.is_finished():
        for agent in agents:
            agent.act(mission)
            if mission.is_finished():
                break

    print("Mission completed:")
    for task, result in mission.completed:
        print(f"- {task}: {result}")

    memory.close()


if __name__ == "__main__":
    main()
