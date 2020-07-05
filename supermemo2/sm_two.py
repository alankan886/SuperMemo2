import datetime

date_fmt = "%Y-%m-%d"

class SMTwo:
    def __init__(self, quality: int, prev_interval: int = 0, prev_repetitions: int = 0, prev_easiness: float = 2.5, first_visit: bool = False, last_review: datetime.date = datetime.date.today()):
        self.quality = quality
        self.prev_easiness = prev_easiness
        self.prev_interval = prev_interval
        self.prev_repetitions = prev_repetitions
        self.first_visit = first_visit
        self.last_review = last_review

        self.new_easiness = 0
        self.new_interval = 0
        self.new_repetitions = 0
        self.next_review = None

        self.new_sm_two()

    @staticmethod
    def set_str_to_date_type(string):
        return datetime.datetime.strptime(string, date_fmt).date()
    
    def new_sm_two(self) -> None:
        self.invalid_input_handler()

        if type(self.last_review) == str:
            self.last_review = self.set_str_to_date_type(self.last_review)

        if self.quality < 3:
            self.new_repetitions = 0
            self.new_interval = 1
            self.new_easiness = self.prev_easiness
        else:
            if self.prev_repetitions == 0:
                self.new_interval = 1
            elif self.prev_repetitions == 1:
                self.new_interval = 6
            else:
                self.new_interval = round(self.prev_interval * self.prev_easiness)

            self.new_repetitions = self.prev_repetitions + 1

            self.new_easiness = self.prev_easiness - 0.8 + 0.28 * self.quality - 0.02 * self.quality**2

        if self.new_easiness < 1.3:
            self.new_easiness = 1.3

        self.next_review = str( self.last_review + datetime.timedelta(days=self.new_interval))

    def json(self) -> dict:
        return {
            "next_review": self.next_review,
            "new_repetitions": self.new_repetitions,
            "new_easiness": self.new_easiness,
            "new_interval": self.new_interval
        }

    def invalid_input_handler(self):
        if self.first_visit:
            if type(self.prev_interval) != int:
                raise TypeError("Interval value should be an integer.")
            elif self.prev_interval != 0:
                raise ValueError("Interval value should be 0 if this is the very first time.")

            if type(self.prev_repetitions) != int:
                raise TypeError("Repetitions value should be an integer.")
            elif self.prev_repetitions != 0:
                raise ValueError("Repetitions value should be 0 if this is the very first time.")

            if type(self.prev_easiness) != float:
                raise TypeError("Easiness value should be a float.")
            elif self.prev_easiness != 2.5:
                raise ValueError("Easiness value should start off with 2.5 if this is the very first time.")
        else:
            if self.prev_easiness < 1.3:
                raise ValueError("Easiness value should not be smaller than 1.3!")

if __name__ == "__main__":
    sm_two = SMTwo(3)
    sm_two.last_review = "2020-07-05"
    sm_two.new_sm_two()