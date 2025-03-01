"""
Тема: ООП Ч3. Инкапсуляция. Приватные методы и атрибуты. Урок: 24
Два уровня сокрытия
_ это protected - досупно при наследовании
__ это private - доступно только внутри класса
"""

class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        self._speed = 0 # protected
        self.__max_speed = 200 # private

    def __str__(self):
        return f"Марка {self.model}, максимальная скорость {self.__max_speed}"

volga = Car("Volga", "black")
print(volga.model)
print(volga.color)
print(volga._speed)
# print(volga.__max_speed)
print(volga._Car__max_speed)

# AttributeError: 'Car' object has no attribute '__max_speed'. Did you mean: '_Car__max_speed'?
# Шаблон искажения имени _<ClassName>__<attributeName>
