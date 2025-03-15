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

# Иерархическое наследование - когда один класс наследует от нескольких классов
# Множественное наследование - когда один класс наследует от нескольких класс

class A:
    def __init__(self, a_param:str):
        self.a_param = a_param
    
    def method_a(self):
        print('Method A' + self.a_param)

class B(A):
    def __init__(self, a_param:str, b_param:str):
        super().__init__(a_param)
        self.b_param = b_param

    def method_b(self):
        print('Method B' + self.b_param)

class C(B):
    def __init__(self, a_param:str, b_param:str, c_param:str):
        super().__init__(a_param, b_param)
        self.c_param = c_param

    def method_c(self):
        print('Method C')

c = C('A', 'B', 'C')
c.method_a()
c.method_b()
c.method_c()



# Бабка - Жучка - Внучка - Репка

# Репка - базовый класс

# class Repka:
#     def __init__(self, weight):
#         self.weight = weight

#     def __str__(self):
#         return f'Репка весом {self.weight} кг'

#     def pull(self):
#         print('Тянут репку')


# # Бабка - класс наследник от Репка
# class Babka(Repka):
#     def __init__(self, weight, name):
#         super().__init__(weight)
#         self.name = name

#     def __str__(self):
#         return f'Бабка {self.name} весом {self.weight} кг'

#     def pull(self):
#         print('Бабка тянет репку')

# # Жучка - класс наследник от Репка
# class Zhuchka(Repka):
#     def __init__(self, weight, name):
#         super().__init__(weight)
#         self.name = name

#     def __str__(self):
#         return f'Жучка {self.name} весом {self.weight} кг'

#     def pull(self):
#         print('Жучка тянет репку')


# # 