import unittest
from solution import Solution

class TestMinInterval(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        queries = [2, 3, 4, 5]
        expected = [3, 3, 1, 4]
        self.assertEqual(self.solution.minInterval(intervals, queries), expected)

    def test_single_query(self):
        intervals = [[1, 3], [2, 5], [4, 6]]
        queries = [3]
        expected = [3]
        self.assertEqual(self.solution.minInterval(intervals, queries), expected)

    def test_no_intervals(self):
        intervals = []
        queries = [1, 2, 3]
        expected = [-1, -1, -1]
        self.assertEqual(self.solution.minInterval(intervals, queries), expected)

    def test_no_valid_intervals(self):
        intervals = [[10, 15], [20, 25]]
        queries = [5, 30]
        expected = [-1, -1]
        self.assertEqual(self.solution.minInterval(intervals, queries), expected)

    def test_identical_intervals(self):
        intervals = [[1, 10], [1, 10], [1, 10]]
        queries = [1, 5, 10]
        expected = [10, 10, 10]
        self.assertEqual(self.solution.minInterval(intervals, queries), expected)

    def test_large_query(self):
        intervals = [[1, 3], [2, 5], [4, 7]]
        queries = [8]
        expected = [-1]
        self.assertEqual(self.solution.minInterval(intervals, queries), expected)

if __name__ == "__main__":
    unittest.main()
