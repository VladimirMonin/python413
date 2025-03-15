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
    def __init__(self, file_path:str, encoding:str="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

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
    
    def read(self)-> list[str]:
        with open(self.file_path, "r", encoding=self.encoding) as file:
            clear_data = [string.strip() for string in file.readlines()]
            return clear_data

    def write(self, *data: str) -> None:
        with open(self.file_path, "w", encoding=self.encoding) as file:
            write_data = "\n".join(data)
            file.write(write_data)

    def append(self, *data: str) -> None:
        with open(self.file_path, "a", encoding=self.encoding) as file:
            write_data = "\n".join(data)
            file.write(write_data)


document = TextDocument("test.txt")
document.write("Привет", "Мир")
print(document.read())