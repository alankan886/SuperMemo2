import datetime

date_fmt = "%Y-%m-%d"

class SMTwo:
    def __init__(self, quality: int, interval: int = 0, repetitions: int = 1, easiness: float = 2.5, first_visit: bool = False, last_review: datetime.date = datetime.date.today()):
        self.quality = quality
        self.easiness = easiness
        self.interval = interval
        self.repetitions = repetitions
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
            try:
                self.last_review = self.set_str_to_date_type(self.last_review)
            except:
                raise ValueError("The date format should be year-month-day, i.e. 2020-07-14.")
        elif type(self.last_review) != datetime.date:
            raise TypeError
        

        if self.quality < 3:
            self.new_repetitions = 1
            self.new_interval = 1
            self.new_easiness = self.easiness
        else:
            if self.repetitions == 1:
                self.new_interval = 1
            elif self.repetitions == 2:
                self.new_interval = 6
            else:
                self.new_interval = round(self.interval * self.easiness)

            self.new_repetitions = self.repetitions + 1

            self.new_easiness = self.easiness - 0.8 + 0.28 * self.quality - 0.02 * self.quality**2

        if self.new_easiness < 1.3:
            self.new_easiness = 1.3

        self.next_review = str(self.last_review + datetime.timedelta(days=self.new_interval))

    def json(self) -> dict:
        return {
            "next_review": self.next_review,
            "new_repetitions": self.new_repetitions,
            "new_easiness": self.new_easiness,
            "new_interval": self.new_interval
        }

    def invalid_input_handler(self):
        # Error check for when repetitions is 1, the previous interval must be 1
        if self.first_visit:
            if self.interval != 0 and type(self.interval) == int:
                raise ValueError("Interval value should be 0 if this is the very first time.")

            if self.repetitions != 1 and type(self.repetitions) == int:
                raise ValueError("Repetitions value should be 1 if this is the very first time.")
            
            if self.easiness != 2.5 and type(self.easiness) == float:
                raise ValueError("Easiness value should start off with 2.5 if this is the very first time.")
        
        if type(self.interval) != int:
            raise TypeError("Interval value should be an integer.")

        if type(self.repetitions) != int:
            raise TypeError("Repetitions value should be an integer.")

        if type(self.easiness) != float:
            raise TypeError("Easiness value should be a float.")
        
        if type(self.first_visit) != bool:
            raise TypeError("First visit should be a boolean value.")

        if type(self.quality) != int:
            raise TypeError("Quality value should be an integer.")

        if self.quality < 0 or self.quality > 5:
            raise ValueError("Quality value is on a scale of 0 to 5.")
        
        if self.easiness < 1.3:
            raise ValueError("Easiness value should not be smaller than 1.3!")
