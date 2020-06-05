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


class TestSheetCalculator(unittest.TestCase):
    def test_get_row(self):
        class MockCsvReader:
            def get_sheet(self):
                return [
                    ['column1', 'column2', 'column3'],
                    [1, 2, 3],
                    ['X', 'Y', 'Z'],
                ]
        mock_csv_reader = MockCsvReader()
        sheet_calculator = SheetCalculator(mock_csv_reader)

        get_row_result_2 = sheet_calculator.get_row(2)
        get_row_result_1 = sheet_calculator.get_row(1)
        get_row_result_0 = sheet_calculator.get_row(0)

        print(get_row_result_0)
        self.assertEqual(get_row_result_0, ['column1', 'column2', 'column3'])


