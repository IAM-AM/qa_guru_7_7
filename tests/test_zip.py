import zipfile
import os
from conftest import RESOURCE_ROOT_PATH
import shutil


def test_zip_file():
    file_path = os.path.join(RESOURCE_ROOT_PATH, "hello.zip")

    with zipfile.ZipFile(file_path) as hellozip:
        hellozip.extract('hello.txt')

        listname = hellozip.namelist()
        text = (hellozip.read('hello.txt').decode('utf-8'))
        print(text)

    assert file_path.endswith('.zip')
    assert os.path.isfile(file_path)
    assert listname == ['hello.txt']
    assert text == 'world'

    # os.remove(file_path)


test_zip_file()


def test_zip_file_archivation():
    tmp_dir = "tmp"
    os.makedirs(tmp_dir, exist_ok=True)

    tmp_path = os.path.join(tmp_dir, "new.zip")

    with zipfile.ZipFile(tmp_path, 'w') as zip_file:
        for file in [
            "docs-pytest-org-en-latest.pdf",
            "file_example_XLS_10.xls",
            "file_example_XLSX_50.xlsx"
        ]:
            file_path = os.path.join(RESOURCE_ROOT_PATH, file)
            zip_file.write(file_path, os.path.basename(file_path))

            assert file in zip_file.namelist()

        shutil.rmtree(tmp_dir)


test_zip_file_archivation()
