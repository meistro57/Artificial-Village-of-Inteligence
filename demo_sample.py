import argparse

from agents.builder import BuilderAgent
from agents.thinker import ThinkerAgent
from agents.artist import ArtistAgent
from agents.guardian import GuardianAgent
from agents.trainer import TrainerAgent
from knowledge_base.local_kb import KnowledgeBase
from memory.storage import Memory
from mission_system.mission import Mission


def main():
    """Run a very small demo mission."""
    parser = argparse.ArgumentParser(description="Run a sample mission")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="enable verbose output",
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

    for agent in agents:
        agent.verbose = args.verbose

    mission = Mission(["sample task"])

    while not mission.is_finished():
        for agent in agents:
            agent.act(mission)
            print(mission.progress_summary())
            if mission.is_finished():
                break

    print("Sample mission completed:")
    for task, result in mission.completed:
        print(f"- {task}: {result}")

    memory.close()


if __name__ == "__main__":
    main()
