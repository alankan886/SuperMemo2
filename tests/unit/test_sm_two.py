from datetime import date, timedelta

import pytest

from supermemo2 import SMTwo


@pytest.mark.parametrize("quality_less_than_three", [0, 1, 2])
def test_default_first_visit_q_less_than_three(quality_less_than_three):
    sm_two = SMTwo(quality=quality_less_than_three, first_visit=True)
    assert sm_two.quality == quality_less_than_three
    assert sm_two.easiness == 2.5
    assert sm_two.interval == 1
    assert sm_two.repetitions == 1
    assert sm_two.last_review == date.today()
    assert sm_two.next_review == date.today() + timedelta(days=1)


# @pytest.mark.parametrize("quality", [0, 1, 2, 3, 4, 5])
# def test_prev(quality):
#     sm_two = SMTwo(quality=quality, first_visit=True)
#     prev = sm_two.prev
#     prev_json = prev.json()
#     assert prev.prev_easiness == 2.5
#     assert prev.prev_interval == 0
#     assert prev.prev_repetitions == 1
#     assert prev_json == {"prev_easiness": 2.5, "prev_interval": 0, "prev_repetitions": 1}


# def test_first_visit_q_less_than_three_bad_values():
#     """
#         Test the reset mechanism when easiness, interval and repetitions values are invalid for first visit
#     """
#     sm_two = SMTwo(quality=2, first_visit=True, easiness=-1.5, interval=-100, repetitions=-12)
#     assert sm_two.quality == 2
#     assert sm_two.easiness == 2.5
#     assert sm_two.interval == 1
#     assert sm_two.repetitions == 1
#     assert sm_two.last_review == date.today()
#     assert sm_two.next_review == date.today() + timedelta(days=1)
