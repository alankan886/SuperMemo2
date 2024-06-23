from datetime import datetime, timedelta

import pytest
from freezegun import freeze_time

from supermemo2 import first_review, review

FREEZE_DATE = "2024-01-01"
MOCK_TODAY = datetime.fromisoformat(FREEZE_DATE).replace(microsecond=0)


@freeze_time(FREEZE_DATE)
@pytest.mark.parametrize(
    "quality, expected_easiness, expected_interval, expected_repetitions, expected_review_date",
    [
        (
            0,
            1.7000000000000002,
            1,
            0,
            str(MOCK_TODAY + timedelta(days=1)),
        ),
        (
            1,
            1.96,
            1,
            0,
            str(MOCK_TODAY + timedelta(days=1)),
        ),
        (
            2,
            2.1799999999999997,
            1,
            0,
            str(MOCK_TODAY + timedelta(days=1)),
        ),
        (
            3,
            2.36,
            1,
            1,
            str(MOCK_TODAY + timedelta(days=1)),
        ),
        (
            4,
            2.5,
            1,
            1,
            str(MOCK_TODAY + timedelta(days=1)),
        ),
        (
            5,
            2.6,
            1,
            1,
            str(MOCK_TODAY + timedelta(days=1)),
        ),
    ],
)
def test_first_review(
    quality,
    expected_easiness,
    expected_interval,
    expected_repetitions,
    expected_review_date,
):

    reviewed = first_review(quality)

    assert reviewed["easiness"] == expected_easiness
    assert reviewed["interval"] == expected_interval
    assert reviewed["repetitions"] == expected_repetitions
    assert reviewed["review_date"] == expected_review_date


@freeze_time(FREEZE_DATE)
@pytest.mark.parametrize(
    "quality, review_date, expected_easiness, expected_interval, expected_repetitions, expected_review_date",
    [
        (0, MOCK_TODAY, 1.7000000000000002, 1, 0, str(MOCK_TODAY + timedelta(days=1))),
        (1, MOCK_TODAY, 1.96, 1, 0, str(MOCK_TODAY + timedelta(days=1))),
        (2, MOCK_TODAY, 2.1799999999999997, 1, 0, str(MOCK_TODAY + timedelta(days=1))),
        (3, MOCK_TODAY, 2.36, 1, 1, str(MOCK_TODAY + timedelta(days=1))),
        (4, MOCK_TODAY, 2.5, 1, 1, str(MOCK_TODAY + timedelta(days=1))),
        (5, MOCK_TODAY, 2.6, 1, 1, str(MOCK_TODAY + timedelta(days=1))),
    ],
)
def test_first_review_given_date(
    quality,
    review_date,
    expected_easiness,
    expected_interval,
    expected_repetitions,
    expected_review_date,
):
    reviewed = first_review(quality, review_date)

    assert reviewed["easiness"] == expected_easiness
    assert reviewed["interval"] == expected_interval
    assert reviewed["repetitions"] == expected_repetitions
    assert reviewed["review_date"] == expected_review_date


@freeze_time(FREEZE_DATE)
@pytest.mark.parametrize(
    "quality, easiness, interval, repetitions, expected_easiness, expected_interval, expected_repetitions, expected_review_date",
    [
        (0, 2.3, 12, 3, 1.5, 1, 0, str(MOCK_TODAY + timedelta(days=1))),
        (1, 2.3, 12, 3, 1.7599999999999998, 1, 0, str(MOCK_TODAY + timedelta(days=1))),
        (2, 2.3, 12, 3, 1.9799999999999998, 1, 0, str(MOCK_TODAY + timedelta(days=1))),
        (
            3,
            2.3,
            12,
            3,
            2.1599999999999997,
            28,
            4,
            str(MOCK_TODAY + timedelta(days=28)),
        ),
        (4, 2.3, 12, 3, 2.3, 28, 4, str(MOCK_TODAY + timedelta(days=28))),
        (5, 2.3, 12, 3, 2.4, 28, 4, str(MOCK_TODAY + timedelta(days=28))),
    ],
)
def test_review(
    quality,
    easiness,
    interval,
    repetitions,
    expected_easiness,
    expected_interval,
    expected_repetitions,
    expected_review_date,
):
    reviewed = review(quality, easiness, interval, repetitions)

    assert reviewed["easiness"] == expected_easiness
    assert reviewed["interval"] == expected_interval
    assert reviewed["repetitions"] == expected_repetitions
    assert reviewed["review_date"] == expected_review_date


@pytest.mark.parametrize(
    "quality, easiness, interval, repetitions, review_date, expected_easiness, expected_interval, expected_repetitions, expected_review_date",
    [
        (
            0,
            2.3,
            12,
            3,
            MOCK_TODAY,
            1.5,
            1,
            0,
            str(MOCK_TODAY + timedelta(days=1)),
        ),
        (
            1,
            2.3,
            12,
            3,
            MOCK_TODAY,
            1.7599999999999998,
            1,
            0,
            str(MOCK_TODAY + timedelta(days=1)),
        ),
        (
            2,
            2.3,
            12,
            3,
            MOCK_TODAY,
            1.9799999999999998,
            1,
            0,
            str(MOCK_TODAY + timedelta(days=1)),
        ),
        (
            3,
            2.3,
            12,
            3,
            MOCK_TODAY,
            2.1599999999999997,
            28,
            4,
            str(MOCK_TODAY + timedelta(days=28)),
        ),
        (
            4,
            2.3,
            12,
            3,
            MOCK_TODAY,
            2.3,
            28,
            4,
            str(MOCK_TODAY + timedelta(days=28)),
        ),
        (5, 2.3, 12, 3, MOCK_TODAY, 2.4, 28, 4, str(MOCK_TODAY + timedelta(days=28))),
        # test case for when easiness drops lower than 1.3
        (0, 1.3, 12, 3, MOCK_TODAY, 1.3, 1, 0, str(MOCK_TODAY + timedelta(days=1))),
        # test case for for repetitions equals to 2
        (4, 2.5, 1, 1, MOCK_TODAY, 2.5, 6, 2, str(MOCK_TODAY + timedelta(days=6))),
    ],
)
def test_review_given_date(
    quality,
    easiness,
    interval,
    repetitions,
    review_date,
    expected_easiness,
    expected_interval,
    expected_repetitions,
    expected_review_date,
):
    reviewed = review(quality, easiness, interval, repetitions, review_date)

    assert reviewed["easiness"] == expected_easiness
    assert reviewed["interval"] == expected_interval
    assert reviewed["repetitions"] == expected_repetitions
    assert reviewed["review_date"] == expected_review_date
