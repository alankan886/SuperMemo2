import json
from datetime import date, timedelta

import attr

from .exceptions import CalcNotCalledYet
from .util import add_from_dict


@attr.s
class SMTwo:
    __quality = attr.ib(
        init=False,
        validator=[
            attr.validators.instance_of(int),
            attr.validators.in_(range(6))
        ],
        on_setattr=attr.setters.validate
    )
    __easiness = attr.ib(init=False)
    __interval = attr.ib(init=False)
    __repetitions = attr.ib(init=False)
    __review_date = attr.ib(init=False)
    __prev = attr.ib(init=False)

    @property
    def quality(self):
        return self.__quality

    @property
    def easiness(self):
        return self.__easiness

    @property
    def interval(self):
        return self.__interval

    @property
    def repetitions(self):
        return self.__repetitions

    @property
    def review_date(self):
        return self.__review_date

    @property
    def prev(self):
        return self.__prev

    @attr.s
    class Prev:
        __easiness = attr.ib(validator=attr.validators.instance_of(float))
        __interval = attr.ib(validator=attr.validators.instance_of(int))
        __repetitions = attr.ib(validator=attr.validators.instance_of(int))
        __review_date = attr.ib(validator=attr.validators.instance_of(date))

        @__easiness.validator
        def __check_valid_easiness(self, attribute, value):
            if value < 1.3:
                message = "easiness has a minimum value of 1.3"
                raise ValueError(message)

        @__interval.validator
        def __check_valid_interval(self, attribute, value):
            if value < 1:
                message = "interval has a minimum value of 1"
                raise ValueError(message)

        @__repetitions.validator
        def __check_valid_repetitions(self, attribute, value):
            if value < 1:
                message = "repetitions has a minimum value of 1"
                raise ValueError(message)

        @property
        def interval(self):
            return self.__interval

        @property
        def easiness(self):
            return self.__easiness

        @property
        def repetitions(self):
            return self.__repetitions

        @property
        def review_date(self):
            return self.__review_date

    def calc(self, quality, easiness, interval, repetitions, review_date):
        self.__quality = quality
        self.__prev = self.Prev(easiness, interval, repetitions, review_date)

        if quality < 3:
            self.__interval = 1
            self.__repetitions = 1
        else:
            if repetitions == 1:
                self.__interval = 1
            elif repetitions == 2:
                self.__interval = 6
            else:
                self.__interval = round(interval * easiness)

            self.__repetitions = repetitions + 1

        self.__easiness = easiness - 0.8 + 0.28 * quality - 0.02 * quality**2
        if self.__easiness < 1.3:
            self.__easiness = 1.3

        self.__review_date = review_date + timedelta(days=self.__interval)

    def json(self, prev=None, curr=None):
        try:
            attrs = {"quality": self.__quality}
            prev_attrs = {
                "prev_easiness": self.__prev.easiness,
                "prev_interval": self.__prev.interval,
                "prev_repetitions": self.__prev.repetitions,
                "prev_review_date": str(self.__prev.review_date)
            }
            cur_attrs = {
                "easiness": self.__easiness,
                "interval": self.__interval,
                "repetitions": self.__repetitions,
                "review_date": str(self.__review_date)
            }
        except AttributeError:
            raise CalcNotCalledYet

        if prev:
            add_from_dict(prev_attrs, attrs)
        elif curr:
            add_from_dict(cur_attrs, attrs)
        else:
            add_from_dict(prev_attrs, attrs)
            add_from_dict(cur_attrs, attrs)

        return json.dumps(attrs)

    def dict(self, prev=None, curr=None):
        try:
            attrs = {"quality": self.__quality}
            prev_attrs = {
                "prev_easiness": self.__prev.easiness,
                "prev_interval": self.__prev.interval,
                "prev_repetitions": self.__prev.repetitions,
                "prev_review_date": self.__prev.review_date
            }
            cur_attrs = {
                "easiness": self.__easiness,
                "interval": self.__interval,
                "repetitions": self.__repetitions,
                "review_date": self.__review_date
            }
        except AttributeError:
            raise CalcNotCalledYet

        if prev:
            add_from_dict(prev_attrs, attrs)
        elif curr:
            add_from_dict(cur_attrs, attrs)
        else:
            add_from_dict(prev_attrs, attrs)
            add_from_dict(cur_attrs, attrs)

        return attrs
