import json
from datetime import date, datetime, timedelta

import pytest

from supermemo2 import SMTwo
from supermemo2.exceptions import DateFormatError


@pytest.mark.parametrize("bad_quality, error", [(False, TypeError), (6, ValueError), (-1, ValueError)])
def test_quality_invalid_value(bad_quality, error):
    with pytest.raises(error) as excinfo:
        SMTwo(bad_quality, True)

    if error == TypeError:
        assert str(excinfo.value) == f"{bad_quality} is not an integer"
    elif error == ValueError:
        assert str(excinfo.value) == f"{bad_quality} is not an integer between the range of 0 to 5"


@pytest.mark.parametrize("bad_first_visit", ["abc", 123, 0.01])
def test_first_visit_invalid_value(bad_first_visit):
    with pytest.raises(TypeError) as excinfo:
        SMTwo(3, bad_first_visit)

    assert str(excinfo.value) == f"first_visit value, '{bad_first_visit}', is not a valid boolean value"


def test_last_review_convert_str_to_date():
    sm_two = SMTwo(3, True, last_review="2020-01-01")
    assert sm_two.last_review == datetime(2020, 1, 1).date()


@pytest.mark.parametrize(
    "bad_last_review, error",
    [
        ("123", DateFormatError),
        ("01-01-2020", DateFormatError),
        ("01/01/2020", DateFormatError),
        (123, TypeError),
        (123.0, TypeError)
    ]
)
def test_last_review_invalid_value(bad_last_review, error):
    with pytest.raises(error):
        SMTwo(3, True, last_review=bad_last_review)


# q < 3, no need to sepcify first visit
@pytest.mark.parametrize(
    "quality, first_visit",
    [
        (0, True),
        (1, True),
        (2, True),
        (0, False),
        (1, False),
        (2, False)
    ]
)
def test_q_less_than_three(quality, first_visit):
    sm_two = SMTwo(quality, first_visit)
    assert sm_two.quality == quality
    assert sm_two.first_visit == first_visit
    assert sm_two.easiness == 2.5
    assert sm_two.interval == 1
    assert sm_two.repetitions == 1
    assert sm_two.last_review == date.today()
    assert sm_two.next_review == date.today() + timedelta(days=1)


# q >= 3 first visit
@pytest.mark.parametrize(
    "quality, first_visit, easiness, interval, repetitions, expected_easiness, expected_interval, expected_repetitions",
    [
        (3, True, 2.5, 1, 1, 2.36, 1, 2),
        (4, True, 2.5, 1, 1, 2.5000000000000004, 1, 2),
        (5, True, 2.5, 1, 1, 2.6, 1, 2),
        (3, False, 2.8, 1, 2, 2.6599999999999997, 6, 3),
        (4, False, 2.8, 1, 2, 2.8000000000000003, 6, 3),
        (5, False, 2.8, 1, 2, 2.9, 6, 3),
        (3, False, 3.1, 6, 3, 2.9599999999999995, 19, 4),
        (4, False, 3.1, 6, 3, 3.1, 19, 4),
        (5, False, 3.1, 6, 3, 3.2, 19, 4),
    ]
)
def test_q_larger_than_and_equal_to_three(quality, first_visit, easiness, interval, repetitions, expected_easiness, expected_interval, expected_repetitions):
    sm_two = SMTwo(quality, first_visit, easiness, interval, repetitions)
    assert sm_two.quality == quality
    assert sm_two.first_visit == first_visit
    assert sm_two.easiness == expected_easiness
    assert sm_two.interval == expected_interval
    assert sm_two.repetitions == expected_repetitions


def test_easiness_lower_bound_reset():
    """
    Tests easiness resets to 1.3 when it goes below 1.3.
    """
    sm_two = SMTwo(3, False, 1.3)
    assert sm_two.easiness == 1.3


# test json method that returns all new information including quality, have the option of including first_visit or not
def test_json():
    sm_two = SMTwo(3, True)
    today = date.today()
    tomorrow = today + timedelta(days=1)
    assert sm_two.json() == json.dumps(
        {
            "quality": 3,
            "first_visit": True,
            "easiness": 2.36,
            "interval": 1,
            "repetitions": 2,
            "last_review": str(today),
            "next_review": str(tomorrow)
        }
    )

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
