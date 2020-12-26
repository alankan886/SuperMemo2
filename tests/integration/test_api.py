import json
from datetime import date, timedelta
from copy import deepcopy

import pytest

from supermemo2 import first_visit, modify, as_json, as_dict


@pytest.mark.parametrize("quality", (0, 1, 2, 3, 4, 5))
def test_first_visit_default_review_date(quality):
    smtwo = first_visit(quality)
    smtwo.quality == quality
    smtwo.prev.easiness == 2.5
    smtwo.prev.interval == 1
    smtwo.prev.repetitions == 1
    smtwo.prev.review_date == date.today()


@pytest.mark.parametrize(
    "quality, review_date",
    (
        [0, date.today() + timedelta(days=1)],
        [1, date.today() + timedelta(days=12)],
        [2, date.today() + timedelta(days=8)],
        [3, date.today()],
        [4, date.today() + timedelta(days=11)],
        [5, date.today() + timedelta(days=2)]
    )
)
def test_first_visit(quality, review_date):
    smtwo = first_visit(quality)
    smtwo.quality == quality
    smtwo.prev.easiness == 2.5
    smtwo.prev.interval == 1
    smtwo.prev.repetitions == 1
    smtwo.review_date == review_date


@pytest.mark.parametrize("quality", (0, 1, 2, 3, 4, 5))
def test_modify_quality(smtwo_after_calc, quality):
    prev_ez = smtwo_after_calc.prev.easiness
    prev_inter = smtwo_after_calc.prev.interval
    prev_rep = smtwo_after_calc.prev.repetitions
    prev_rd = smtwo_after_calc.prev.review_date
    modify(smtwo_after_calc, new_quality=quality)

    assert smtwo_after_calc.quality == quality
    assert smtwo_after_calc.prev.easiness == prev_ez
    assert smtwo_after_calc.prev.interval == prev_inter
    assert smtwo_after_calc.prev.repetitions == prev_rep
    assert smtwo_after_calc.prev.review_date == prev_rd


@pytest.mark.parametrize("easiness", (1.3, 2.5, 3.0))
def test_modify_easiness(smtwo_after_calc, easiness):
    prev_q = smtwo_after_calc.quality
    prev_inter = smtwo_after_calc.prev.interval
    prev_rep = smtwo_after_calc.prev.repetitions
    prev_rd = smtwo_after_calc.prev.review_date
    modify(smtwo_after_calc, new_easiness=easiness)

    assert smtwo_after_calc.quality == prev_q
    assert smtwo_after_calc.prev.easiness == easiness
    assert smtwo_after_calc.prev.interval == prev_inter
    assert smtwo_after_calc.prev.repetitions == prev_rep
    assert smtwo_after_calc.prev.review_date == prev_rd


@pytest.mark.parametrize("interval", (1, 6, 24))
def test_modify_interval(smtwo_after_calc, interval):
    prev_q = smtwo_after_calc.quality
    prev_ez = smtwo_after_calc.prev.easiness
    prev_rep = smtwo_after_calc.prev.repetitions
    prev_rd = smtwo_after_calc.prev.review_date
    modify(smtwo_after_calc, new_interval=interval)

    assert smtwo_after_calc.quality == prev_q
    assert smtwo_after_calc.prev.easiness == prev_ez
    assert smtwo_after_calc.prev.interval == interval
    assert smtwo_after_calc.prev.repetitions == prev_rep
    assert smtwo_after_calc.prev.review_date == prev_rd


@pytest.mark.parametrize("repetitions", (1, 2, 99))
def test_modify_repetitions(smtwo_after_calc, repetitions):
    prev_q = smtwo_after_calc.quality
    prev_ez = smtwo_after_calc.prev.easiness
    prev_inter = smtwo_after_calc.prev.interval
    prev_rd = smtwo_after_calc.prev.review_date
    modify(smtwo_after_calc, new_repetitions=repetitions)

    assert smtwo_after_calc.quality == prev_q
    assert smtwo_after_calc.prev.easiness == prev_ez
    assert smtwo_after_calc.prev.interval == prev_inter
    assert smtwo_after_calc.prev.repetitions == repetitions
    assert smtwo_after_calc.prev.review_date == prev_rd


@pytest.mark.parametrize("review_date", (date(2020, 12, 20),))
def test_modify_last_review(smtwo_after_calc, review_date):
    prev_q = smtwo_after_calc.quality
    prev_ez = smtwo_after_calc.prev.easiness
    prev_inter = smtwo_after_calc.prev.interval
    prev_rep = smtwo_after_calc.prev.repetitions
    modify(smtwo_after_calc, new_review_date=review_date)

    assert smtwo_after_calc.quality == prev_q
    assert smtwo_after_calc.prev.easiness == prev_ez
    assert smtwo_after_calc.prev.interval == prev_inter
    assert smtwo_after_calc.prev.repetitions == prev_rep
    assert smtwo_after_calc.prev.review_date == review_date


def test_modify_no_inputs(smtwo_after_calc):
    with pytest.raises(ValueError) as excinfo:
        modify(smtwo_after_calc)
    assert excinfo.value.args[0] == "a new value is not provided for modification"


# perhaps I don't want to let user pass dates as string

def test_json(smtwo_after_calc):
    json_fmt = json.dumps({
        "quality": 3,
        "prev_easiness": 2.5,
        "prev_interval": 1,
        "prev_repetitions": 1,
        "prev_review_date": str(date.today()),
        "easiness": 2.36,
        "interval": 1,
        "repetitions": 2,
        "review_date": str(date.today() + timedelta(days=1))
    })
    assert as_json(smtwo_after_calc) == json_fmt


def test_json_prev(smtwo_after_calc):
    json_fmt = json.dumps({
        "quality": 3,
        "prev_easiness": 2.5,
        "prev_interval": 1,
        "prev_repetitions": 1,
        "prev_review_date": str(date.today())
    })
    assert as_json(smtwo_after_calc, prev=True) == json_fmt


def test_json_cur(smtwo_after_calc):
    json_fmt = json.dumps({
        "quality": 3,
        "easiness": 2.36,
        "interval": 1,
        "repetitions": 2,
        "review_date": str(date.today() + timedelta(days=1))
    })
    assert as_json(smtwo_after_calc, curr=True) == json_fmt


def test_dict(smtwo_after_calc):
    dict_fmt = {
        "quality": 3,
        "prev_easiness": 2.5,
        "prev_interval": 1,
        "prev_repetitions": 1,
        "prev_review_date": date.today(),
        "easiness": 2.36,
        "interval": 1,
        "repetitions": 2,
        "review_date": date.today() + timedelta(days=1)
    }
    assert as_dict(smtwo_after_calc) == dict_fmt
