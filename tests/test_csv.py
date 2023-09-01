import csv
import os.path
from conftest import RESOURCE_ROOT_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_csv_file():
    csv_path = os.path.join(RESOURCE_ROOT_PATH, 'test_csv.csv')

    names = [
        ['Bonny', 'Pavel', 'Peter'],
        ['Alex', 'Serj', 'Yana']
    ]

    with open(csv_path, "w", newline='') as file:
        csvwriter = csv.writer(file, delimiter=',')
        csvwriter.writerows(names)

    with open(csv_path) as file:
        csvreader = csv.reader(file)
        actual_names = [row for row in csvreader]

    assert actual_names == names, "Ожидаемые имена отсутствуют в списке"

    os.remove(os.path.abspath(csv_path))
