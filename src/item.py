import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        """
        self.name = name         #Название товара.
        self.price = price       #Цена за единицу товара.
        self.quantity = quantity #Количество товара в магазине.
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return float(self.price * self.quantity)


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price =  float(self.price * self.pay_rate)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_len):
        if len(name_len) > 10:
            # print(Exception('Длина наименования товара превышает 10 символов'))
            self.__name = name_len[:10]
        else:
            self.__name = name_len

    @classmethod
    def instantiate_from_csv(cls):
        Item.all = []
        with open("../src/items.csv") as csvfile:
            datas = csv.DictReader(csvfile)
            for data in datas:
                cls(data['name'], data['price'], data['quantity'])

    @staticmethod
    def string_to_number(line):
        number = int(float(line))
        return number

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception