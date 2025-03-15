"""
Lesson 26 - Наследование
- Концепция наследования
- Как называются родительские классы и наследники
- Базовый класс и производный класс
- Родительский класс и дочерний класс
- Superclass и subclass

- Переопределение методов
- Расширение методов
- Вызов методов родительского класса
- Super()
- Работа с инициализаторами
- MRO - Method Resolution Order
- Type vs Isinstance
- Абстрактные классы и методы
- Модуль ABC - Abstract Base Classes
- Декоратор @abstractmethod
"""

from abc import ABC, abstractmethod

class AbstractDocument(ABC):
    def __init__(self, file_path:str):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def append(self):
        pass

    def __str__(self):
        return f"Документ типа {self.__class__.__name__} по пути {self.file_path}"
    

class TextDocument(AbstractDocument):
    pass

# instantiate abstract class TextDocument without an implementation for abstract metho
td = TextDocument("text.txt")