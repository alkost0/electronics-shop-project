from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, quantity_of_sim):
        super().__init__(name, price, quantity)
        self.__quantity_of_sim = quantity_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity}, {self.quantity_of_sim})"

    @property
    def quantity_of_sim(self):
        return self.__quantity_of_sim

    @quantity_of_sim.setter
    def quantity_of_sim(self, quantity):
        if quantity <= 0:
            raise ValueError("Неверное количество SIM-карт, не натуральное число!")
        else:
            self.__quantity_of_sim = quantity
