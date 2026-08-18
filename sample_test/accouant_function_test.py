#import unittest
#from unittest import TestCase
#
#
#
#class AccountTest(unittest.TestCase):
#
#    def test_sample(self):
#        result = 15
#        first_number = 10
#        second_number = 5
#        summation = first_number + second_number
#        self.assertTrue(summation == result)
#        self.assertEqual(summation,result)
#        
        
        
        
        
from unittest import TestCase
from account_function import check_balance        
class AccountTest(TestCase):
    def test_accountBalance_isZero_duringCreation(self):
        expected_balance = 0
        actual_balance = check_balance() 
        self.assertEqual(actual_balance,expected_balance)
