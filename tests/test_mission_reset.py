from mission_system.mission import Mission


def test_reset_mission():
    mission = Mission(["a", "b"])
    mission.next_task()
    mission.complete_task("a", "done")
    mission.reset()
    assert mission.completed == []
    assert mission.get_remaining_tasks() == ["a", "b"]
