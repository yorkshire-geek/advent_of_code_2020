import unittest
from .exercise_5 import DataWrapper


class MyTestCase(unittest.TestCase):
    data_wrapper = DataWrapper("FBFBBFFRLR")

    def test_row_data(self):
        self.assertEqual("FBFBBFF", self.data_wrapper.get_row_str())

    def test_seat_data(self):
        self.assertEqual("RLR", self.data_wrapper.get_column_str())

    def test_row_binary(self):
        self.assertEqual("0101100", self.data_wrapper.get_row_binary())

    def test_column_binary(self):
        self.assertEqual("0101100", self.data_wrapper.get_row_binary())

    def test_row(self):
        self.assertEqual(44, self.data_wrapper.get_row())

    def test_column(self):
        self.assertEqual(5, self.data_wrapper.get_column())

    def test_id(self):
        self.assertEqual(357, self.data_wrapper.get_id())

    def test_one_two_three(self):
        self.assertEqual(567, DataWrapper("BFFFBBFRRR").get_id())
        self.assertEqual(119, DataWrapper("FFFBBBFRRR").get_id())
        self.assertEqual(820, DataWrapper("BBFFBBFRLL").get_id())


if __name__ == '__main__':
    unittest.main()
