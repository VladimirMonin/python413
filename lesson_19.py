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


ВАРИАНТЫ АННОТАЦИЙ ДЛЯ ДЕКОРАТОРОВ С ARGS/KWARGS:

1. Базовый вариант (любые аргументы, любой возврат):
def decorator(func: Callable[..., Any]) -> Callable[..., Any]

2. Строгая типизация конкретных аргументов:
def decorator(func: Callable[[int, str], bool]) -> Callable[[int, str], bool]

3. Смешанный вариант (известны типы позиционных аргументов):
def decorator(func: Callable[[int, str, ...], str]) -> Callable[[int, str, ...], str]

4. С указанием типов для kwargs:
def decorator(func: Callable[..., Dict[str, Any]]) -> Callable[..., Dict[str, Any]]

5. Комбинированный вариант:
def decorator(func: Callable[[int, str], Union[str, None]]) -> Callable[[int, str], Union[str, None]]

6. Для методов класса:
def decorator(func: Callable[[Any, ...], Any]) -> Callable[[Any, ...], Any]

7. Для асинхронных функций:
def decorator(func: Callable[..., Awaitable[Any]]) -> Callable[..., Awaitable[Any]]

8. С параметрами декоратора:
def param_decorator(param: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]

ВАЖНО: ... в Callable означает "любое количество аргументов любого типа"

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
# print(multiply(5, "6"))

data_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_sum(data_set))

################# Декораторы #################

def simple_decorator2(func: Callable[..., Any]) -> Callable[..., Any]:
    # func, message
    def wrapper(*args, **kwargs):
        print(f'Печать до вызова.')
        result = func(*args, **kwargs)
        print(f'Печать после вызова.')

        return result
    
    return wrapper

@simple_decorator2
def multiply2(a: int, b: int) -> int:
    return a * b

@simple_decorator2
def multiply3(a: int, b: int, c: int) -> int:
    return a * b * c

print(multiply2(5, 6))
print(multiply3(5, 6, 7))

# Напишем полезный декоратор. Который супер точно засекает время работы
# Любой функции и выводит время работы. Используем специальную функцию
# Из библиотеки time - perf_counter()

from time import perf_counter
from data.marvel import full_dict

def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'Время работы функции {func.__name__}: {end - start:.10f} секунд')
        return result
    return wrapper

# Декоратор печатающий какая функция работает (типа логирование)
def log_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        print(f'Вызывается функция {func.__name__} с аргументами {args} {kwargs}')
        result = func(*args, **kwargs)
        print(f'Функция {func.__name__} завершила работу с результатом {result}')
        return result
    return wrapper

@log_decorator # Этот враппер будет запущен первым
@timer_decorator # Первый закончит
def get_film_by_year(year: int) -> List[Dict[str, Any]]:
    return [film for film in full_dict.values() if film['year'] == year]
    
print(get_film_by_year(2008))
print(get_film_by_year(2019))

############ ДЕКОРАТОР С ПАРАМЕТРОМ ##################
"""
Декоратор проверяющий длину строки и выдающий ошибку если длина строки не соответствует параметру.
"""

def string_length_decorator(min_length: int) -> Callable:
    def decorator(func: Callable[[str], str]) -> Callable[[str], str]:
        def wrapper(name: str) -> str:
            if len(name) < min_length:
                raise ValueError(f'Строка {name} слишком короткая. Длина должна быть не менее {min_length} символов.')
            return func(name)
        return wrapper
    return decorator

@string_length_decorator(5)
def hello(name: str) -> str:
    return f'Привет, {name}!'

# print(hello('Жека'))
print(hello('Евгений!'))


while True:
    name = input('Введите ваше имя: ')
    try:
        print(hello(name))
    except ValueError as error:
        print(error)
