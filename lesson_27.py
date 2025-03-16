"""
Тема: ООП Ч6. Наследование. Миксины. Практика Урок: 27
"""

# 1. Базовый класс Pizza

class Pizza:
    def __init__(self, size: int):
        self.size = size

class Pie:
    def __init__(self, size: int):
        self.size = size


class CheeseBorderMixin:
    def __init__(self, height: int):
        self.height = height

    def add_cheese_border(self):
        print(f'Сырный борт, высотой {self.height} мм активирован!')

class ThinkCrustMixin:
    def __init__(self, thickness: int):
        self.thickness = thickness
    def add_thin_crust(self):
        print(f'Тонкое тесто, толщиной {self.thickness} мм активировано!')


######################
# 1. Нам нужна Пицца. Делаем экземпляр класса Pizza
# pizza = Pizza(30)

# 2. Нам нужна "мутация" - пицца с сырным бортом. Делаем экземпляр класса PizzaCheeseBorder

class PizzaCheeseBorder(Pizza, CheeseBorderMixin):
    def __init__(self, size: int, height: int):
        Pizza.__init__(self, size)
        CheeseBorderMixin.__init__(self, height)