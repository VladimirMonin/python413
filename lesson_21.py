"""
Тема: Функции Ч8. Генераторы. Генераторные выражения. Урок: 21
- Концепция ленивых вычислений
- Сравнение range в списке и вне
"""
from typing import Generator
START_VALUE = 0
END_VALUE = 1_000_000_000_000_000_000

range_obj = range(START_VALUE, END_VALUE)

# Помещаем это в фильтр для получения только четных чисел. Получаем объект фильтра
even_numbers = filter(lambda x: x % 2 == 0, range_obj)

# Получаем map объект из even_numbers и превращаем числа в строки и добавляем число
even_numbers_str = map(lambda x: f"Число: {x}", even_numbers)

for num in even_numbers_str:
    print(num)
