"""
08.02.2025
Тема: Функции Ч7. Анонимные функции. Map Filter Sorted. Урок: 20
- Функции высшего порядка
"""
from typing import Callable, Iterable, Union, Any, List, Tuple, Set
# Функция может принемать функцию

def my_map(func: Callable, data: Union[List, Tuple, Set]) -> List[Any]:
    result = []

    for item in data:
        result.append(func(item))
    
    return result

potatos = ["картошка", "картошка", "гнилая_картошка", "картошка", "гнилая_ картошка", "картошка"]

def clean_potato(potato: str) -> str:
    return potato + "_очищенная"

cleaned_potatos = my_map(clean_potato, potatos)
print(cleaned_potatos)

# используем встроеный map
cleaned_potatos_2 = list(map(clean_potato, potatos)) # list( <map object at 0x00000276552F9B10> )
print(cleaned_potatos_2)

# ФИЛЬТР

def my_filtr(func: Callable, data: Iterable) -> List:
    result = []

    for item in data:
        if func(item):
            result.append(item)
    
    return result

def is_bad_wegetable(wegetable: str) -> bool:
    return "гнил" in wegetable.lower()

bad_potatos = my_filtr(is_bad_wegetable, potatos)
print(bad_potatos)

# используем встроеный filter
bad_potatos_2 = list(filter(is_bad_wegetable, potatos)) # <filter object at 0x000001B43843B550>
print(bad_potatos_2)