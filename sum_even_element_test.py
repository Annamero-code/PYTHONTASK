import unittest
from sum_even_element import *
class sum_even_element_test(unittest.TestCase):
    def test_thatWhen_iSum_upThe_even_element_iGet_theTotal(self):
        lists = [6,6,8,9,3,4,2]
        expected_total = sum_even_element(lists)
        actual_total = 26
        self.assertEqual(expected_total,actual_total)
