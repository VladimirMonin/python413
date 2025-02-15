"""
15.02.2025
Python: ООП. Ч1. Атрибуты и методы. Класс и экземпляр. Практика. Урок: 22
- class
- нейминг классов UpperCamelCase
- атрибут класса
- атрибуты экземпляра
- __init__ - инициализатор
- self - ссылка на экземпляр класса
- __new__ - как скрытая часть конструктора
- методы работающие с self - методы экземпляра
- документация класса и методов
- статичные методы
- методы класса

"""

# pip install requests
import requests


class Weather:
    """
    Класс для получения погоды из API OpenWeatherMap.
    """

    requsts_url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units={units}&lang={lang}"

    def __init__(self, appid: str, units: str, lang: str):
        self.appid = appid
        self.units = units
        self.lang = lang
        self.url: str = ""

    def get_url(self, city: str) -> str:
        """
        Формирует url для запроса к API OpenWeatherMap.
        :param city: Название города.
        :return: Сформированный url.
        """
        self.url = self.requsts_url.format(
            city=city, appid=self.appid, units=self.units, lang=self.lang
        )
        return self.url

    def format_response(self, response: dict) -> str:
        """
        Форматирует ответ API OpenWeatherMap.
        :param response: Ответ API в формате словаря.
        :return: Отформатированная строка с информацией о погоде.
        """
        temp = response["main"]["temp"]
        feels_like = response["main"]["feels_like"]
        return f"Температура: {temp}°C, ощущается как {feels_like}°C"

    def get_weather(self, city: str) -> str:
        """
        Получает и форматирует погоду для заданного города.
        :param city: Название города.
        :return: Информация о погоде.
        """
        url = self.get_url(city)
        try:
            response = requests.get(url)
            data = response.json()
            return self.format_response(data)
        except requests.exceptions.RequestException as e:
            return f"Ошибка при получении данных для города {city} - {str(e)}"

    def __call__(self, city: str) -> str:
        """
        Делает объект вызываемым.
        :param city: Название города.
        :return: Информация о погоде.
        """
        return f'Город: {city}, {self.get_weather(city)}'


# ТЕСТ
if __name__ == "__main__":
    weather = Weather(
        appid="23496c2a58b99648af590ee8a29c5348", units="metric", lang="ru"
    )
    # Это без __call__
    moscow = weather.get_weather("Москва")
    # __call__ сделал мой объект вызываемым
    sanct_petersburg = weather("Санкт-Петербург")

    print(moscow)
    print(sanct_petersburg)
