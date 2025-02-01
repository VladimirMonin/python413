"""
Python: Функции Ч5. Области видимости. Замыкания. Декоратор. Урок: 18
- Области видимости в Python
"""

# Области видимости
# Built-in - встроенная - служебная область видимости Python
# - print() -len() -bool()

# Global - глобальная область видимости
# Все переменные, созданные вне функции, принадлежат глобальной области видимости

# Local - локальная область видимости функций
# Nonlocal - Не локальная область видимости (функция внутри функции)

# Python производит поиск "изнутри наружу".
# Global
# print = "банан"
# print("апельсин") # TypeError: 'str' object is not callable

# print(banana) # NameError: name 'banana' is not defined

a = 2 # Global

def foo():
    a = 3 # Local
    print(f'foo: {a=}')

def foo2():
    global a
    a = 4 # Local
    print(f'foo2: {a=}')

def foo3():
    print(f'foo3: {a=}')

print(a) # 2 global
foo() # 3 local
foo2()# 4 global
foo3() # 4 global
print(a) # 4 global