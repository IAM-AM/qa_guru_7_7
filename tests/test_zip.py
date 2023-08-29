import zipfile
import os
from conftest import RESOURCE_ROOT_PATH


def test_zip_file():
    file_path = os.path.join(RESOURCE_ROOT_PATH, "hello.zip")

    with zipfile.ZipFile(file_path) as hellozip:
        hellozip.extract('hello.txt')

        print(hellozip.namelist())
        text = hellozip.read('hello.txt')
        text = text.decode('utf-8')
        print(text)

    assert file_path.endswith('.zip')
    assert os.path.isfile(file_path)
    assert text == str('world')

    os.remove(file_path)
