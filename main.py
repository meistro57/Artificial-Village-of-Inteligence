from agents.builder import BuilderAgent
from agents.thinker import ThinkerAgent
from agents.artist import ArtistAgent
from agents.guardian import GuardianAgent
from memory.storage import Memory
from mission_system.mission import Mission


def main():
    memory = Memory()
    agents = [
        BuilderAgent("Builder", memory),
        ThinkerAgent("Thinker", memory),
        ArtistAgent("Artist", memory),
        GuardianAgent("Guardian", memory),
    ]
    mission = Mission([
        "design module",
        "analyze requirements",
        "create logo",
        "check security",
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
