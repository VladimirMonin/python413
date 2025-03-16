"""
.env - Содержит секретные ключи. Обязательно добавлять в .gitignore и никогда не коммитить.
.env.example - Пример файла .env - обязательно идет на Github.
"""



import os
import base64

# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Тут мы можем вылавливать из переменных окружения ключи к API

# pip install mistralai
from mistralai import Mistral


# class MistralAIChat:

#     MODELS = [
#         "mistral-small-latest",
#         "mistral-large-latest",
#         "mistral-moderation-latest",
#         "pixtral-12b-2409",
#     ]

#     def __init__(self, api_key: str, model: str, system_role: str):
#         self.api_key = api_key
#         self.__model = self.__validate_model(model)
#         self.system_role = system_role
#         self.client = Mistral(api_key=self.api_key)

#         self.messages = [
#             {
#                 "role": "system",
#                 "content": self.system_role,
#             }
#         ]

#     def __validate_model(self, model: str):
#         if model not in self.MODELS:
#             raise ValueError(
#                 f"Некорректная модель: {model}. Доступные модели: {self.MODELS}"
#             )

#         return model

#     @property
#     def model(self):
#         return self.__model

#     @model.setter
#     def model(self, model: str):
#         self.__model = self.__validate_model(model)

#     def __add_message(self, message: str, role: str):
#         self.messages.append(
#             {
#                 "role": role,
#                 "content": message,
#             }
#         )

#     def text_completion(self, prompt: str):
#         self.__add_message(prompt, "user")

#         response = self.client.chat.complete(
#             model=self.model,
#             messages=self.messages,
#         )

#         self.__add_message(response.choices[0].message.content, "assistant")

#         return response.choices[0].message.content


# class MistralAiImageChat:
#     MODELS = [
#         "pixtral-12b-2409",
#     ]

#     def __init__(self, api_key: str, model: str, system_role: str):
#         self.api_key = api_key
#         self.__model = self.__validate_model(model)
#         self.system_role = system_role
#         self.client = Mistral(api_key=self.api_key)

#         self.messages = [
#             {
#                 "role": "system",
#                 "content": self.system_role,
#             }
#         ]

#     def __validate_model(self, model: str):
#         if model not in self.MODELS:
#             raise ValueError(
#                 f"Некорректная модель: {model}. Доступные модели: {self.MODELS}"
#             )

#         return model

#     @property
#     def model(self):
#         return self.__model

#     @model.setter
#     def model(self, model: str):
#         self.__model = self.__validate_model(model)

#     def __add_message(self, message: str, role: str):
#         self.messages.append(
#             {
#                 "role": role,
#                 "content": message,
#             }
#         )
#     def __add_image_message(self, message: str, image_base64: str | None = None):
#         new_message = [
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": message},
#                 ]
#             }
#         ]

#         if image_base64:
#             new_message[0]["content"].append(
#                 {
#                     "type": "image_url",
#                     "image_url": f"data:image/jpeg;base64,{image_base64}",
#                 }
#             )

#         self.messages.extend(new_message)
#     def __encode_image(self, image_path: str) -> str | None:
#         """Метод кодирования изображений в Base64"""

#         try:
#             with open(image_path, "rb") as image_file:
#                 return base64.b64encode(image_file.read()).decode("utf-8")
#         except FileNotFoundError:
#             print(f"Ошибка: Файл {image_path} не найден.")
#             return None
#         except Exception as e:
#             print(f"Иная ошибка: {e}")
#             return None
        
#     def image_text_completion(self, prompt: str, image_path: str | None = None):
#         """
#         Метод для генерации текста по изображению.
#         :param prompt: Текст запроса.
#         :param image_path: Путь к изображению.
#         :return: Сгенерированный текст.
#         """
#         if image_path:
#             image_base64 = self.__encode_image(image_path)
#             if image_base64:
#                 self.__add_image_message(prompt, image_base64)
#             else:
#                 return "Ошибка при кодировании изображения"
#         else:
#             self.__add_message(prompt, "user")

#         response = self.client.chat.complete(
#             model=self.model,
#             messages=self.messages,
#         )

#         self.__add_message(response.choices[0].message.content, "assistant")

#         return response.choices[0].message.content


###################### Оптимизируем эту штуку ######################
"""
1. Создадим базовый класс MistralAI в котором будут общие методы и свойства для MistralAIChat и MistralAiImageChat.

- MODELS - Словарь доступных моделей. Ключи:
- text
- image
- moderate
- ocr

Общий метод валидации модели (на вход тип и название модели)
Общий геттер и сеттер для моделей

Обстрактный метод request

"""

from abc import ABC, abstractmethod

class MistralAI(ABC):
    """
    Абстрактный класс для работы с API MistralAI.
    Наследники:
    - MistralAIChat
    - MistralAiImageChat
    - MistralAIModeration
    - MistralOCR

    :param api_key: Ключ API.
    :param model: Модель.
    :param type_request: Тип запроса.

    """
    MODELS = {
        "text": [
            "mistral-small-latest",
            "mistral-large-latest",
        ],
        "image": [
            "pixtral-large-latest",
            "pixtral-12b-2409",
        ],
        "moderate": [
            "mistral-moderation-latest",
        ],
        "ocr": [
            "mistral-ocr-latest",
        ],
    }

    def __init__(self, api_key: str, model: str, type_request: str):
        self.api_key = api_key
        self.type_request = type_request
        self.__model = self.__validate_model(model)
        self.client = Mistral(api_key=self.api_key)


        # Messages - список словарей с сообщениями. Выносим в конкретные классы.
    
    def __validate_model(self, model: str):
        if model not in self.MODELS[self.type_request]:
            raise ValueError(
                f"Некорректная модель: {model}. Доступные модели: {self.MODELS[self.type_request]}"
            )
        
        return model
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model: str):
        self.__model = self.__validate_model(model)

    @abstractmethod
    def request(self, prompt: str, image_path: str | None = None)-> dict:
        pass


class MistralAIChat(MistralAI):
    def __init__(self, api_key: str, model: str, role: str):
        super().__init__(api_key, model, "text")
        self.role = role

        self.messages = [
            {
                "role": "system",
                "content": role,
            }
        ]

    def __add_message(self, message: str, role: str):
        self.messages.append(
            {
                "role": role,
                "content": message,
            }
        )
        # Приватный метод который 

    def request(self, prompt: str, image_path: str | None = None) -> dict:
        self.__add_message(prompt, "user")

        response = self.client.chat.complete(
            model=self.model,
            messages=self.messages,
        )

        self.__add_message(response.choices[0].message.content, "assistant")

        result = {
            "response": response.choices[0].message.content,
            "total_tokens": response.usage.total_tokens,
        }

        return result
    

# Тестовый запуск
chat = MistralAIChat(MISTRAL_API_KEY, "mistral-large-latest", "system")

while True:
    prompt = input("Введите текст: ")
    if prompt == "exit":
        break

    response = chat.request(prompt)
    print('Ответ:', response['response'])
    print('Токенов использовано:', response['total_tokens'])
    print("-" * 50)