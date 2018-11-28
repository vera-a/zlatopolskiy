import find_everything
import pdb
import unittest

class FindingEverything(unittest.TestCase):
    def test_finding_numbers(self):
        self.assertEqual(find_everything.get_everything(237), (23, 7, 12, 42))

if __name__ == '__main__':
    unittest.main()
