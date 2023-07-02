import pytest
from src.item import Item
from src.phone import Phone

@pytest.fixture()
def phone_name():
    return Phone("Samsung_Dual_Sim", 30000, 5, 2)

def test_init(phone_name):
    assert phone_name.name == "Samsung_Dual_Sim"
    assert phone_name.price == 30000
    assert phone_name.quantity == 5
    assert phone_name.number_of_sim == 2

def test_repr(phone_name):
    assert repr(phone_name) == "Phone('Samsung_Dual_Sim', 30000, 5, 2)"

def test_str(phone_name):
    assert str(phone_name) == "Samsung_Dual_Sim"

def test_add(phone_name):
    item_name = Item("Смартфон", 10000, 20)
    assert item_name + phone_name == 25
    assert phone_name + phone_name == 10
    assert phone_name + 10 == Exception

def test_number_of_sim_setter(phone_name):
    phone_name.number_of_sim = 2
    assert phone_name.number_of_sim == 2
    phone_name.number_of_sim = 0
    assert phone_name.number_of_sim == ValueError("Неверное количество SIM-карт, не натуральное число!")
    phone_name.number_of_sim = -1
    assert phone_name.number_of_sim == ValueError("Неверное количество SIM-карт, не натуральное число!")

def test_number_of_sim_getter(phone_name):
    assert phone_name.number_of_sim == 2