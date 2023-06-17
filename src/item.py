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
