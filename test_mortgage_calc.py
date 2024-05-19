import unittest
from mortgage_calculation import mortgage_calc


class TestMortgageCalc(unittest.TestCase):
    def test_empty_cells(self):
        self.assertEqual(mortgage_calc("", "", "", "", "Y"), False)

    def test_initial_fee_more_than_price(self):
        self.assertEqual(mortgage_calc("70000", "100000", "10", "16", "Y"), (0, 0, 0, 0))

    def test_invalid_value(self):
        self.assertEqual(mortgage_calc("70000e+2", "100000e-2", "10", "16", "Y"), False)

    def test_term_equals_0(self):
        self.assertEqual(mortgage_calc("700000", "100000", "10", "0", "Y"), False)

    def test_percent_equals_0(self):
        self.assertEqual(mortgage_calc("700000", "100000", "0", "10", "Y"), False)

    def test_too_large_value(self):
        self.assertEqual(mortgage_calc("7000000", "100000", "1600000", "10", "Y"), False)

    def test_calculation(self):
        self.assertEqual(mortgage_calc("7000000", "100000", "16", "10", "Y"), (6900000, 115584, 6970086, 13870086))


if __name__ == "__main__":
    unittest.main()
