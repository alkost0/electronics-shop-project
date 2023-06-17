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

