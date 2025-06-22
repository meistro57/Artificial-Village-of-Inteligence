from mission_system.mission import Mission


def test_progress_summary():
    mission = Mission(["task1", "task2"])
    assert mission.progress_summary() == "0/2 tasks completed"
    mission.next_task()
    mission.complete_task("task1", "done")
    assert mission.progress_summary() == "1/2 tasks completed"
