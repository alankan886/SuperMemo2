from datetime import date, timedelta

import attr


@attr.s
class SMTwo:
    # the default none might have conflict with the validator on type later
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
    __last_review = attr.ib(init=False, validator=attr.validators.instance_of(date))
    __next_review = attr.ib(init=False)
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
    def last_review(self):
        return self.__last_review

    @property
    def next_review(self):
        return self.__next_review

    @property
    def prev(self):
        return self.__prev

    @attr.s
    class Prev:
        # need validation checks
        __easiness = attr.ib(validator=attr.validators.instance_of(float))
        __interval = attr.ib(validator=attr.validators.instance_of(int))
        __repetitions = attr.ib(validator=attr.validators.instance_of(int))

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

    def calc(self, quality, easiness, interval, repetitions, last_review):
        self.__quality = quality
        self.__prev = self.Prev(easiness, interval, repetitions)
        self.__last_review = last_review

        if quality < 3:
            self.__easiness = easiness
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

        self.__next_review = last_review + timedelta(days=self.__interval)
        # make sure if quality is less than 4, set next_review date to today

    def json(self):
        pass

    def dict(self):
        pass
