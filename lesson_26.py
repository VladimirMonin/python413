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
"""

# 1. Концепция наследования
# Наследование - это механизм, который позволяет создать новый класс на основе уже существующего.

class Animal:
    def __init__(self, name: str):
        self.name = name

    def voice(self):
      return f'{self.__class__.__name__} по имени {self.name} издал(а) звук'
    
    def __str__(self):
        return f'{self.__class__.__name__} по имени {self.name}'

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
    def __init__(self, name: str, fluffy_level: int):
        super().__init__(name)
        self.fluffy_level = self.__fluffy_validator(fluffy_level)

    def voice(self):
        return f'{super().voice()} и это было сделано кошкой'

    
    def __fluffy_validator(self, fluffy_level):
        if not 0 <= fluffy_level <= 10:
            raise ValueError('Fluffy level must be between 0 and 10')
        else:
            return fluffy_level

dog = Dog('Белка')
cat = Cat('Хитролап', 5)

print(dog.voice())  # Dog издало звук. И это было сделано собакой
print(cat.voice())  # Cat издало звук

# MRO - Method Resolution Order - Порядок разрешения методов
# Порядок разрешения методов - это порядок, в котором Python ищет методы в иерархии наследования.

# Получим это для Dog
print(Dog.__mro__)  # (<class '__main__.Dog'>, <class '__main__.Animal'>, <class 'object'>)

