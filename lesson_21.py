"""
Тема: Функции Ч8. Генераторы. Генераторные выражения. Урок: 21
- Концепция ленивых вычислений
- Сравнение range в списке и вне
"""

from pprint import pprint
from typing import Generator
from urllib import response
from data.cities import cities_list

print(len(cities_list))
pprint(sorted(cities_list, key=lambda x: x["population"], reverse=True)[:5])

# Получим названия городов несколькими способами

# 1. Классика. Цикл
cities = []
for city in cities_list:
    cities.append(city["name"])

# 2. Списковое выражение
cities = [city["name"] for city in cities_list]

# 3. Генераторная функция


def get_cities_gen(cities: list[dict]) -> Generator[str]:
    for city in cities:
        yield city["name"]


cities_gen = get_cities_gen(cities_list)

# 4. Генераторное выражение

cities_gen = (city["name"] for city in cities_list)
# 5. Поместим это в фильтр - нужны города начинающиеся на Й
# filtered_cities = (city["name"] for city in cities_list if city["name"].startswith("Ш"))

# for city in filtered_cities:
#     print(city)

# 5. В ленивом режиме запишем имена в cities.txt
file_name = "cities.txt"

with open(file_name, "w", encoding="utf-8") as f:
    for city in cities_gen:
        f.write(f"{city}\n")


# Построчное чтение - возвращаем генератор
# with open(file_name, "r", encoding="utf-8") as f:
#     # for line in f:
#     #     print(line.strip())
#     cities = (line.strip() for line in f)

#     # Получим города где есть тире
#     filtered_cities = (city for city in cities if "-" in city)


def read_file_lines(filename: str) -> Generator[str]:
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()


cities = read_file_lines(file_name)

for city in cities:
    print(city)


# // https://api.openweathermap.org/data/2.5/weather?q=Усть-Каменогорск&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru

cities_list = ["Бангкок", "Сеул", "Токио", "Усть-Каменогорск", "Барнаул", "Москва"]

# pip install requests
import requests

# Тестирую гет запрос
response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q=Усть-Каменогорск&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru"
)
pprint(response.json())

# 1. Функция которая примет город и вернет погоду по нему temp и feelslike

def get_weather(city: str) -> str:
    # Базовый url API
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Параметры GET запроса
    params = {
        "q": city,
        "appid": "23496c2a58b99648af590ee8a29c5348",
        "units": "metric",
        "lang": "ru",
    }

    # Сам запрос. 
    response = requests.get(url, params=params)
    data = response.json()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    return f"Город: {city}, Температура: {temp}°C, ощущается как {feels_like}°C"

# for city in cities_list:
#     print(get_weather(city))


# Это же, на генераторе
def get_weather_gen(cities: list[str]) -> Generator[str]:
    for city in cities:
        yield get_weather(city)

for weather in get_weather_gen(cities_list):
    print(weather)