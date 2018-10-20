import unittest 
import math
import sincos

class SinCosTest(unittest.TestCase):
    def test_sincos(self):
        self.assertEqual(sincos.sin_cos((1.5 * math.pi), 0), 2.97)


if __name__ == '__main__':
    unittest.main()

