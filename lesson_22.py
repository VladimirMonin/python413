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
    # Атрибут класса
    name = "Джон"


p1 = Person()
p2 = Person()

print(p1.name, p2.name)

p1.name = "Филлип"
p2.name = "Джордж"

print(p1.name, p2.name)
