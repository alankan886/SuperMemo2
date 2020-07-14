import pytest
from datetime import datetime 

from supermemo2 import SMTwo

@pytest.fixture(params=[
    [0, 60, 7, 1.5, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [1, 30, 4, 1.6, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [2, 15, 3, 1.7, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [0, 60, 7, 1.5, False, "2020-07-13"],
    [1, 30, 4, 1.6, False, "2020-07-13"],
    [2, 15, 3, 1.7, False, "2020-07-13"],
    [1, 0, 1, 2.5, True, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [1, 0, 1, 2.5, True, "2020-07-13"],
    [3, 31, 6, 1.3, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [0, 24, 4, 1.4, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [3, 12, 5, 1.4, False, "2020-07-13"]
])
def anything(request):
    '''Returns a SuperMemo-2 object.'''
    return SMTwo(*request.param)

@pytest.fixture(params=[
    [0, 60, 7, 1.5, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [1, 30, 4, 1.6, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [2, 15, 3, 1.7, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [0, 60, 7, 1.5, False, "2020-07-13"],
    [1, 30, 4, 1.6, False, "2020-07-13"],
    [2, 15, 3, 1.7, False, "2020-07-13"],
    [1, 0, 1, 2.5, True, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [1, 0, 1, 2.5, True, "2020-07-13"]
])
def quality_less_than_three_nth_visit(request):
    '''Returns a SuperMemo-2 objcet with a quality of 0'''
    return SMTwo(*request.param)

@pytest.fixture(params=[
    [3, 31, 6, 1.3, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [3, 24, 4, 1.4, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [3, 12, 5, 1.4, False, "2020-07-13"]
])
def quality_three_nth_visit_break_easiness_lowerbound(request):
    '''Returns a SuperMemo-2 objcet with a quality of 3'''
    return SMTwo(*request.param)

@pytest.fixture(params=[
    [3, 0, 1, 2.5, True, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [4, 0, 1, 2.5, True, "2020-07-13"]
])
def first_visit(request):
    '''Returns a SuperMemo-2 objcet with a first visit values.'''
    return SMTwo(*request.param)

@pytest.fixture(params=[
    [3, 1, 2, 2.5, False, datetime.strptime("2020-07-13", "%Y-%m-%d").date()],
    [4, 1, 2, 2.5, False, "2020-07-13"]
])
def repetitions_equals_two(request):
    '''Returns a SuperMemo-2 objcet with a repetitions of 1'''
    return SMTwo(*request.param)


def test_attributes_when_quality_less_than_three(quality_less_than_three_nth_visit):
    old_easiness = quality_less_than_three_nth_visit.easiness
    
    assert quality_less_than_three_nth_visit.new_easiness == old_easiness
    assert quality_less_than_three_nth_visit.new_interval == 1
    assert quality_less_than_three_nth_visit.new_repetitions == 1

def test_easiness_lowerbound_reset(quality_three_nth_visit_break_easiness_lowerbound):
    quality_three_nth_visit_break_easiness_lowerbound.new_sm_two()
    assert quality_three_nth_visit_break_easiness_lowerbound.new_easiness == 1.3

def test_first_visit_reset(first_visit):
    assert first_visit.interval == 0
    assert first_visit.repetitions == 1
    assert first_visit.new_interval == 1
    assert first_visit.new_repetitions == 2

@pytest.mark.parametrize("quality, interval, repetitions, easiness, first_visit, last_review", [
    (0, 1, 1, 2.5, True, "2020-07-14"),
    (0, -1, 1, 2.5, True, "2020-07-14"),
    (1, 0, 0, 2.5, True, "2020-07-14"),
    (1, 0, 2, 2.5, True, "2020-07-14"),
    (1, 0, 1, 2.4, True, "2020-07-14"),
    (1, 0, 1, 2.6, True, "2020-07-14"),
    (-1, 0, 1, 2.5, True, "2020-07-14"),
    (6, 0, 1, 2.5, True, "2020-07-14"),
    (5, 0, 1, 2.5, True, ""),
    (3, 0, 1, 2.5, True, "abcabc"),
    (3, 0, 1, 2.5, True, "06-15-2020"),
    (123, 123, 123, 123, True, "2020-07-14")
])
def test_first_visit_input_value_error_handler(quality, interval, repetitions, easiness, first_visit, last_review):
    with pytest.raises(ValueError):
        SMTwo(quality, interval, repetitions, easiness, first_visit, last_review)

@pytest.mark.parametrize("quality, interval, repetitions, easiness, first_visit, last_review", [
    (2, 30, 4, 1.0, False, "2020-05-06")
])
def test_nth_visit_input_value_error_handler(quality, interval, repetitions, easiness, first_visit, last_review):
    with pytest.raises(ValueError):
        SMTwo(quality, interval, repetitions, easiness, first_visit, last_review)

@pytest.mark.parametrize("quality, interval, repetitions, easiness, first_visit, last_review", [
    ("abc", 0, 1, 2.5, True, "2020-07-14"),
    (1, "cba", 1, 2.5, True, "2020-07-14"),
    (2, 0, "abc", 2.5, True, "2020-07-14"),
    (3, 0, 1, "efg", True, "2020-07-14"),
    (3, 0, 1, 2.5, "abc", "2020-07-14"),
    (4, 0, 1, 2.5, True, 123),
    ("abc", "def", "hij", "lmn", "opr", "xyz")
])

def test_input_type_error_handler(quality, interval, repetitions, easiness, first_visit, last_review):
    with pytest.raises(TypeError):
        SMTwo(quality, interval, repetitions, easiness, first_visit, last_review)

def test_repetitions_equals_two_reset(repetitions_equals_two):
    assert repetitions_equals_two.interval == 1
    assert repetitions_equals_two.repetitions == 2
    assert repetitions_equals_two.new_interval == 6
    assert repetitions_equals_two.new_repetitions == 3

def test_json(anything):
    json = anything.json()
    assert type(json) == dict
    assert "new_interval" in json
    assert "new_repetitions" in json
    assert "new_easiness" in json
    assert type(json["new_interval"]) == int
    assert type(json["new_repetitions"]) == int
    assert type(json["new_easiness"]) == float


