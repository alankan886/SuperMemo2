import unittest
import json

from supermemo2 import SuperMemoTwo

class SM2Test(unittest.TestCase):
    def setUp(self):
        self.sm2 = SuperMemoTwo(0)

    def test_easiness_value_lowerbound(self):
        self.sm2.interval = 30
        self.sm2.repetitions = 6
        self.sm2.easiness = 1.3

        self.assertEqual(self.sm2.calc_new_easiness(), 1.3)