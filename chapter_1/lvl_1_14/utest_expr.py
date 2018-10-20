import unittest

import math

import math_expr

class TestMathExpression(unittest.TestCase):
    def test_math_expr(self):
        self.assertEqual(math_expr.squareroot(2, 8), 8)

if __name__ == '__main__':
    unittest.main()
