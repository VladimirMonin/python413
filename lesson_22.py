"""
15.02.2025
Python: ООП. Ч1. Атрибуты и методы. Класс и экземпляр. Практика. Урок: 22
- class
- нейминг классов UpperCamelCase
- атрибут класса
- __init__ - инициализатор
- self - ссылка на экземпляр класса
"""

class Person:
    def __init__(self, name: str):
        self.name = name

    def say_my_name(self):
        print(f"Меня зовут {self.name}")

# Person.__init__() missing 1 required positional argument: 'name'
p1 = Person("Барак")
p2 = Person("Владимир")
p3 = Person("Дональд")

print(p1.name, p2.name, p3.name)
p1.say_my_name()
p2.say_my_name()
p3.say_my_name()

