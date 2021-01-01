class CalcNotCalledYet(Exception):
    def __init__(self, message="SMTwo.calc method is required to be called first"):
        self.message = message
        super().__init__(self.message)
