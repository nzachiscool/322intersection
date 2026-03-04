import unittest
from main import do_segments_intersect

class TestMathFunctions(unittest.TestCase):
    def test_basic_intersect(self):
        self.assertEqual(do_segments_intersect(((1.0, 1.0),(4.0, 4.0)), ((2.0, 4.0), (4.0, 2.0))), True)

    def test_colinear1(self):
        self.assertEqual(do_segments_intersect(((1.0, 1.0),(4.0, 4.0)), ((3.0, 3.0), (4.0, 2.0))), True)

    def test_colinear2(self):
        self.assertEqual(do_segments_intersect(((1.0, 1.0),(4.0, 4.0)), ((3.0, 3.0), (2.0, 2.0))), True)

    def test_colinear3(self):
        self.assertEqual(do_segments_intersect(((1.0, 1.0),(4.0, 4.0)), ((5.0, 5.0), (6.0, 6.0))), False)

    def test_same_segments(self): 
        self.assertEqual(do_segments_intersect(((1.0, 1.0),(4.0, 4.0)), ((1.0, 1.0), (4.0, 4.0))), True)
 
    def test_negative_points(self): 
        self.assertEqual(do_segments_intersect(((-1.0, -1.0),(4.0, 4.0)), ((2.0, 4.0), (4.0, 2.0))), True)
 

if __name__ == "__main__":
    unittest.main()