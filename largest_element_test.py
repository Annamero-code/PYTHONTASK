import unittest
from largest_element import *
class largest_element_test(unittest.TestCase):
    def test_thatWhen_iEnterList_ofNumber_iGetThe_largest(self):
        lists = [5,8,97,6,4,5,]
        expected_answer = largest_element(lists)
        actual_answer = 97
        self.assertEqual(expected_answer,actual_answer)

