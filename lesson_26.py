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
- Множественное и иерархическое наследование

"""

# Множественное наследование. Тут все ок. Стройная иерархия.

# class A:
#     def method_a(self):
#         print("Method A")


# class B:
#     def method_b(self):
#         print("Method B")


# class C(A, B):
#     def method_c(self):
#         print("Method C")

# print(C.__mro__)
# # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


# Множественное наследование

class A:
    def method_a(self):
        print("Method A")


class B(object):
    def method_b(self):
        print("Method B")


class C(A):
    def method_c(self):
        print("Method C")


class D(B):
    def method_d(self):
        print("Method D")


# А вот здесь начинается настоящий хаос, детка!
class X(C, D):
    pass


class Y(D, C):
    pass


# БАБАХ! Вот она, бомба замедленного действия!
class Z(X, Y):
    pass

# Эта строчка вызовет ошибку TypeError
print(Z.__mro__)