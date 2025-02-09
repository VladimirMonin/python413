"""
Тема: Функции Ч8. Генераторы. Генераторные выражения. Урок: 21
- Концепция ленивых вычислений
- Сравнение range в списке и вне
"""
from typing import Generator
START_VALUE = 0
END_VALUE = 1_000_000_000_000_000_000

# list_range = list(range(START_VALUE, END_VALUE))

# range_object = range(START_VALUE, END_VALUE)
# print(range_object, type(range_object))

# for num in range_object:
#     print(num)

potatos = ["картошка", "картошка", "гнилая картошка", "картошка"]

def clean_potatos(potatos: list[str]) -> list[str]:
    new_potatos = []
    
    for potato in potatos:
        potato += "чищенная"
        new_potatos.append(potato)
    return new_potatos


cleaned_potatos = clean_potatos(potatos)
print(cleaned_potatos)

# Генераторные функции. Yield.
def generator_clean_potatos(potatos: list[str]) -> Generator[str]:
    for potato in potatos:
        potato += "_чищенная"
        yield potato

cleaned_potatos = generator_clean_potatos(potatos)
print(next(cleaned_potatos))
print(next(cleaned_potatos))
print(next(cleaned_potatos))
# StopIteration


for potato in cleaned_potatos:
    print(potato, "Из цикла")

for potato in generator_clean_potatos(potatos):
    print(potato, "Из цикла_2")