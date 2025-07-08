from mission_system.mission import Mission


def test_get_remaining_tasks():
    mission = Mission(["a", "b"])
    assert mission.get_remaining_tasks() == ["a", "b"]
    mission.next_task()
    assert mission.get_remaining_tasks() == ["b"]
