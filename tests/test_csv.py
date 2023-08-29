import csv
import os.path
from tests.conftest import PROJECT_ROOT_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_csv_file():
    csv_path = os.path.join(PROJECT_ROOT_PATH, 'test_csv.py')
    names = [
        ['Bonny', 'Pavel', 'Peter'],
        ['Alex', 'Serj', 'Yana']
    ]
    try:
        with open(csv_path, "w") as file:
            csvwriter = csv.writer(file, delimiter=',')
            csvwriter.writerows(names)

        with open(csv_path) as file:
            csvreader = csv.reader(file)
            actual_names = [row for row in csvreader]

        assert actual_names == names, "Ожидаемые имена отсутствуют в списке"
        assert os.path.exists(csv_path)

    finally:
        if os.path.exists(csv_path):
            os.remove(csv_path)
