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

# nonlocal
def foo():
    a = 3 # Local foo
    print(f'foo до вызова foo2 {a=}')

    def foo2():
        # Позволит перписать a из foo
        nonlocal a
        a = 4
        print(f'foo2 {a=}')

    foo2()
    print(f'foo после вызова foo2 {a=}')

foo()


bananas = print

bananas("Привет!")
bananas("Как дела?")

one = "1"
bir = one
odin = bir

print(odin)