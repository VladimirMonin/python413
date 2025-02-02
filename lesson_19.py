"""
Python: Функции Ч6. Декораторы. Параметры декоратора. Урок: 19
pip install mypy
mypy file.py
"""
from typing import Callable, Any, List, Dict, Tuple, Set, Iterable, Union, Optional

# Стандартные аннотации типов
"""
str - строка
int - целое число
float - число с плавающей точкой
bool - булевое значение (True или False)
list - список
tuple - кортеж
dict - словарь
set - множество
None - нет значения

list[str] - список строк
set[int] - множество целых чисел
| - ИЛИ
"""

# Расширенные аннотации типов в Typing
"""
Any - любой тип данных
Callable - callable объект
Iterable - итерируемый объект
Union - объединение тиов - ИЛИ то или ЭТО
Optional - или ЭТО или None
Dict[[str|int], List[Union[str, None]]] - словарь, где ключи - строки, значения - список строк или целых чисел
Callable[[int, str], str] - функция, принимающая целое число и строку, и возвращающая строку
Iterable[str] - итерируемый объект, содержащий строки
Optional[int] - целое число или None
Union[int, float] - целое или число с плавающей точкой
"""



def simple_decorator(func: Callable):
    # func, message
    def wrapper():
        print(f'Печать до вызова.')
        result = func()
        print(f'Печать после вызова.')

        return result
    
    return wrapper
        

@simple_decorator
def foo():
    return f'Результат foo'

@simple_decorator
def foo66():
    return f'Функция 66'

print(foo())
print(foo())
print(foo())


def multiply(a: int, b: int) -> int:
    return a * b

def get_sum(num_list: List[int]) -> int:
    return sum(num_list)

print(multiply(5, 6))
print(multiply(5, "6"))

data_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_sum(data_set))

################# Декораторы #################

def simple_decorator2(func: Callable):
    # func, message
    def wrapper(a: int, b: int):
        print(f'Печать до вызова.')
        result = func(a, b)
        print(f'Печать после вызова.')

        return result
    
    return wrapper

@simple_decorator2
def multiply2(a: int, b: int) -> int:
    return a * b

@simple_decorator2
def multiply3(a: int, b: int, c: int) -> int:
    return a * b * c

multiply2(5, 6)
multiply3(5, 6, 7)
