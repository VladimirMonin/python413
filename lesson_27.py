"""
.env - Содержит секретные ключи. Обязательно добавлять в .gitignore и никогда не коммитить.
.env.example - Пример файла .env - обязательно идет на Github.
"""

from email.mime import image
import os
import base64

# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# pip install mistralai
from mistralai import Mistral
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
    def request(self, prompt: str, image_path: str | None = None) -> dict:
        pass


class MistralAIChat(MistralAI):
    def __init__(self, api_key: str, model: str, role: str):
        super().__init__(api_key, model, "text")
        self.role = role
        self.token_limit = 100_000

        self.messages = [
            {
                "role": "system",
                "content": role,
            }
        ]

    def __add_message(self, message: str, role: str, tokens: int):
        """
        Метод добавления сообщения в список сообщений.
        :param message: Текст сообщения.
        :param role: Роль.
        :param tokens: Количество токенов.
        """
        self.messages.append(
            {
                "role": role,
                "content": message,
            }
        )

        self.__check_token_limit(tokens)

    def __check_token_limit(self, tokens: int):
        """
        Метод проверки лимита токенов.
        :param tokens: Количество токенов.
        """
        if tokens > self.token_limit:
            self.messages.pop(1)

    def request(self, prompt: str, image_path: str | None = None) -> dict:
        self.__add_message(prompt, "user", 0)

        response = self.client.chat.complete(
            model=self.model,
            messages=self.messages,
        )

        result = {
            "response": response.choices[0].message.content,
            "total_tokens": response.usage.total_tokens,
        }

        self.__add_message(result["response"], "assistant", result["total_tokens"])

        return result


class MistralAiImageChat(MistralAI):
    """
    Класс для работы с мультимодальной моделью MistralAI, поддерживающей анализ изображений.
    Позволяет сохранять полную историю чата со всеми изображениями.
    """

    def __init__(self, api_key: str, model: str, role: str):
        super().__init__(api_key, model, "image")
        self.role = role
        self.token_limit = 100_000
        self.images_count = 0  # Счетчик загруженных изображений

        self.messages = [
            {
                "role": "system",
                "content": role,
            }
        ]

    def __encode_image(self, image_path: str) -> str | None:
        """
        Кодирует изображение в формат base64 для отправки в API.

        :param image_path: Путь к файлу изображения.
        :return: Base64-строка или None при ошибке.
        """
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        except FileNotFoundError:
            print(f"Ошибка: Файл {image_path} не найден.")
            return None
        except Exception as e:
            print(f"Произошла ошибка при обработке изображения: {e}")
            return None

    def __add_message(self, message: str, role: str, tokens: int = 0):
        """
        Добавляет текстовое сообщение в историю чата.

        :param message: Текст сообщения.
        :param role: Роль отправителя (user/assistant).
        :param tokens: Количество токенов в сообщении.
        """
        self.messages.append(
            {
                "role": role,
                "content": message,
            }
        )
        self.__check_token_limit(tokens)

    def __add_image_message(self, prompt: str, image_base64: str | None = None):
        """
        Добавляет сообщение с изображением в историю чата.

        :param prompt: Текст сообщения пользователя.
        :param image_base64: Изображение в формате base64.
        """
        content_items = [{"type": "text", "text": prompt}]

        if image_base64:
            self.images_count += 1
            content_items.append(
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{image_base64}",
                }
            )

        self.messages.append({"role": "user", "content": content_items})

    def __check_token_limit(self, tokens: int):
        """
        Проверяет, не превышен ли лимит токенов, и при необходимости удаляет старые сообщения.

        :param tokens: Количество токенов в последнем сообщении.
        """
        # Если превысили лимит, удаляем самое старое сообщение (кроме системного)
        if tokens > self.token_limit:
            # Находим первое сообщение, которое не является системным
            for i in range(1, len(self.messages)):
                if self.messages[i]["role"] != "system":
                    self.messages.pop(i)
                    break

    def request(self, prompt: str, image_path: str | None = None) -> dict:
        """
        Отправляет запрос к API Mistral с изображением или без.
        Все изображения сохраняются в истории чата.

        :param prompt: Текст запроса пользователя.
        :param image_path: Путь к новому изображению (None если новое изображение не добавляется).
        :return: Словарь с ответом модели и количеством использованных токенов.
        """
        # Если передан путь к новому изображению
        if image_path:
            image_base64 = self.__encode_image(image_path)
            if not image_base64:
                return {
                    "response": "Ошибка при кодировании изображения",
                    "total_tokens": 0,
                }

            # Добавляем новое сообщение с изображением в историю
            self.__add_image_message(prompt, image_base64)
        else:
            # Добавляем обычное текстовое сообщение
            self.__add_message(prompt, "user")

        # Отправляем запрос к API со всей накопленной историей
        response = self.client.chat.complete(
            model=self.model,
            messages=self.messages,
        )

        result = {
            "response": response.choices[0].message.content,
            "total_tokens": response.usage.total_tokens,
        }

        # Добавляем ответ модели в историю
        self.__add_message(result["response"], "assistant", result["total_tokens"])

        return result

    def get_images_count(self) -> int:
        """
        Возвращает количество изображений в истории.

        :return: Количество изображений.
        """
        return self.images_count

    def clear_history(self, keep_system_prompt: bool = True):
        """
        Очищает историю сообщений, оставляя только системный промпт.

        :param keep_system_prompt: Флаг, указывающий, сохранять ли системный промпт.
        """
        if keep_system_prompt:
            system_prompt = self.messages[0]
            self.messages = [system_prompt]
        else:
            self.messages = []

        self.images_count = 0


# # Тестовый запуск
# chat = MistralAIChat(MISTRAL_API_KEY, "mistral-large-latest", "Ты шутник юморист. Отвечаешь как робот Бендер из Футурамы")

# while True:
#     prompt = input("Введите текст: ")
#     if prompt == "exit":
#         break

#     response = chat.request(prompt)
#     print('Ответ:', response['response'])
#     print('Токенов использовано:', response['total_tokens'])
#     print("-" * 50)


# Запуск с изображениями

image_chat = MistralAiImageChat(MISTRAL_API_KEY, "pixtral-large-latest", "Ты анализируешь изображения, отвечаешь на вопросы пользователя. Детально и на русском языке")

while True:
    prompt = input("Введите текст: ")
    if prompt == "exit":
        break

    if prompt == "clear":
        image_chat.clear_history()
        print('Изображений в истории после очистки:', image_chat.get_images_count())
        print("-" * 50)
        continue

    image_path = input("Введите путь к изображению (или Enter, если изображение не нужно): ")
    response = image_chat.request(prompt, image_path)
    print('Ответ:', response['response'])
    print('Токенов использовано:', response['total_tokens'])
    print('Изображений в истории:', image_chat.get_images_count())
    print("-" * 50)