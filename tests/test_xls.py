import os
import xlrd
from conftest import RESOURCE_ROOT_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_xls_file():
    file_path = os.path.join(RESOURCE_ROOT_PATH, "file_example_XLS_10.xls")
    book = xlrd.open_workbook(file_path)

    sheet = book.sheet_by_index(0)

    print(f"Количество листов {book.nsheets}")
    print(f"Имена листов {book.sheet_names()}")
    print(f"Количество колонок {sheet.ncols}")
    print(f"Количество строк {sheet.nrows}")

    print(f"Пересечение строки и столбца {sheet.cell_value(rowx=4, colx=1)}")

    assert os.path.isfile(file_path)
    assert book.nsheets == 1
    assert book.sheet_names() == ['Sheet1']
    assert sheet.ncols == 8
    assert sheet.nrows == 10
    assert sheet.cell_value(rowx=4, colx=1) == "Kathleen"

    # for rx in range(sheet.nrows):
    #     print(sheet.row(rx))
