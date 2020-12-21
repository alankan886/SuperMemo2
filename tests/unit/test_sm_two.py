from datetime import date, timedelta

import pytest


def test_SMTwo_instance(smtwo):
    checklist = ["calc", "json", "dict"]
    assert len(vars(smtwo)) == 0
    for method in checklist:
        assert method in dir(smtwo)


# might need to think more on non first/second visit test cases


@pytest.mark.parametrize(
    "quality, easiness, interval, repetitions, expected_easiness, expected_interval, expected_repetitions, next_review",
    [
        (0, 2.5, 6, 3, 2.5, 1, 1, date.today() + timedelta(days=1)),
        (1, 2.5, 1, 1, 2.5, 1, 1, date.today() + timedelta(days=1)),
        (2, 2.5, 1, 2, 2.5, 1, 1, date.today() + timedelta(days=1)),
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
def test_SMTwo_calc(smtwo, quality, easiness, interval, repetitions, expected_easiness, expected_interval, expected_repetitions, next_review):
    smtwo.calc(quality, easiness, interval, repetitions, date.today())
    assert smtwo.quality == quality
    assert smtwo.easiness == expected_easiness
    assert smtwo.interval == expected_interval
    assert smtwo.repetitions == expected_repetitions
    assert smtwo.prev.easiness == easiness
    assert smtwo.prev.interval == interval
    assert smtwo.prev.repetitions == repetitions
    assert smtwo.last_review == date.today()
    assert smtwo.next_review == next_review


@pytest.mark.parametrize("quality", ["abc", -1, 6, 3.3])
def test_SMTwo_calc_invalid_quality(smtwo, quality):
    if not isinstance(quality, int):
        with pytest.raises(TypeError) as excinfo:
            smtwo.calc(quality, 2.5, 1, 1, date.today())

        if isinstance(quality, str):
            message = f"'_SMTwo__quality' must be <class 'int'> (got '{quality}' that is a {type(quality)})."
            assert excinfo.value.args[0] == message
        else:
            message = f"'_SMTwo__quality' must be <class 'int'> (got {quality} that is a {type(quality)})."
            assert excinfo.value.args[0] == message
    else:
        with pytest.raises(ValueError) as excinfo:
            smtwo.calc(quality, 2.5, 1, 1, date.today())
        message = f"'_SMTwo__quality' must be in range(0, 6) (got {quality})"
        assert excinfo.value.args[0] == message


@pytest.mark.parametrize("easiness", ["abc", 0, 1.2])
def test_SMTwo_calc_invalid_easiness(smtwo, easiness):
    if not isinstance(easiness, float):
        with pytest.raises(TypeError) as excinfo:
            smtwo.calc(3, easiness, 1, 1, date.today())

        if isinstance(easiness, str):
            message = f"'_Prev__easiness' must be <class 'float'> (got '{easiness}' that is a {type(easiness)})."
            assert excinfo.value.args[0] == message
        else:
            message = f"'_Prev__easiness' must be <class 'float'> (got {easiness} that is a {type(easiness)})."
            assert excinfo.value.args[0] == message
    else:
        with pytest.raises(ValueError) as excinfo:
            smtwo.calc(3, easiness, 1, 1, date.today())
        assert excinfo.value.args[0] == "easiness has a minimum value of 1.3"


@pytest.mark.parametrize("interval", ["abc", -1, 0, 1.2])
def test_SMTwo_calc_invalid_interval(smtwo, interval):
    if not isinstance(interval, int):
        with pytest.raises(TypeError) as excinfo:
            smtwo.calc(3, 2.5, interval, 1, date.today())

        if isinstance(interval, str):
            message = f"'_Prev__interval' must be <class 'int'> (got '{interval}' that is a {type(interval)})."
            assert excinfo.value.args[0] == message
        else:
            message = f"'_Prev__interval' must be <class 'int'> (got {interval} that is a {type(interval)})."
            assert excinfo.value.args[0] == message
    else:
        with pytest.raises(ValueError) as excinfo:
            smtwo.calc(3, 2.5, interval, 1, date.today())
        assert excinfo.value.args[0] == "interval has a minimum value of 1"


@pytest.mark.parametrize("repetitions", ["abc", -1, 0, 1.2])
def test_SMTwo_calc_invalid_repetitions(smtwo, repetitions):
    if not isinstance(repetitions, int):
        with pytest.raises(TypeError) as excinfo:
            smtwo.calc(3, 2.5, 1, repetitions, date.today())

        if isinstance(repetitions, str):
            message = f"'_Prev__repetitions' must be <class 'int'> (got '{repetitions}' that is a {type(repetitions)})."
            assert excinfo.value.args[0] == message
        else:
            message = f"'_Prev__repetitions' must be <class 'int'> (got {repetitions} that is a {type(repetitions)})."
            assert excinfo.value.args[0] == message
    else:
        with pytest.raises(ValueError) as excinfo:
            smtwo.calc(3, 2.5, 1, repetitions, date.today())
        assert excinfo.value.args[0] == "todo"


@pytest.mark.skip("it's not checking right yet")
@pytest.mark.parametrize("last_review", ["abc", 123, 123.0, -123, "12/20/2020", "12-20-2020", "20-12-2020", "20/12/2020"])
def test_SMTwo_calc_invalid_last_review(smtwo, last_review):
    with pytest.raises(ValueError):
        smtwo.calc(3, 2.5, 1, 1, last_review)
