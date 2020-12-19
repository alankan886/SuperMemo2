import json
from datetime import date, timedelta

import pytest

from supermemo2 import SMTwo


# test default convert on first visit
def test_first_visit_invalid_easiness_interval_repetitions():
    with pytest.warns(UserWarning) as record:
        sm_two = SMTwo(3, True, 999, 666, 777)

    assert len(record) == 3
    assert str(record[0].message) == "easiness automatically set to 2.5, easiness should be 2.5 for the first visit"
    assert str(record[1].message) == "interval automatically set to 1, interval should be 1 for the first visit"
    assert str(record[2].message) == "repetitions automatically set to 1, repetitions should be 1 for the first visit"
    assert sm_two.prev.easiness == 2.5
    assert sm_two.prev.interval == 1
    assert sm_two.prev.repetitions == 1


# test repetitions = 1 and 2, then modify interval to wrong values
@pytest.mark.parametrize("first_visit, expected_interval, repetitions, updated_prev_interval", [(True, 1, 1, 66), (False, 1, 2, 99)])
def test_update_invalid_prev_interval(first_visit, expected_interval, repetitions, updated_prev_interval):
    sm_two = SMTwo(3, first_visit, 2.5, expected_interval, repetitions)
    with pytest.warns(UserWarning) as record:
        sm_two.prev.interval = updated_prev_interval

    assert len(record) == 1
    assert str(record[0].message) == f"interval automatically set to {expected_interval}, when repetition is {repetitions}, interval is always {expected_interval}"
    print(sm_two.prev.interval)
    # assert sm_two.prev.interval == expected_interval


# test q < 3 update prev attrs, might have to rewrite test case
@pytest.mark.parametrize(
    "quality, first_visit, easiness, interval, repetitions, updated_prev_easiness, updated_prev_interval, updated_prev_repetitions",
    [
        (0, True, 2.5, 1, 1, 3.1, 2, 666),
        (1, False, 2.5, 1, 2, 2.1, 999, 4),
        (2, False, 2.5, 999, 24, 3.6, 4, 10)
    ]
)
def test_update_prev_q_less_than_three(quality, first_visit, easiness, interval, repetitions, updated_prev_easiness, updated_prev_interval, updated_prev_repetitions):
    sm_two = SMTwo(quality, first_visit, easiness, interval, repetitions)
    sm_two.prev.easiness = updated_prev_easiness
    sm_two.prev.interval = updated_prev_interval
    sm_two.prev.repetitions = updated_prev_repetitions
    
    assert sm_two.prev.easiness == updated_prev_easiness
    assert sm_two.prev.repetitions == updated_prev_repetitions
    assert sm_two.prev.interval == updated_prev_interval
    assert sm_two.repetitions == 1
    assert sm_two.interval == 1
    assert sm_two.easiness == updated_prev_easiness
    assert sm_two.next_review == date.today() + timedelta(days=1)


# test q >= 3 update attrs repetitions or maybe all attrs (prob need to add a lot more params)?
# note, once rep > 2, interval can be anything larger than 7 (I believe the lowest it can go would be 8) TODO: set lower bound of 8 for interval or at least not lower than 6
# (0, True, 2.5, 1, 1, 2, 1, 1), this should cause warning for auto-reset cuz trying to set rep to 2 when it's first visit
# I don't think I need to test when q < 3, because when q < 3 rep must be 1, and any changes on rep will be warned then auto set to 1
@pytest.mark.parametrize(
    "first_visit, easiness, interval, repetitions, updated_prev_repetitions, expected_prev_interval, expected_interval",
    [   
        (True, 2.5, 1, 1, 1, 1, 1),
        (False, 2.5, 6, 2, 1, 1, 6),
        (False, 2.5, 19, 3, 2, 6, 48),
        (False, 2.5, 19, 3, 4, 19, 48)
    ]
)
def test_update_prev_repetitions_q_larger_equal_three(first_visit, easiness, interval, repetitions, updated_prev_repetitions, expected_prev_interval, expected_interval):
    """
        After modifying the previous values, it should change the new values for some cases
    """
    sm_two = SMTwo(3, first_visit, easiness, interval, repetitions)
    sm_two.prev.repetitions = updated_prev_repetitions
    assert sm_two.prev.json() == json.dumps({"easiness": easiness, "interval": expected_prev_interval, "repetitions": updated_prev_repetitions})
    assert sm_two.interval == expected_interval
    assert sm_two.repetitions == updated_prev_repetitions + 1
    assert sm_two.next_review == date.today() + timedelta(days=expected_interval)

# test q >= 3 update attrs interval, this does affect next_review
# not going to test when rep=1 and rep=2, because those have pre-defined intervals
# @pytest.mark.parametrize(
#     "first_visit, easiness, interval, repetitions, updated_prev_interval, expected_interval",
#     [
#         (False, 2.5, 1, 1, 1, )
#     ]
# )
# def test_update_prev_attrs_interval(first_visit, easiness, interval, repetitions, updated_prev_interval, expected_interval):
#     sm_two = SMTwo(3, )

# test q >= 3 update attrs second visit
@pytest.mark.skip
def test_update_prev_attrs_second_visit():
    sm_two = SMTwo(quality=3, first_visit=False)

    # update repetitions to 2 should change interval to 6
    sm_two.prev.repetitions = 2
    assert sm_two.prev.json() == '{"easiness": 2.36, "interval": 1, "repetitions": 2}'
    assert sm_two.interval == 6

# test q >= 3 update attrs nth visit

# test q < 3 update attrs first visit

# test q < 3 update attrs second visit

# test q < 3 update attrs nth visit

# test prev

# @pytest.mark.parametrize("first_visit, new_rep, new_inter", [(True, 1, 1), (False, 2, 6), (False, 3, 14)])
# def test_repeititons_setter(monkeypatch, first_visit, new_rep, new_inter):
#     sm_two = SMTwo(3, first_visit)
#     monkeypatch.setattr(sm_two, "interval", new_inter)
#     prev = Prev(sm_two, 3.0, 14, 4)
#     prev.repetitions = new_rep

#     assert sm_two.interval == new_inter
