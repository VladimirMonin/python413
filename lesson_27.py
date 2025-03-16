"""
Тема: ООП Ч6. Наследование. Миксины. Практика Урок: 27
"""

# 1. Базовый класс Pizza

class Pizza:
    def __init__(self, **kwargs):
        self.size = kwargs.get('size', 30)

class Pie:
    def __init__(self, **kwargs):
        self.size = kwargs.get('size', 30)


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
# Пицца с сырным бортом
class CheeseBorderPizza(Pizza, CheeseBorderMixin):
    def __init__(self, **kwargs):
        Pizza.__init__(self, **kwargs)
        CheeseBorderMixin.__init__(self, height=kwargs.get('height', 10))

    def make_pizza(self):
        print(f'Пицца с сырным бортом, размером {self.size} см готова!')
        self.add_cheese_border()