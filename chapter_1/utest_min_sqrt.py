import unittest 
import math 
import min_sqrt

class MinSqrRt(unittest.TestCase):
    def test_minsqrrt(self):
        self.assertEqual(min_sqrt.minusqrt(13, 9), -20.0)


if __name__ == '__main__':
    unittest.main()
