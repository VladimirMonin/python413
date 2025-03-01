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
        self.__speed = 0 # private
        self.__max_speed = 200 # private

    def __str__(self):
        return f"Марка {self.model}, максимальная скорость {self.__max_speed}"
    
    def __validate_speed(self, speed: int):
        """
        Приватный метод-валидатор скорости.
        Проверяет, что скорость не отрицательная и не превышает максимальную.
        """
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        
        if speed > self.__max_speed:
            raise ValueError("Скорость не может быть больше максимальной")
    
    @property
    def speed(self) -> int:
        """
        Публичный метод для получения скорости.
        """
        return self.__speed
    
    @speed.setter
    def speed(self, speed: int):
        """
        Публичный метод для установки скорости.
        Вызывает приватный метод-валидатор.
        """
        self.__validate_speed(speed)
        self.__speed = speed


    @speed.deleter
    def speed(self):
        self.__speed = 0


audi = Car("Audi", "red")
print(audi)
audi.speed = 100
print(audi.speed)
audi.speed = 200
print(audi.speed)
# audi.speed = 300
print(audi.speed)
# audi.speed = -100
print(audi.speed)
del audi.speed
print(audi.speed)
