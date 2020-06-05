import unittest

from oop.day5.csv_exe import SheetCalculator


#
# class MockCsvReader:
#     def get_sheet(self):
#         return [
#             ['column1', 'column2', 'column3'],
#             [1, 2, 3],
#             ['X', 'Y', 'Z'],
#         ]
#
#
# mock_csv_reader = MockCsvReader()
# temp_sheet_calculator = SheetCalculator(mock_csv_reader)
# assert temp_sheet_calculator.get_row(2) == ['X', 'Y', 'Z']
# assert temp_sheet_calculator.get_row(1) == [1, 2, 3]
# assert temp_sheet_calculator.get_row(0) == ['column1', 'column2', 'column3']

# TEST SUITE
class TestSheetCalculator(unittest.TestCase):

    # TEST CASE
    def test_get_row(self):
        # GIVEN (dane wejściowe i spodziewany wynik)
        class MockCsvReader:
            def get_sheet(self):
                return [
                    ['column1', 'column2', 'column3'],
                    [1, 2, 3],
                    ['X', 'Y', 'Z'],
                ]

        mock_csv_reader = MockCsvReader()
        sheet_calculator = SheetCalculator(mock_csv_reader)
        expected_get_row_result_0 = ['column1', 'column2', 'column3']
        expected_get_row_result_1 = [1, 2, 3]
        expected_get_row_result_2 = ['X', 'Y', 'Z']

        # WHEN (operacja)
        get_row_result_0 = sheet_calculator.get_row(0)
        get_row_result_1 = sheet_calculator.get_row(1)
        get_row_result_2 = sheet_calculator.get_row(2)

        # THEN (assercia)
        self.assertEqual(get_row_result_0, expected_get_row_result_0)
        self.assertEqual(get_row_result_1, expected_get_row_result_1)
        self.assertEqual(get_row_result_2, expected_get_row_result_2)

    # TEST CASE
    def test_get_row_out_of_range(self):
        # GIVEN (dane wejściowe i spodziewany wynik)
        class MockCsvReader:
            def get_sheet(self):
                return [
                    ['column1', 'column2', 'column3'],
                ]

        mock_csv_reader = MockCsvReader()
        sheet_calculator = SheetCalculator(mock_csv_reader)

        # WHEN (operacja) $ THEN (assercia)
        with self.assertRaises(IndexError):
            get_row_result_2 = sheet_calculator.get_row(2)


# class IndexError(Exception):
#     pass