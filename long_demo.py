import time
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
    """Run a longer mission demo to showcase agent collaboration."""
    parser = argparse.ArgumentParser(
        description="Run an extended mission demo"
    )
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
        ThinkerAgent("Thinker", memory),
        ArtistAgent("Artist", memory),
        GuardianAgent("Guardian", memory),
        TrainerAgent("Trainer", memory, kb),
    ]

    # Larger set of tasks to make the demo run longer
    tasks = [
        f"task {i}" for i in range(1, 21)
    ]
    for agent in agents:
        agent.verbose = args.verbose
    mission = Mission(tasks)

    while not mission.is_finished():
        for agent in agents:
            agent.act(mission)
            time.sleep(0.1)
            if mission.is_finished():
                break

    print("Extended mission completed:")
    for task, result in mission.completed:
        print(f"- {task}: {result}")

    memory.close()


if __name__ == "__main__":
    main()
