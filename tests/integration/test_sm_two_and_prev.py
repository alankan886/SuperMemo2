from supermemo2 import SMTwo


def test_update_prev_attrs():
    """
        After modifying the previous values, it should change the new values for some cases
    """
    sm_two = SMTwo(quality=2, first_visit=True)
    assert sm_two.easiness == 2.5
    assert sm_two.interval == 1
    assert sm_two.repetitions == 1

    # update repetitions to 1 should change interval to 1
    sm_two.prev.repetitions = 1
    assert sm_two.prev.json() == {"easiness": 2.5, "interval": 0, "repetitions": 1}
    assert sm_two.interval == 1

    # update repetitions to 2 should change interval to 6
    sm_two.prev.repetitions = 2
    assert sm_two.prev.json() == {"easiness": 2.5, "interval": 0, "repetitions": 2}
    assert sm_two.interval == 6
