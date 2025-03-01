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
    
    def __validate_speed(self, speed: int):
        """
        Приватный метод-валидатор скорости.
        Проверяет, что скорость не отрицательная и не превышает максимальную.
        """
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        
        if speed > self.__max_speed:
            raise ValueError("Скорость не может быть больше максимальной")
    
    
    def set_speed(self, speed: int):
        """
        Публичный метод для установки скорости.
        Вызывает приватный метод-валидатор.
        """
        self.__validate_speed(speed)
        self._speed = speed


class Driver:
    def __init__(self, name: str, car: Car):
        self.name = name
        self.car = car

    def drive(self, speed: int):
        print(f"{self.name} сел в {self.car.model}")
        self.car.set_speed(speed)
        print(f"Скорость {self.car.model}: {self.car._speed}")


volga = Car("Volga", "black")
driver = Driver("Иосиф", volga)
driver.drive(100)
driver.drive(200)
driver.drive(300)