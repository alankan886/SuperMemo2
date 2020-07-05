import unittest
import json
import datetime

from supermemo2 import SMTwo

class SM2Test(unittest.TestCase):
    def setUp(self):
        self.sm_two = SMTwo(quality=0)

    def test_easiness_value_lowerbound(self):
        self.sm_two.quality = 3
        self.sm_two.interval = 30
        self.sm_two.repetitions = 6
        self.sm_two.easiness = 1.3

        self.sm_two.new_sm_two()

        self.assertEqual(self.sm_two.new_easiness, 1.3)
    
    def test_covert_last_review_str_to_date(self):
        self.sm_two.last_review = "2020-07-05"
        self.sm_two.new_sm_two()

        self.assertEqual(type(self.sm_two.last_review), datetime.date)