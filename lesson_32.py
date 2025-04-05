"""
Lesson 32 
05.04.2025
Порождаюющие паттерны проектирования
Паттерн Singleton

"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Экземпляр Singleton с значением: {self.value} и идентификатором: {id(self)}"
    

# Пример использования
singleton1 = Singleton(10)
singleton2 = Singleton(20)
print(singleton1)  # Экземпляр Singleton с значением: 10
print(singleton2)  # Экземпляр Singleton с значением: 10

# Экземпляр Singleton с значением: 20 и идентификатором: 1786903687056
# Экземпляр Singleton с значением: 20 и идентификатором: 1786903687056

