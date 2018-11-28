import unittest 
import vice_versa

class TestViceVersa(unittest.TestCase):
    def test_vice_versa(self):
        self.assertEqual(vice_versa.vice_versa(43), (43, 34))


if __name__ == '__main__':
    unittest.main()

