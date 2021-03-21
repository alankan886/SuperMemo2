from math import ceil
from datetime import date, datetime, timedelta
from typing import Optional, Union, Dict

import attr


year_mon_day = "%Y-%m-%d"
mon_day_year = "%m-%d-%Y"
day_mon_year = "%d-%m-%Y"


@attr.s
class SMTwo:
    easiness = attr.ib(default=2.5, validator=attr.validators.instance_of(float))
    interval = attr.ib(default=0, validator=attr.validators.instance_of(int))
    repetitions = attr.ib(default=0, validator=attr.validators.instance_of(int))

    def first_review(
        self,
        quality: int,
        review_date: Optional[Union[date, str]] = None,
        date_fmt: Optional[str] = None,
    ) -> Dict:
        if not review_date:
            review_date = date.today()

        if not date_fmt:
            date_fmt = year_mon_day

        self.easiness = 2.5
        self.interval = 0
        self.repetitions = 0

        return self.review(quality, review_date, date_fmt)

    def review(
        self,
        quality: int,
        review_date: Optional[Union[date, str]] = None,
        date_fmt: Optional[str] = None,
    ) -> Dict:
        if not review_date:
            review_date = date.today()

        if not date_fmt:
            date_fmt = year_mon_day

        if isinstance(review_date, str):
            review_date = datetime.strptime(review_date, date_fmt).date()

        if quality < 3:
            self.interval = 1
            self.repetitions = 0
        else:
            if self.repetitions == 0:
                self.interval = 1
            elif self.repetitions == 1:
                self.interval = 6
            else:
                self.interval = ceil(self.interval * self.easiness)

            self.repetitions = self.repetitions + 1

        self.easiness += 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)
        if self.easiness < 1.3:
            self.easiness = 1.3

        review_date += timedelta(days=self.interval)
        return {
            "easiness": self.easiness,
            "interval": self.interval,
            "repetitions": self.repetitions,
            "review_date": review_date,
        }
