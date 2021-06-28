"""
Testing the code for different cases using unittest framework.


"""
import unittest
from challenge import cliChallenge

class TestChallenge(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(cliChallenge('2 + 5'), '7')
        self.assertEqual(cliChallenge("0 + 0"), "0")
        self.assertEqual(cliChallenge("-2 + 5"), "3")
        self.assertEqual(cliChallenge("2 + -5"), "-3")
        self.assertEqual(cliChallenge("1_1/2 + 3_1/2"), "5")
        self.assertEqual(cliChallenge("2_4/5 + 12_13/15"), "15_2/3")
        self.assertEqual(cliChallenge("  2_4/5  +   12_13/15  "), "15_2/3")
        self.assertEqual(cliChallenge(" 2_4/5  +  12_13/15 "), "15_2/3")        

    def test_subtraction(self):
        self.assertEqual(cliChallenge('2 - 5'), '-3')
        self.assertEqual(cliChallenge('  10 -  7 '), '3')
        self.assertEqual(cliChallenge('0 - 12/15'), '-12/15')
        self.assertEqual(cliChallenge(' 0 - 12/14 '), '-6/7')
        self.assertEqual(cliChallenge(' -1/4 - -1/2 '), '1/4')


    def test_division(self):
        self.assertEqual(cliChallenge(' 10 / 5'), '2')
        self.assertEqual(cliChallenge(' 100_1/15 / 20_15/17'), '4_4217/5325')
        self.assertEqual(cliChallenge(' 10 / 1/5'), '50')
        self.assertEqual(cliChallenge(' 10 / _/5'), False)

    def test_multiplication(self):
        self.assertEqual(cliChallenge(' 10 * 1/5'), '2')
        self.assertEqual(cliChallenge(' 10_1/5 * 1/5'), '2_1/25')
        self.assertEqual(cliChallenge(' 1005 * 250_115/166'), '251946_39/166')
        self.assertEqual(cliChallenge('10_1/5  *   1/5        '), '2_1/25')
    
    def test_misTypedFraction(self):
        self.assertFalse(cliChallenge(" 2_4/5+  12_13/15 "))
        self.assertFalse(cliChallenge(" 2_4/5  12_13/15 "))
        self.assertFalse(cliChallenge(" 2_4/5+12_13/15 "))
        self.assertFalse(cliChallenge(" 2_/5 +  12_13/ "))
        self.assertFalse(cliChallenge(" 2_4/5+  _13/15 "))
        
    def test_zeroCases(self):
        self.assertFalse(cliChallenge(" 2_4/5 /  0 "))
        self.assertFalse(cliChallenge(" 500 /  0/0 "))
        self.assertFalse(cliChallenge(" 5 *  /0 "))


    def test_negativeNumbers(self):
        self.assertEqual(cliChallenge(' 10 * -1/5'), '-2')
        self.assertEqual(cliChallenge(' -10 * -1/5'), '2')
        self.assertEqual(cliChallenge(' -10 + -5'), '-15')
        self.assertEqual(cliChallenge(' -10 / -5'), '2')

#DO NOT CHANGE
if __name__ == '__main__':
    unittest.main()