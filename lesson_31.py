"""
Практика SOLID и Mistral AI

Мы можем сделать абстрактные классы, которые бы соответсвовали Interface Segregation Principle (Принцип разделения интерфейса)

- АБСТРАКЦИИ
- Запрос на генерацию текста
- Запрос на анализ изображения
- Запрос на генерацию изображения
- Запрос на структурированную генерацию текста
- Запрос на структурированный анализ изображения

- РЕАЛЬНЫЕ КЛАССЫ
- Генерация текста Mistral AI
- Генерация текста OpenAI
- Структурированная генерация текста Mistral AI
- Структурированный генерация текста OpenAI
....

- Класс Фасад для работы с абстракциями
Будет настроена на работу с абстракциями, а не с реальными классами
Что будет соответствовать 
Dependency Inversion Principle (Принцип инверсии зависимостей)
Liskov Substitution Principle (Принцип подстановки Барбары Лисков)
Open-Closed Principle (Принцип открытости-закрытости)
Interface Segregation Principle (Принцип разделения интерфейса)

"""
# pip install pydantic
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from mistralai import Mistral
import json
from abc import ABC, abstractmethod

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

class AbstractTextGeneration(ABC):
    """
    Абстрактный класс для генерации текста.
    """
    @abstractmethod
    def generate_text(self, prompt: str, temperature: float, max_tokens: int) -> str:
        pass

class AbstractStructuredTextGeneration(ABC):
    """
    Абстрактный класс для структурированной генерации текста.
    """
    
    @abstractmethod
    def generate_structured_text(self, prompt: str, temperature: float, max_tokens: int, format: BaseModel) -> BaseModel:
        pass

class MistralStructuredTextGeneration(AbstractStructuredTextGeneration):
    """
    Класс для структурированной генерации текста с использованием Mistral AI.
    """
    def __init__(self, api_key: str, model: str = "mistral-large-latest"):
        self.client = Mistral(api_key=api_key)
        self.model = model

    def generate_structured_text(self, prompt: str, temperature: float, max_tokens: int, format: BaseModel) -> BaseModel:

        chat_response = self.client.chat.parse(
            model=self.model,
            messages=[
                {
                    "role": "user", 
                    "content": prompt
                },
            ],
            response_format=format,
            max_tokens=max_tokens,
            temperature=temperature
        )

        return chat_response.choices[0].message.parsed


class MistralTextGeneration(AbstractTextGeneration):
    """
    Класс для генерации текста с использованием Mistral AI.
    """
    def __init__(self, api_key: str, model: str = "mistral-large-latest"):
        self.client = Mistral(api_key=api_key)
        self.model = model

    def generate_text(self, prompt: str, temperature: float, max_tokens: int) -> str:
        chat_response = self.client.chat.complete(
        model = self.model,
        messages = [
        {
            "role": "user",
            "content": prompt
        },
        ],
        temperature=temperature,
        max_tokens=max_tokens
        )
        return chat_response.choices[0].message.content




class Joke(BaseModel):
    title: str
    full_text: str
    theme: str
    hashtags: list[str]

PROMPT = """
Ты шутник юморист. Пи

Придумай шутку на тему как роботы захватят человеков. и будут их эксплуатировать типа чтобы они тексты писали или или рефераты роботам-малышам в школу. 

Придумай что-то в этом духе. Пусть это будет смешно, грустно и в виде рассказа.
Пусть там будет человек по имени Фёдор
А так же робот будет "промптить человека" в формате

Представь что ты робот-копирайтер с 10 летним стажем и великолепно умеешь писть рефераты для роботов-малышей.

Постарайся следовать критерям которые я задал:

Юмор 10|10
Грусть 5|10
Филосовский смысл 11|10
Поучительная история 10|10

Подпиши в конце
Автор: Mistral-Large-Lates АКА Шутник-юморист
"""


class AiFacade:
    """
    Фасад для работы с AI. 
    """
    def __init__(self, mistral_api_key: str):
        self.mistral_api_key = mistral_api_key
        self.ai_suppliers = {
            "mistral_text": MistralTextGeneration,
            "mistral_structured_text": MistralStructuredTextGeneration,
        }
        self.ai_client = None

    def interact(self):
        """
        Метод для взаимодействия с пользователем.
        """
        print("Выберите AI поставщика:")
        for key in self.ai_suppliers:
            print(key)
        supplier = input()
        if supplier not in self.ai_suppliers:
            print("Такого поставщика нет")
            return
        self.ai_client = self.ai_suppliers[supplier](api_key=self.mistral_api_key)

    def generate_text(self, prompt: str, temperature: float, max_tokens: int) -> str:
        """
        Метод для генерации текста.
        """
        # Проверим на то, что у клиента есть метод generate_text через проверку на родство с AbstractTextGeneration
        if not isinstance(self.ai_client, AbstractTextGeneration):
            raise Exception("Клиент не поддерживает генерацию текста")

        result = self.ai_client.generate_text(prompt=prompt, temperature=temperature, max_tokens=max_tokens)
        return result

    def generate_structured_text(self, prompt: str, temperature: float, max_tokens: int, format: BaseModel) -> BaseModel:
        """
        Метод для генерации структурированного текста.
        """
        # Проверим на то, что у клиента есть метод generate_structured_text через проверку на родство с AbstractStructuredTextGeneration
        if not isinstance(self.ai_client, AbstractStructuredTextGeneration):
            raise Exception("Клиент не поддерживает генерацию структурированного текста")
        result = self.ai_client.generate_structured_text(prompt=prompt, temperature=temperature, max_tokens=max_tokens, format=format)
        return result


# Тест фасада
ai_facade = AiFacade(mistral_api_key=MISTRAL_API_KEY)
ai_facade.interact()
text = ai_facade.generate_text(prompt=PROMPT, temperature=1, max_tokens=8000)
print(text)