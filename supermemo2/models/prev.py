import json
import attr


@attr.s
class Prev:
    __sm_two_obj = attr.ib()
    __easiness = attr.ib()
    __interval = attr.ib()
    __repetitions = attr.ib()

    @property
    def easiness(self):
        return self.__easiness

    @property
    def interval(self):
        return self.__interval

    @property
    def repetitions(self):
        return self.__repetitions

    @repetitions.setter
    def repetitions(self, value):
        print('set prev rep')
        if self.__repetitions == 1:
            self.__sm_two_obj.interval = 1
        elif self.__repetitions == 2:
            self.__sm_two_obj.interval = 6
        else:
            # wrong, missing .interval
            self.__sm_two_obj = round(self.__interval * self.__easiness)

    def json(self):
        return json.dumps(
            {
                "easiness": self.easiness,
                "interval": self.interval,
                "repetitions": self.repetitions
            }
        )
