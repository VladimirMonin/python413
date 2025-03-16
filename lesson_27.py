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
    def add_cheese_border(self):
        print("Сырный борт активирован!")

class ThinkCrustMixin:
    def add_thin_crust(self):
        print("Тонкое тесто активировано!")


######################
# 1. Нам нужна Пицца. Делаем экземпляр класса Pizza
# pizza = Pizza(30)

# 2. Нам нужна "мутация" - пицца с сырным бортом. Делаем экземпляр класса PizzaCheeseBorder

class PizzaCheeseBorder(Pizza, CheeseBorderMixin):
    def __init__(self, size: int):
        super().__init__(size)
        self.add_cheese_border()

# 3. Пирог с сырным бортом и тонким тестом
class PieCheeseBorderThinCrust(Pie, CheeseBorderMixin, ThinkCrustMixin):
    def __init__(self, size: int):
        super().__init__(size)


p = PieCheeseBorderThinCrust(30)
print(p.size)
p.add_cheese_border()
p.add_thin_crust()