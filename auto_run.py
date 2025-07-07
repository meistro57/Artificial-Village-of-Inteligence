import argparse
import time

from agents.builder import BuilderAgent
from agents.thinker import ThinkerAgent
from agents.artist import ArtistAgent
from agents.guardian import GuardianAgent
from agents.trainer import TrainerAgent
from knowledge_base.local_kb import KnowledgeBase
from memory.storage import Memory
from mission_system.mission import Mission


def generate_tasks(iteration: int) -> list[str]:
    """Create a simple list of evolving tasks."""
    return [
        f"design module {iteration}",
        f"analyze requirements {iteration}",
        f"create logo {iteration}",
        f"check security {iteration}",
        f"teach python {iteration}",
    ]


def main(verbose: bool = False, sleep: float = 5.0) -> None:
    """Run missions in an endless loop, evolving tasks each iteration."""
    memory = Memory()
    kb = KnowledgeBase()
    agents = [
        BuilderAgent("Builder", memory),
        ThinkerAgent("Thinker", memory),
        ArtistAgent("Artist", memory),
        GuardianAgent("Guardian", memory),
        TrainerAgent("Trainer", memory, kb),
    ]
    for agent in agents:
        agent.verbose = verbose

    iteration = 0
    try:
        while True:
            mission = Mission(generate_tasks(iteration))
            while not mission.is_finished():
                for agent in agents:
                    agent.act(mission)
                    if mission.is_finished():
                        break
            print(f"Iteration {iteration} completed")
            iteration += 1
            time.sleep(sleep)
    except KeyboardInterrupt:
        print("Stopping auto run")
    finally:
        memory.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the agents continuously")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="enable verbose output",
    )
    parser.add_argument(
        "-s",
        "--sleep",
        type=float,
        default=5.0,
        help="seconds to sleep between iterations",
    )
    args = parser.parse_args()
    main(verbose=args.verbose, sleep=args.sleep)
