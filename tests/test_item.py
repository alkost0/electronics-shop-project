import pytest
from src.item import Item

@pytest.fixture()
def item_name():
    return Item("Ноутбук", 50000, 2)

def test_item_init(item_name):
    '''Тест по атрибутам Класса (проверяем инит как первую функцию)'''
    assert item_name.price == 50000
    assert item_name.name == "Ноутбук"
    assert item_name.quantity == 2

def test_item_calculation(item_name):
    '''Тест по итоговой цене (проверяем вторую функцию)'''
    assert item_name.calculate_total_price() == 100000.0

def test_item_discount(item_name):
    '''Тест по скидке (проверяем третьюю функцию)'''
    item_name.pay_rate = 0.85
    item_name.apply_discount()
    assert item_name.price == 8500.0

def test_get_name(item_name):
    assert item_name.name == "Ноутбук"

def test_set_name(item_name):
    item_name.name = "НоутбукДеллВостро"
    assert item_name.name == "НоутбукДел"

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item_name1 = Item.all[0]
    assert item_name1.name == "Смартфон"
    item_name2 = Item.all[1]
    assert item_name2.name == "Ноутбук"

def test_string_to_number():
    Item.instantiate_from_csv()
    assert Item.string_to_number("2.2") == 2

def test_str(item_name):
    assert str(item_name) == "Ноутбук"

def test_repr(item_name):
    assert repr(item_name) == "Item('Ноутбук', 50000, 2)"
