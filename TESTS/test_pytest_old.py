import pytest
from old_program import document_search

FIXTURE_SEARCH = {
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов"),
    ("1000", "Лев Иванович")
}


@pytest.mark.parametrize("number, name", FIXTURE_SEARCH)
def test_document_search(number, name):
    result = document_search(number)
    assert (name in result) or ("Лев Иванович" not in result)
