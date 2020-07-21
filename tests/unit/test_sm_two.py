from datetime import datetime 

import pytest
from supermemo2 import SMTwo

from ..conftest import sm_two
from ..test_cases import (
    attributes,
    anything,
    quality_less_than_three_nth_visit,
    quality_three_nth_visit_break_easiness_lowerbound,
    first_visit,
    repetitions_equals_two,
    first_visit_input_value_error_handler,
    nth_visit_input_value_error_handler,
    input_type_error_handler
)


def load_test_cases(sm_two, quality, interval, repetitions, easiness, first_visit, last_review):
    sm_two.quality = quality
    sm_two.interval = interval
    sm_two.repetitions = repetitions
    sm_two.easiness = easiness
    sm_two.first_visit = first_visit
    sm_two.last_review = last_review

    sm_two.new_sm_two()

@pytest.mark.parametrize(attributes, quality_less_than_three_nth_visit)
def test_attributes_when_quality_less_than_three(sm_two, quality, interval, repetitions, easiness, first_visit, last_review):
    load_test_cases(sm_two, quality, interval, repetitions, easiness, first_visit, last_review)
    
    old_easiness = sm_two.easiness

    assert sm_two.new_easiness == old_easiness
    assert sm_two.new_interval == 1
    assert sm_two.new_repetitions == 1

@pytest.mark.parametrize(attributes, quality_three_nth_visit_break_easiness_lowerbound)
def test_easiness_lowerbound_reset(sm_two, quality, interval, repetitions, easiness, first_visit, last_review):
    load_test_cases(sm_two, quality, interval, repetitions, easiness, first_visit, last_review)

    assert sm_two.new_easiness == 1.3

@pytest.mark.parametrize(attributes, first_visit)
def test_first_visit_reset(sm_two, quality, interval, repetitions, easiness, first_visit, last_review):
    load_test_cases(sm_two, quality, interval, repetitions, easiness, first_visit, last_review)

    assert sm_two.interval == 0
    assert sm_two.repetitions == 1
    assert sm_two.new_interval == 1
    assert sm_two.new_repetitions == 2

@pytest.mark.parametrize(attributes, first_visit_input_value_error_handler)
def test_first_visit_input_value_error_handler(sm_two, quality, interval, repetitions, easiness, first_visit, last_review):
    with pytest.raises(ValueError):
        load_test_cases(sm_two, quality, interval, repetitions, easiness, first_visit, last_review)

@pytest.mark.parametrize(attributes, nth_visit_input_value_error_handler)
def test_nth_visit_input_value_error_handler(sm_two, quality, interval, repetitions, easiness, first_visit, last_review):
    with pytest.raises(ValueError):
        load_test_cases(sm_two, quality, interval, repetitions, easiness, first_visit, last_review)

@pytest.mark.parametrize(attributes, input_type_error_handler)
def test_input_type_error_handler(sm_two, quality, interval, repetitions, easiness, first_visit, last_review):
    with pytest.raises(TypeError):
        load_test_cases(sm_two, quality, interval, repetitions, easiness, first_visit, last_review)

@pytest.mark.parametrize(attributes, repetitions_equals_two)
def test_repetitions_equals_two_reset(sm_two, quality, interval, repetitions, easiness, first_visit, last_review):
    load_test_cases(sm_two, quality, interval, repetitions, easiness, first_visit, last_review)

    assert sm_two.interval == 1
    assert sm_two.repetitions == 2
    assert sm_two.new_interval == 6
    assert sm_two.new_repetitions == 3

@pytest.mark.parametrize(attributes, anything)
def test_json(sm_two, quality, interval, repetitions, easiness, first_visit, last_review):
    load_test_cases(sm_two, quality, interval, repetitions, easiness, first_visit, last_review)

    json = sm_two.json()
    assert type(json) == dict
    assert "new_interval" in json
    assert "new_repetitions" in json
    assert "new_easiness" in json
    assert type(json["new_interval"]) == int
    assert type(json["new_repetitions"]) == int
    assert type(json["new_easiness"]) == float


