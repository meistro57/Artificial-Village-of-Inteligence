from mission_system.mission import Mission


def test_mission_on_complete():
    events = []

    def callback(task, result):
        events.append((task, result))

    mission = Mission(["a"], on_complete=callback)
    mission.next_task()
    mission.complete_task("a", "done")

    assert events == [("a", "done")]
