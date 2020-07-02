import datetime

date_fmt = "%Y-%m-%d"

class SuperMemoTwo:
    def __init__(self, quality: int, interval: int = 0, repetitions: int = 0, easiness: float = 2.5, first_visit: bool = False, last_review: datetime.date = datetime.date.today()):
        self.easiness = easiness
        self.quality = quality
        self.first_visit = first_visit
        self.interval = interval
        self.repetitions = repetitions
        self.last_review = last_review

        if self.first_visit:
            if type(self.interval) != int:
                raise TypeError("Interval value should be an integer.")
            elif self.interval != 0:
                raise ValueError("Interval value should be 0 if this is the very first time.")

            if type(self.repetitions) != int:
                raise TypeError("Repetitions value should be an integer.")
            elif self.repetitions != 0:
                raise ValueError("Repetitions value should be 0 if this is the very first time.")

            if type(self.easiness) != float:
                raise TypeError("Easiness value should be a float.")
            elif self.easiness != 2.5:
                raise ValueError("Easiness value should start off with 2.5 if this is the very first time.")
        else:
            if self.easiness < 1.3:
                raise ValueError("Easiness value should not be smaller than 1.3!")
        
        if type(self.last_review) == str:
            self.last_review = datetime.datetime.strptime(self.last_review, date_fmt).date()

    def json(self):
        return {
            "next_review": self.next_review_date(),
            "new_repetitions": self.calc_new_repetitions(),
            "new_easiness": self.calc_new_easiness(),
            "new_interval": self.calc_new_interval(),
            "first_visit": False
        }
    
    def is_first_visit(self):
        return self.first_visit

    def calc_new_repetitions(self):
        # I might do like depending whether it's 0, 1 or 3, the repetition might reset differently.
        # The rule mentioned the reset can be I(1) or I(2), aka interval= 1 or 6
        if self.quality < 3:
            return 0
        
        return self.repetitions + 1

    def calc_new_easiness(self):
        potential_new_easiness = self.easiness - 0.8 + 0.28 * self.quality - 0.02 * self.quality**2
        new_easiness = max(1.3, potential_new_easiness)
        
        return new_easiness

    def calc_new_interval(self):
        if self.repetitions == 0:
            new_interval = 6
        elif self.repetitions == 1:
            new_interval = 6
        else:
            new_interval = self.interval * self.easiness
        
        return round(new_interval)
    
    def next_review_date(self):
        return self.last_review + datetime.timedelta(days=self.calc_new_interval())



if "__main__" == __name__:
    sm2 = SuperMemoTwo(4, first_visit=True)
    print(sm2.next_review_date())

    next_sm2 = SuperMemoTwo(5, sm2.calc_new_interval(), sm2.calc_new_repetitions(), sm2.calc_new_easiness(), last_review="2020-07-08")
    print(next_sm2.next_review_date())
    print(next_sm2.calc_new_easiness())

    next_next_sm2 = SuperMemoTwo(5, next_sm2.calc_new_interval(), next_sm2.calc_new_repetitions(), 3.6, last_review="2020-07-14")
    print(next_next_sm2.next_review_date())
    print(next_next_sm2.calc_new_easiness())
    print(next_next_sm2.json())
        

    