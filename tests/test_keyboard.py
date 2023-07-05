import pytest
from src.keyboard import Keyboard

@pytest.fixture()
def keyboard_name():
    return Keyboard("Chicony 100500", 5000, 20)

def test_str(keyboard_name):
    assert str(keyboard_name) == "Chicony 100500"
    assert str(keyboard_name.language) == "EN"

def test_repr(keyboard_name):
    assert repr(keyboard_name) == "Keyboard('Chicony 100500', 5000, 20)"

def test_change_lang(keyboard_name):
    keyboard_name.change_lang()
    assert str(keyboard_name.language) == "RU"
    keyboard_name.change_lang().change_lang()
    assert str(keyboard_name.language) == "RU"