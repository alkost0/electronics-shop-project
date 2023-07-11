import pytest
from src.item import Item
from src.phone import Phone
from src.instantiate import InstantiateCSVError

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
    '''Тест на подтягивание имени'''
    assert item_name.name == "Ноутбук"

def test_set_name(item_name):
    '''Тест сеттера по имени айтема'''
    item_name.name = "НоутбукДеллВостро"
    assert item_name.name == "НоутбукДел"

def test_instantiate_from_csv():
    '''Тест по скидке (проверяем третьюю функцию)'''
    Item.instantiate_from_csv()
    item_name1 = Item.all[0]
    assert item_name1.name == "Смартфон"
    item_name2 = Item.all[1]
    assert item_name2.name == "Ноутбук"

def test_instantiate_from_csv_instantiate_error():
    '''Тест на повреждение (внутри другой порядок) файла при работе с исключениями'''
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()

def test_instantiate_from_csv_found_error():
    '''Тест на отсутствие файла при работе с исключениями'''
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()

def test_string_to_number():
    '''Тест преобразования строки в число'''
    Item.instantiate_from_csv()
    assert Item.string_to_number("2.2") == 2

def test_str(item_name):
    '''Тест дандер-метода стринг для строк'''
    assert str(item_name) == "Смартфон"

def test_repr(item_name):
    '''Тест дандер-метода репр'''
    assert repr(item_name) == "Item('HuaweiP100', 10000, 10)"

def test_add(item_name):
    '''Тест на добавление айтема и их сложение через дандер-метод'''
    Phone_2 = Phone("Samsung_Dual_Sim", 30000, 5, 2)
    assert item_name + Phone_2 == 25
    assert item_name + item_name == 20