"""
08.02.2025
Тема: Функции Ч7. Анонимные функции. Map Filter Sorted. Урок: 20
- Функции высшего порядка
- Написали собственный my_map - чтобы разобрать как работает map
- Написали собственный my_filter - чтобы разобрать как работает filter
- Познакомились с lambda
- Посмотрели как работает lambda с фильтр
"""
# 1. Список чисел от пользователя
# 1.1 Цикл

# users_nums = input('Введите числа через пробел: ').split()

# nums_list = []

# for num in users_nums:
#     nums_list.append(int(num))


# 1.2 Списковое выражение
# nums_list = [int(num) for num in input('Введите числа через пробел: ').split()]

# 1.3 Map к списку строк
# users_nums = input('Введите числа через пробел: ').split()
# users_nums = list(map(int, users_nums))

# users_nums = list(map(lambda num: int(num) if num.isdigit() else None, users_nums))

from data.marvel import full_dict

full_list = [{"id": film_id, **film} for film_id, film in full_dict.items()]

# 2. Фильмы первой фазы
stage = "Первая фаза"

result = []

for film in full_list:
    if film['stage'] == stage:
        result.append(film)

# 2.1 Списковое выражение
first_stage = [film for film in full_list if film['stage'] == stage]

# 2.2 Filter
first_stage = list(filter(lambda film: film['stage'] == stage, full_list))

# 3. Фильмы 2018 года
films_2018 = [film for film in full_list if film['year'] == 2018]
films_2018 = list(filter(lambda film: film['year'] == 2018, full_list))

# 4. Фильмы после 2020 года
# films_after_2020 = [film for film in full_list if film['year'] > 2020]
# films_after_2020 = list(filter(lambda film: film['year'] > 2020, full_list))
# TypeError: '>' not supported between instances of 'str' and 'int'

# Нам надо проверить является ли это числом перед сравнением
films_after_2020 = [film for film in full_list if isinstance(film["year"], int) and film['year'] > 2020] 
films_after_2020 = list(filter(lambda film: isinstance(film["year"], int) and film['year'] > 2020, full_list))

from pprint import pprint
# pprint(films_after_2020)

# СОРТИРОВКА!
# list.sort() - метод списков
# key - необязательный параметр для сортировки ()
# reverse - необязательный параметр для сортировки по убыванию

participants = [
    "Владимир",
    "Олег",
    "Кирилл",
    "Алексей",
    "Александр",
    "Андрей",
    "Ильдар",
    "Андрей",
    "Никита",
    "Даши",
    "Сергей",
    "Максим",
    "Никита",
    "Анна",
    "Егор",
    "Елена"
]

participants.sort(key= lambda name: name[-1])
print(participants)

# 5. Сортировка full list по году и по названию

def film_sorter(film):
    title = film['title']
    year = film['year']

    title = title if title else "Без названия"
    year = year if isinstance(year, int) else 0
    return year, title

full_list.sort(key=film_sorter)
pprint(full_list)

full_list.sort(key=lambda film: (film['year'] if isinstance(film['year'], int) else 0, film['title'] if film['title'] else "Без названия"))


# SORTED - функция высшего порядка, возвращает генератор
# key - необязательный параметр для сортировки
# reverse - необязательный параметр для сортировки по убыванию

films = sorted(participants, reverse=True, key=len)
print(films)

film =  {
        'title': None,
        'year': 'TBA',
        'director': 'TBA',
        'screenwriter': 'Яссер Лестер',
        'producer': 'Кевин Файги и Джонатан Шварц',
}

print(dict(sorted(film.items())))
# в item будут заходить кортежи типа ("title", None)
print(dict(sorted(film.items(), key=lambda item: item[1] if item[1] else "")))

# Фильтрация по году а потом сортировка по названию
sorted_2023 = list(sorted(filter(lambda film: film["year"] == 2023, full_list), key=lambda film: film["title"]))
print(sorted_2023)