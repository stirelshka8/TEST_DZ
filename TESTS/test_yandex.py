from yandex import creating_directory

ETALON = '<Response [204]>'


def test_creating_directory():
    result = creating_directory()
    assert result in ETALON
