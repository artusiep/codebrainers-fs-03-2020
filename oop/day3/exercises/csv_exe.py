import csv
from functools import reduce


class CsvReader:
    # __init__ wczytanie pliku csv poprzez podanie scieżki + stworzenie 2 pól _path, _sheet (2d list)
    # get_sheet zwórcenie sheeta
    def __init__(self, file_path):
        self._path = file_path
        with open(self._path) as file:
            csvreader = csv.reader(file)
            self._sheet = list(csvreader)[1:]

    def get_sheet(self):
        return self._sheet

    def get_path(self):  # encapsulation
        return self._path


csv_reader = CsvReader('data/data.csv')
print(csv_reader.get_path())
print(csv_reader.get_sheet())


class SheetCalculator:
    def __init__(self, csvreader):  # argumenty, pola klasy
        self.sheet = csvreader.get_sheet()
        print()

    def get_row(self, num):
        return self.sheet[num]

    def count_colum(self):
        return len(self.sheet[0])

    def get_column(self, col):
        return [x[col] for x in self.sheet]

    def count_row(self):
        return len(self.sheet[:])

    def sum_col(self, col):
        return reduce(lambda x1, x2: int(x1) + int(x2), self.get_column(col))

    def mul_sum(self, mul):
        return reduce(lambda x1, x2: int(x1) * int(x2), self.get_column(mul))

    def mean_column(self, mean):
        return self.sum_col(mean) / self.count_row()

    def apply_function_on_column(self, col_number, function):
        # print(type(col_number), type(function))
        return reduce(function, self.get_column(col_number))
    #  __init__ pobranie CsvReadera i wczytanie sheeta do własnego pola
    # get_column
    # get_row
    # count_column
    # count_row
    # sum_column
    # mul_column
    # mean_column
    # apply_function_on_column


sheetcalc = SheetCalculator(csv_reader)
print(sheetcalc.get_row(4))
print(sheetcalc.count_colum())
print(sheetcalc.get_column(6))
print(sheetcalc.count_row())
print(sheetcalc.sum_col(0))
print(sheetcalc.mul_sum(0))
print(sheetcalc.mean_column(0))
print(sheetcalc.apply_function_on_column(6, lambda x, y: int(x) + int(y)))
print(sheetcalc.apply_function_on_column(6, lambda x, y: int(y)))


def max(x, y):
    # print(type(x), type(x))
    if int(x) > int(y):
        return x
    else:
        return y

print(type(max))

print(sheetcalc.apply_function_on_column(0, max))
