import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), 1)
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(arrs.get(["test", 1, 2], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -3, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -1), [3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1, -2), [])
        self.assertEqual(arrs.my_slice([-1, -2, -3], 0), [-1, -2, -3])
        self.assertEqual(arrs.my_slice([], ), [])
        self.assertEqual(arrs.my_slice([], 0, -1), [])
        self.assertEqual(arrs.my_slice([-6], -2), [-6])