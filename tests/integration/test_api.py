import json
from datetime import date, timedelta

import pytest

from supermemo2 import first_visit, modify, as_json


@pytest.mark.parametrize("quality", (0, 1, 2, 3, 4, 5))
def test_first_visit_default_last_review(quality):
    smtwo = first_visit(quality)
    smtwo.quality == quality
    smtwo.prev.easiness == 2.5
    smtwo.prev.interval == 1
    smtwo.prev.repetitions == 1
    smtwo.last_review == date.today()


@pytest.mark.parametrize(
    "quality, last_review",
    (
        [0, date.today() + timedelta(days=1)],
        [1, date.today() + timedelta(days=12)],
        [2, date.today() + timedelta(days=8)],
        [3, date.today()],
        [4, date.today() + timedelta(days=11)],
        [5, date.today() + timedelta(days=2)]
    )
)
def test_first_visit(quality, last_review):
    smtwo = first_visit(quality)
    smtwo.quality == quality
    smtwo.prev.easiness == 2.5
    smtwo.prev.interval == 1
    smtwo.prev.repetitions == 1
    smtwo.last_review == last_review


@pytest.mark.parametrize("quality", (0, 1, 2, 3, 4, 5))
def test_modify_quality(smtwo_after_calc, quality):
    new_smtwo = modify(smtwo_after_calc, new_quality=quality)
    assert new_smtwo.quality == quality
    assert new_smtwo.prev.easiness == smtwo_after_calc.prev.easiness
    assert new_smtwo.prev.interval == smtwo_after_calc.prev.interval
    assert new_smtwo.prev.repetitions == smtwo_after_calc.prev.repetitions
    assert new_smtwo.last_review == smtwo_after_calc.last_review


@pytest.mark.parametrize("easiness", (1.3, 2.5, 3.0))
def test_modify_easiness(smtwo_after_calc, easiness):
    new_smtwo = modify(smtwo_after_calc, new_easiness=easiness)
    assert new_smtwo.quality == smtwo_after_calc.quality
    assert new_smtwo.prev.easiness == easiness
    assert new_smtwo.prev.interval == smtwo_after_calc.prev.interval
    assert new_smtwo.prev.repetitions == smtwo_after_calc.prev.repetitions
    assert new_smtwo.last_review == smtwo_after_calc.last_review


@pytest.mark.parametrize("interval", (1, 6, 24))
def test_modify_interval(smtwo_after_calc, interval):
    new_smtwo = modify(smtwo_after_calc, new_interval=interval)
    assert new_smtwo.quality == smtwo_after_calc.quality
    assert new_smtwo.prev.easiness == smtwo_after_calc.prev.easiness
    assert new_smtwo.prev.interval == interval
    assert new_smtwo.prev.repetitions == smtwo_after_calc.prev.repetitions
    assert new_smtwo.last_review == smtwo_after_calc.last_review


@pytest.mark.parametrize("repetitions", (1, 2, 99))
def test_modify_repetitions(smtwo_after_calc, repetitions):
    new_smtwo = modify(smtwo_after_calc, new_repetitions=repetitions)
    assert new_smtwo.quality == smtwo_after_calc.quality
    assert new_smtwo.prev.easiness == smtwo_after_calc.prev.easiness
    assert new_smtwo.prev.interval == smtwo_after_calc.prev.interval
    assert new_smtwo.prev.repetitions == repetitions
    assert new_smtwo.last_review == smtwo_after_calc.last_review


@pytest.mark.parametrize("last_review", (date(2020, 12, 20),))
def test_modify_last_review(smtwo_after_calc, last_review):
    new_smtwo = modify(smtwo_after_calc, new_last_review=last_review)
    assert new_smtwo.quality == smtwo_after_calc.quality
    assert new_smtwo.prev.easiness == smtwo_after_calc.prev.easiness
    assert new_smtwo.prev.interval == smtwo_after_calc.prev.interval
    assert new_smtwo.prev.repetitions == smtwo_after_calc.prev.repetitions
    assert new_smtwo.last_review == last_review


def test_modify_no_inputs(smtwo_after_calc):
    with pytest.raises(ValueError) as excinfo:
        modify(smtwo_after_calc)
    assert excinfo.value.args[0] == "a new value is not provided for modification"


# perhaps I don't want to let user pass dates as string
def test_json(smtwo_after_calc):
    json_fmt = json.dumps({
        "quality": 3,
        "easiness": 2.5,
        "interval": 1,
        "repetitions": 1,
        "last_review": str(date.today()),
        "next_review": str(date.today() + timedelta(days=1))
    })
    assert as_json(smtwo_after_calc) == json_fmt
