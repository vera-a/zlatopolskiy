import unittest 
import number

class TestNumber(unittest.TestCase):
    def test_number(self):
        self.assertEqual(number.return_num(7), 7)

if __name__ == '__main__':
    unittest.main()
