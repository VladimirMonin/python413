"""
Тема: ООП Ч6. Наследование. Миксины. Практика Урок: 27
"""

# 1. Базовый класс Pizza

class Pizza:
    def __init__(self, **kwargs):
        self.size = kwargs.pop('size', 30)
        super().__init__(**kwargs)

class Pie:
    def __init__(self, **kwargs):
        self.size = kwargs.pop('size', 30)
        super().__init__(**kwargs)


class CheeseBorderMixin:
    def __init__(self, **kwargs):
        self.height = kwargs.pop('height', 10)

    def add_cheese_border(self):
        print(f'Сырный борт, высотой {self.height} мм активирован!')

class ThinkCrustMixin:
    def __init__(self, **kwargs):
        self.thickness = kwargs.pop('thickness', 1)
    
    def add_thin_crust(self):
        print(f'Тонкое тесто, толщиной {self.thickness} мм активировано!')


######################
# Пицца с сырным бортом
class CheeseBorderPizza(Pizza, CheeseBorderMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_cheese_border()


# Тест
print('Пицца с сырным бортом')
pizza = CheeseBorderPizza(size=40, height=20)
print(pizza.size)
print(pizza.height)
print(pizza.__dict__)