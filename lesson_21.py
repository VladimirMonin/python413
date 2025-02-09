"""
Тема: Функции Ч8. Генераторы. Генераторные выражения. Урок: 21
- Концепция ленивых вычислений
- Сравнение range в списке и вне
"""

# // https://api.openweathermap.org/data/2.5/weather?q=Усть-Каменогорск&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru

cities_list = ["Бангкок", "Сеул", "Токио", "Усть-Каменогорск", "Барнаул", "Москва"]

# pip install requests
import requests
from typing import Generator

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
    try:
        response = requests.get(url, params=params)
        data = response.json()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

    except requests.exceptions.RequestException as e:
        return f"Ошибка при получении данных для города {city} - {str(e)}"
    
    return f"Город: {city}, Температура: {temp}°C, ощущается как {feels_like}°C"

# for city in cities_list:
#     print(get_weather(city))


# Это же, на генераторе
def get_weather_gen(cities: list[str]) -> Generator[str]:
    for city in cities:
        yield get_weather(city)

for weather in get_weather_gen(cities_list):
    print(weather)