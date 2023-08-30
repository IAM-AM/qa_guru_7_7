import os.path
import pypdf
from conftest import RESOURCE_ROOT_PATH


def test_pdf_file():
    file_path = os.path.join(RESOURCE_ROOT_PATH, "docs-pytest-org-en-latest.pdf")
    reader = pypdf.PdfReader(file_path)

    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    text = first_page.extract_text()

    count = 0

    for image_file in first_page.images:
        with open(os.path.join(RESOURCE_ROOT_PATH, str(count) + image_file.name), 'wb') as fp:
            fp.write(image_file.data)
            img_path = os.path.join(RESOURCE_ROOT_PATH, str(count) + image_file.name)
            count += 1

    assert number_of_pages == 412
    assert (text ==
            'pytest Documentation\n'
            'Release 0.1\n'
            'holger krekel, trainer and consultant, https://merlinux.eu/\n'
            'Jul 14, 2022')
    assert os.path.isfile(file_path)
    assert count == 1
    assert file_path.endswith('.pdf')

    os.remove(os.path.abspath(img_path))