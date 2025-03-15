"""
Lesson 26 - Наследование
- Концепция наследования
- Переопределение методов
- Расширение методов
- Вызов методов родительского класса
- Super()
- Работа с инициализаторами
"""

# 1. Концепция наследования
# Наследование - это механизм, который позволяет создать новый класс на основе уже существующего.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def voice(self):
        print(f'{self.__class__.__name__} по имени {self.name} издал(а) звук')

class Dog(Animal):
    # Пайтон ищет метод у собственного класса.
    # Тут мы переопределили метод voice() у класса Dog.
    # Теперь будет вызываться метод voice() у класса Dog а не у класса Animal.
    def voice(self):
        print(f'{self.__class__.__name__} по имени {self.name} начал(а) лаять')

class Cat(Animal):
    pass

dog = Dog('Барабос')
cat = Cat('Святомур')

dog.voice()  # Dog издало звук
cat.voice()  # Cat издало звук