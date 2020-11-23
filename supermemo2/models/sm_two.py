from datetime import date, datetime, timedelta
import warnings

import attr

from .prev import Prev
from supermemo2.exceptions import DateFormatError


@attr.s()
class SMTwo:
    quality = attr.ib(converter=int)
    first_visit = attr.ib()
    easiness = attr.ib(default=2.5, converter=float)
    interval = attr.ib(default=0, converter=int)
    repetitions = attr.ib(default=1, converter=int)
    last_review = attr.ib(default=date.today())
    __next_review = attr.ib(init=False)
    __old_values = attr.ib(factory=dict)
    __prev = attr.ib(init=False)

    __date_fmt = "%Y-%m-%d"

    @first_visit.validator
    def _check_first_visit(self, attribute, value):
        if value is not True and value is not False:
            raise ValueError(f"first_visit value, '{value}', is not a valid boolean value")

    @easiness.validator
    def _easiness_first_visit(self, attribute, value):
        if self.first_visit and value != 2.5:
            setattr(self, attribute.name, 2.5)
            warnings.warn("easiness automatically set to 2.5, easiness should be 2.5 for the first visit")

    @last_review.validator
    def _convert_if_str(self, attribute, value):
        if not isinstance(value, date) and isinstance(value, str):
            try:
                setattr(self, attribute.name, datetime.strptime(value, self.__date_fmt).date())
            except ValueError:
                message = "please provide the last review date in the format of Year-Month-Day or an date object"
                raise DateFormatError(message)

    def __attrs_post_init__(self):
        self.__prev = Prev(self, self.easiness, self.interval, self.repetitions)
        # take this out later
        self.interval = 1
        self.__next_review = self.last_review + timedelta(days=self.interval)

    @property
    def next_review(self):
        return self.__next_review

    @property
    def prev(self):
        return self.__prev


if __name__ == "__main__":
    sm = SMTwo(1, True)
    print(sm.prev)
    sm.prev.repetitions = 2
    print(sm.interval)
