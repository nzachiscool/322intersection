import unittest
from main import Orientation

class TestMathFunctions(unittest.TestCase):
    def test_colinear(self):
        self.assertEqual(Orientation((1,1), (2,2), (3,3)), "Collinear")

    def test_counterclockwise(self):
        self.assertEqual(Orientation((1,1), (2,1), (2,2)), "Counter-clockwise")

    def test_clockwise(self):
        self.assertEqual(Orientation((1,1), (1,2), (2,2)), "Clockwise")

if __name__ == "__main__":
    unittest.main()