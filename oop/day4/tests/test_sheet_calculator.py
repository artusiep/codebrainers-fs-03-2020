import unittest

from oop.day4.csv_exe import SheetCalculator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # GIVEN (dane wejściowe do testu)
        class TempCsvReader:
            def get_sheet(self):
                return [['column1', 'column2', 'column3'],
                        [1, 2, 3]]
        temp_csv_reader = TempCsvReader()
        sheet_calculator = SheetCalculator(temp_csv_reader)
        expected_result = ['column1', 'column2', 'column3']

        # WHEN (operacja)
        result = sheet_calculator.get_row(0)

        # THEN (porównanie ze spodziewanym wynikiem)
        # assert result == expected_result
        self.assertEqual(result, expected_result)
