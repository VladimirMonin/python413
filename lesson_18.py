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


# nonlocal
def foo(a: str):
    # a - local для foo
    def foo2():
        return a
    return foo2

f2 = foo("апельсин")
f3 = foo("банан")

orange = f2() # Замыкание.
banan = f3()

print(orange)
print(banan)

# f2 -> foo2 -> "апельсин" (local a)

# Счечтик который помнит своё состояние. И может принять стартовую позицию.

def counter(start: int = 0, step: int = 1):

    position = start

    def tik():
        nonlocal position
        position += step
        return position
    
    return tik

counter_0_2 = counter(0, 2)
print(counter_0_2())
print(counter_0_2())
print(counter_0_2())
print(counter_0_2())


product_list = ["морковь", "картошка", "чеснок", "говядина", "коньяк"]

# Функция с кешированием результатов вызова на примере сортировщика

def product_sort(products: list):
    # тут будет хранится products
    cach = []

    def sorter():
        nonlocal cach
        if cach and len(cach) == len(products):
            return cach
        
        cach = sorted(products)
        return cach

    return sorter

product_sorter = product_sort(product_list)
print(product_sorter())
print(product_sorter())

product_list.append("капуста")
print(product_sorter())
print(product_sorter())