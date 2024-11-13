import unittest
from datetime import datetime

class TestStockVisualizerInputs(unittest.TestCase):
    def test_validate_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))
        self.assertTrue(validate_symbol("GOOGL"))
        self.assertFalse(validate_symbol("apple"))
        self.assertFalse(validate_symbol("AAPL123"))
        self.assertFalse(validate_symbol("TOOLONGSYMBOL"))

    def test_validate_chart_type(self):
        self.assertTrue(validate_chart_type("Line"))
        self.assertTrue(validate_chart_type("Bar"))
        self.assertFalse(validate_chart_type("Pie"))
        self.assertFalse(validate_chart_type("1"))

    def test_validate_time_series(self):
        self.assertTrue(validate_time_series("TIME_SERIES_DAILY"))
        self.assertTrue(validate_time_series("TIME_SERIES_WEEKLY"))
        self.assertTrue(validate_time_series("TIME_SERIES_MONTHLY"))
        self.assertFalse(validate_time_series("TIME_SERIES_YEARLY"))
        self.assertFalse(validate_time_series("DAILY"))

    def test_validate_date_input(self):
        self.assertTrue(validate_date_input("2023-01-01"))
        self.assertTrue(validate_date_input("2000-12-31"))
        self.assertFalse(validate_date_input("01-01-2023"))
        self.assertFalse(validate_date_input("2023/01/01"))
        self.assertFalse(validate_date_input("2023-13-01"))
        self.assertFalse(validate_date_input("2023-00-01"))
        self.assertFalse(validate_date_input("2023-01-32"))

    def test_date_range(self):
        start_date = datetime.strptime("2023-01-01", "%Y-%m-%d")
        end_date_valid = datetime.strptime("2023-01-02", "%Y-%m-%d")
        end_date_invalid = datetime.strptime("2022-12-31", "%Y-%m-%d")
        
        self.assertTrue(end_date_valid > start_date)
        
        self.assertFalse(end_date_invalid > start_date)

if __name__ == "__main__":
    unittest.main()
