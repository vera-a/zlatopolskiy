import math
import in_meters
import unittest


class TestDistanceMeters (unittest.TestCase):
    def test_im_meters(self):
        self.assertEqual(in_meters.in_meters(786), 7)



if __name__ == '__main__':
    unittest.main()
