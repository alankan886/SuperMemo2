from math import ceil
from datetime import date, datetime, timedelta
from typing import Optional, Union

import attr

__all__ = ["first_review", "SMTwo"]

year_mon_day = "%Y-%m-%d"
mon_day_year = "%m-%d-%Y"
day_mon_year = "%d-%m-%Y"


def first_review(
    quality: int,
    review_date: Optional[Union[date, str]] = None,
    date_fmt: Optional[str] = None,
):
    if not review_date:
        review_date = date.today()
    
    if not date_fmt:
        date_fmt = year_mon_day

    return review(quality, 2.5, 0, 0, review_date, date_fmt)


def review(
    quality: int,
    easiness: float,
    interval: int,
    repetitions: int,
    review_date: Optional[Union[date, str]] = None,
    date_fmt: Optional[str] = None,
):
    if not review_date:
        review_date = date.today()
    
    if not date_fmt:
        date_fmt = year_mon_day

    if isinstance(review_date, str):
        review_date = datetime.strptime(review_date, date_fmt).date()

    if quality < 3:
        interval = 1
        repetitions = 0
    else:
        if repetitions == 0:
            interval = 1
        elif repetitions == 1:
            interval = 6
        else:
            interval = ceil(interval * easiness)

        repetitions = repetitions + 1

    easiness += 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)
    if easiness < 1.3:
        easiness = 1.3

    review_date += timedelta(days=interval)
    return {
        "quality": quality,
        "easiness": easiness,
        "interval": interval,
        "repetitions": repetitions,
        "review_date": review_date,
    }