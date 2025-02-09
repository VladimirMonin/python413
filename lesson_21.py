"""
Тема: Функции Ч8. Генераторы. Генераторные выражения. Урок: 21
- Концепция ленивых вычислений
- Сравнение range в списке и вне
"""

START_VALUE = 0
END_VALUE = 1_000_000_000_000_000_000

# list_range = list(range(START_VALUE, END_VALUE))

range_object = range(START_VALUE, END_VALUE)
print(range_object, type(range_object))

for num in range_object:
    print(num)
