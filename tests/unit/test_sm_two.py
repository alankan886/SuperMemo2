import json
from datetime import date, timedelta

import pytest


def test_SMTwo_instance(empty_smtwo):
    checklist = ["calc", "json", "dict"]
    assert len(vars(empty_smtwo)) == 0
    for method in checklist:
        assert method in dir(empty_smtwo)


@pytest.mark.parametrize(
    "quality, easiness, interval, repetitions, expected_easiness, expected_interval, expected_repetitions, expected_review_date",
    [
        (0, 2.5, 6, 3, 1.7, 1, 1, date.today() + timedelta(days=1)),
        (1, 2.5, 1, 1, 1.96, 1, 1, date.today() + timedelta(days=1)),
        (2, 2.5, 1, 2, 2.1799999999999997, 1, 1, date.today() + timedelta(days=1)),
        (3, 2.5, 1, 1, 2.36, 1, 2, date.today() + timedelta(days=1)),
        (4, 2.5, 1, 1, 2.5000000000000004, 1, 2, date.today() + timedelta(days=1)),
        (5, 2.5, 1, 1, 2.6, 1, 2, date.today() + timedelta(days=1)),
        (3, 2.8, 1, 2, 2.6599999999999997, 6, 3, date.today() + timedelta(days=6)),
        (4, 2.8, 1, 2, 2.8000000000000003, 6, 3, date.today() + timedelta(days=6)),
        (5, 2.8, 1, 2, 2.9, 6, 3, date.today() + timedelta(days=6)),
        (3, 3.1, 6, 3, 2.9599999999999995, 19,
         4, date.today() + timedelta(days=19)),
        (4, 3.1, 6, 3, 3.1, 19, 4, date.today() + timedelta(days=19)),
        (5, 3.1, 6, 3, 3.2, 19, 4, date.today() + timedelta(days=19)),
    ]
)
def test_SMTwo_calc(empty_smtwo, quality, easiness, interval, repetitions, expected_easiness, expected_interval, expected_repetitions, expected_review_date):
    empty_smtwo.calc(quality, easiness, interval, repetitions, date.today())
    assert empty_smtwo.quality == quality
    assert empty_smtwo.easiness == expected_easiness
    assert empty_smtwo.interval == expected_interval
    assert empty_smtwo.repetitions == expected_repetitions
    assert empty_smtwo.prev.easiness == easiness
    assert empty_smtwo.prev.interval == interval
    assert empty_smtwo.prev.repetitions == repetitions
    assert empty_smtwo.prev.review_date == date.today()
    assert empty_smtwo.review_date == expected_review_date


@pytest.mark.parametrize("quality", ["abc", -1, 6, 3.3])
def test_SMTwo_calc_invalid_quality(empty_smtwo, quality):
    if not isinstance(quality, int):
        with pytest.raises(TypeError) as excinfo:
            empty_smtwo.calc(quality, 2.5, 1, 1, date.today())

        if isinstance(quality, str):
            message = f"'_SMTwo__quality' must be <class 'int'> (got '{quality}' that is a {type(quality)})."
            assert excinfo.value.args[0] == message
        else:
            message = f"'_SMTwo__quality' must be <class 'int'> (got {quality} that is a {type(quality)})."
            assert excinfo.value.args[0] == message
    else:
        with pytest.raises(ValueError) as excinfo:
            empty_smtwo.calc(quality, 2.5, 1, 1, date.today())
        message = f"'_SMTwo__quality' must be in range(0, 6) (got {quality})"
        assert excinfo.value.args[0] == message


@pytest.mark.parametrize("easiness", ["abc", 0, 1.2])
def test_SMTwo_calc_invalid_easiness(empty_smtwo, easiness):
    if not isinstance(easiness, float):
        with pytest.raises(TypeError) as excinfo:
            empty_smtwo.calc(3, easiness, 1, 1, date.today())

        if isinstance(easiness, str):
            message = f"'_Prev__easiness' must be <class 'float'> (got '{easiness}' that is a {type(easiness)})."
            assert excinfo.value.args[0] == message
        else:
            message = f"'_Prev__easiness' must be <class 'float'> (got {easiness} that is a {type(easiness)})."
            assert excinfo.value.args[0] == message
    else:
        with pytest.raises(ValueError) as excinfo:
            empty_smtwo.calc(3, easiness, 1, 1, date.today())
        assert excinfo.value.args[0] == "easiness has a minimum value of 1.3"


@pytest.mark.parametrize("interval", ["abc", -1, 0, 1.2])
def test_SMTwo_calc_invalid_interval(empty_smtwo, interval):
    if not isinstance(interval, int):
        with pytest.raises(TypeError) as excinfo:
            empty_smtwo.calc(3, 2.5, interval, 1, date.today())

        if isinstance(interval, str):
            message = f"'_Prev__interval' must be <class 'int'> (got '{interval}' that is a {type(interval)})."
            assert excinfo.value.args[0] == message
        else:
            message = f"'_Prev__interval' must be <class 'int'> (got {interval} that is a {type(interval)})."
            assert excinfo.value.args[0] == message
    else:
        with pytest.raises(ValueError) as excinfo:
            empty_smtwo.calc(3, 2.5, interval, 1, date.today())
        assert excinfo.value.args[0] == "interval has a minimum value of 1"


@pytest.mark.parametrize("repetitions", ["abc", -1, 0, 1.2])
def test_SMTwo_calc_invalid_repetitions(empty_smtwo, repetitions):
    if not isinstance(repetitions, int):
        with pytest.raises(TypeError) as excinfo:
            empty_smtwo.calc(3, 2.5, 1, repetitions, date.today())

        if isinstance(repetitions, str):
            message = f"'_Prev__repetitions' must be <class 'int'> (got '{repetitions}' that is a {type(repetitions)})."
            assert excinfo.value.args[0] == message
        else:
            message = f"'_Prev__repetitions' must be <class 'int'> (got {repetitions} that is a {type(repetitions)})."
            assert excinfo.value.args[0] == message
    else:
        with pytest.raises(ValueError) as excinfo:
            empty_smtwo.calc(3, 2.5, 1, repetitions, date.today())
        message = "repetitions has a minimum value of 1"
        assert excinfo.value.args[0] == message


# Down to line we can allow user to pass a string, and we can convert it to a date
@pytest.mark.parametrize("review_date", ["abc", 123, 123.0, -123, "2020/12/20", "2020-12-20", "12/20/2020", "12-20-2020", "20-12-2020", "20/12/2020"])
def test_SMTwo_calc_invalid_last_review(empty_smtwo, review_date):
    with pytest.raises(TypeError) as excinfo:
        empty_smtwo.calc(3, 2.5, 1, 1, review_date)

    if isinstance(review_date, str):
        message = f"'_Prev__review_date' must be <class 'datetime.date'> (got '{review_date}' that is a {type(review_date)})."
        assert excinfo.value.args[0] == message
    else:
        message = f"'_Prev__review_date' must be <class 'datetime.date'> (got {review_date} that is a {type(review_date)})."
        assert excinfo.value.args[0] == message


def test_SMTwo_json(smtwo_after_calc):
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
    assert smtwo_after_calc.json() == json_fmt


def test_SMTwo_json_prev(smtwo_after_calc):
    json_fmt = json.dumps({
        "quality": 3,
        "prev_easiness": 2.5,
        "prev_interval": 1,
        "prev_repetitions": 1,
        "prev_review_date": str(date.today())
    })
    assert smtwo_after_calc.json(prev=True) == json_fmt


def test_SMTwo_json_curr(smtwo_after_calc):
    json_fmt = json.dumps({
        "quality": 3,
        "easiness": 2.36,
        "interval": 1,
        "repetitions": 2,
        "review_date": str(date.today() + timedelta(days=1))
    })
    assert smtwo_after_calc.json(curr=True) == json_fmt


def test_SMTwo_json_exception(empty_smtwo):
    with pytest.raises(Exception) as excinfo:
        empty_smtwo.json()

    assert excinfo.value.args[0] == "SMTwo.calc method is required to be called first"


def test_SMTwo_dict(smtwo_after_calc):
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
    assert smtwo_after_calc.dict() == dict_fmt


def test_SMTwo_dict_prev(smtwo_after_calc):
    dict_fmt = {
        "quality": 3,
        "prev_easiness": 2.5,
        "prev_interval": 1,
        "prev_repetitions": 1,
        "prev_review_date": date.today()
    }
    assert smtwo_after_calc.dict(prev=True) == dict_fmt


def test_SMTwo_dict_curr(smtwo_after_calc):
    dict_fmt = {
        "quality": 3,
        "easiness": 2.36,
        "interval": 1,
        "repetitions": 2,
        "review_date": date.today() + timedelta(days=1)
    }
    assert smtwo_after_calc.dict(curr=True) == dict_fmt


def test_SMTwo_dict_exception(empty_smtwo):
    with pytest.raises(Exception) as excinfo:
        empty_smtwo.dict()

    assert excinfo.value.args[0] == "SMTwo.calc method is required to be called first"
