import json
from datetime import date, datetime, timedelta
import warnings

import attr

from supermemo2.models.prev import Prev
from supermemo2.exceptions import DateFormatError


@attr.s()
class SMTwo:
    # listener on quality and last_review is needed
    quality = attr.ib()
    first_visit = attr.ib()
    easiness = attr.ib(default=2.5, converter=float)
    interval = attr.ib(default=1, converter=int)
    repetitions = attr.ib(default=1, converter=int)
    last_review = attr.ib(default=date.today())
    __next_review = attr.ib(init=False)
    __prev = attr.ib(init=False)

    __date_fmt = "%Y-%m-%d"

    @quality.validator
    def _check_quality(self, attribute, value):
        # validator is after converter,
        # using custom converter here to not convert bool to int to avoid confusing bugs,
        # since int(True) = 1 and int(False) = 0.
        if isinstance(value, bool):
            message = f"{value} is not an integer"
            raise TypeError(message)
        else:
            setattr(self, attribute.name, int(value))

        if not 0 <= value <= 5:
            message = f"{value} is not an integer between the range of 0 to 5"
            raise ValueError(message)

    @first_visit.validator
    def _check_first_visit(self, attribute, value):
        if value is not True and value is not False:
            message = f"first_visit value, '{value}', is not a valid boolean value"
            raise TypeError(message)

    @easiness.validator
    def _easiness_first_visit(self, attribute, value):
        if self.first_visit and value != 2.5:
            setattr(self, attribute.name, 2.5)
            warnings.warn("easiness automatically set to 2.5, easiness should be 2.5 for the first visit")

    @interval.validator
    def _interval_first_visit(self, attribute, value):
        if self.first_visit and value != 1:
            setattr(self, attribute.name, 1)
            warnings.warn("interval automatically set to 1, interval should be 1 for the first visit")

    @repetitions.validator
    def _repetitions_first_visit(self, attribute, value):
        if self.first_visit and value != 1:
            setattr(self, attribute.name, 1)
            warnings.warn("repetitions automatically set to 1, repetitions should be 1 for the first visit")

    @last_review.validator
    def _convert_if_str(self, attribute, value):
        if isinstance(value, str):
            try:
                setattr(self, attribute.name, datetime.strptime(value, self.__date_fmt).date())
            except ValueError:
                message = "please provide the last review date in the format of Year-Month-Day or an date object"
                raise DateFormatError(message)
        elif not isinstance(value, date):
            message = "invalid type for last_review, which should be type Date or str"
            raise TypeError(message)

    def __attrs_post_init__(self):
        self.__prev = Prev(self, self.easiness, self.interval, self.repetitions)
        if self.quality < 3:
            self.interval = 1
            self.repetitions = 1
        else:
            if self.repetitions == 1:
                pass
            elif self.repetitions == 2:
                self.interval = 6
            else:
                self.interval = round(self.interval * self.easiness)

            self.repetitions += 1
            self.easiness = self.easiness - 0.8 + 0.28 * self.quality - 0.02 * self.quality**2

        if self.easiness < 1.3:
            self.easiness = 1.3

        self.__next_review = self.last_review + timedelta(days=self.interval)

    @property
    def next_review(self):
        return self.__next_review

    @property
    def prev(self):
        return self.__prev

    def json(self):
        return json.dumps(
            {
                "quality": self.quality,
                "first_visit": self.first_visit,
                "easiness": self.easiness,
                "interval": self.interval,
                "repetitions": self.repetitions,
                "last_review": str(self.last_review),
                "next_review": str(self.next_review),
            }
        )
