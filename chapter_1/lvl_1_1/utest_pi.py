import unittest 
import pi

class PiTest(unittest.TestCase):
    def test_pi(self):
        self.assertEqual(pi.pi(), 3.14)

if __name__ == '__main__':
    unittest.main()

