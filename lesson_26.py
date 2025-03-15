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
"""

# 1. Концепция наследования
# Наследование - это механизм, который позволяет создать новый класс на основе уже существующего.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def voice(self):
      return f'{self.__class__.__name__} по имени {self.name} издал(а) звук'

class Dog(Animal):
    # Пайтон ищет метод у собственного класса.
    # Тут мы переопределили метод voice() у класса Dog.
    # Теперь будет вызываться метод voice() у класса Dog а не у класса Animal.
    def voice(self):
        # Получим результат метода voice() у родительского класса через прямое обращение к нему.
        # result = Animal.voice(self)
        # super() - встроеенная функция, которая найдет родительский класс
        result = super().voice()
        return f'{result} и это было сделано собакой'

class Cat(Animal):
    pass

dog = Dog('Белка')
cat = Cat('Святомур')

print(dog.voice())  # Dog издало звук. И это было сделано собакой
print(cat.voice())  # Cat издало звук