import json
import warnings

import attr


@attr.s
class Prev:
    __sm_two_obj = attr.ib()
    __first_visit = attr.ib()
    __easiness = attr.ib()
    __interval = attr.ib(on_setattr=attr.setters.validate)
    __repetitions = attr.ib()

    @__interval.validator
    def _interval_value_check(self, attribute, value):
        print('called_vali')
        if self.__repetitions == 1 and value != 1:
            print(value)
            self.interval = 1
            warnings.warn("interval automatically set to 1, when repetition is 1, interval is always 1")
        elif self.__repetitions == 2 and value != 1:
            self.interval = 1
            warnings.warn("interval automatically set to 1, when repetition is 2, interval is always 1")
        
    @property
    def first_visit(self):
        return self.__first_visit

    @property
    def easiness(self):
        return self.__easiness

    @easiness.setter
    def easiness(self, value):
        self.__easiness = value
        # this will need to call calc_easiness later I think or depends on the quality
        if self.__sm_two_obj.quality < 3:
            self.__sm_two_obj.easiness = value
        else:
            self.__sm_two_obj.calc_easiness()

    @property
    def interval(self):
        return self.__interval

    @interval.setter
    def interval(self, value):
        print('called_prop')
        self.__interval = value
        print(self.__interval)
        # this will need to call calc_interval later I think

    @property
    def repetitions(self):
        return self.__repetitions

    @repetitions.setter
    def repetitions(self, value):
        if value == 1:
            self.__interval = 1
            # this is not the right equation
            # to update the SMTwo values, we can group the calculations in to different functions
            # and if changing interval affects A and B,
            # we call the function that calculates A and B here to update the value in SMTwo
            # also probably call attr.validate(self) to validate values again
            # or maybe use the attr.setter.validate on on_setattr (this is new and should work great)
        elif value == 2:
            self.__interval = 6

        self.__repetitions = value
        if self.__sm_two_obj.quality < 3:
            self.__sm_two_obj.repetitions = 1
        else:
            self.__sm_two_obj.calc_repetitions()
        
    def json(self):
        return json.dumps(
            {
                "easiness": self.easiness,
                "interval": self.interval,
                "repetitions": self.repetitions
            }
        )
