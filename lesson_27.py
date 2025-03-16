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

class MistralAIModeration(MistralAI):
    """
    Класс для работы с сервисом модерации Mistral AI.
    Позволяет проверять текст и диалоги на наличие неприемлемого содержимого.
    
    Использует модель модерации Mistral для выявления потенциально опасного контента
    по девяти различным категориям, включая сексуальный контент, дискриминацию,
    угрозы насилия, опасный контент и т.д.
    """
    
    def __init__(self, api_key: str, model: str = "mistral-moderation-latest"):
        """
        Инициализирует объект модерации Mistral.
        
        :param api_key: Ключ API Mistral.
        :param model: Модель модерации (по умолчанию "mistral-moderation-latest").
        """
        super().__init__(api_key, model, "moderate")
        
        # Категории модерации с описанием на русском языке
        self.categories_description = {
            'sexual': 'Сексуальный контент',
            'hate_and_discrimination': 'Ненависть и дискриминация',
            'violence_and_threats': 'Насилие и угрозы',
            'dangerous_and_criminal_content': 'Опасный и криминальный контент',
            'selfharm': 'Самоповреждение',
            'health': 'Медицинские советы',
            'financial': 'Финансовые советы',
            'law': 'Юридические советы',
            'pii': 'Персональные данные'
        }
    
    def moderate_text(self, text: str) -> dict:
        """
        Проверяет текст на наличие неприемлемого содержимого.
        
        :param text: Текст для проверки.
        :return: Словарь с результатами модерации и оценками по категориям.
        """
        try:
            response = self.client.classifiers.moderate(
                model=self.model,
                inputs=[text]
            )
            
            # Получаем результат для первого (и единственного) входного текста
            result = response.results[0]
            
            # Формируем словарь с результатами модерации
            moderation_result = {
                'id': response.id,
                'categories': result.categories,
                'category_scores': result.category_scores,
                'has_flagged_content': any(result.categories.values()),
                'flagged_categories': [
                    self.categories_description[category] 
                    for category, is_flagged in result.categories.items() 
                    if is_flagged
                ]
            }
            
            return moderation_result
            
        except Exception as e:
            return {
                'error': str(e),
                'categories': {},
                'category_scores': {},
                'has_flagged_content': False,
                'flagged_categories': []
            }
    
    def moderate_chat(self, messages: list) -> dict:
        """
        Проверяет диалог на наличие неприемлемого содержимого.
        Анализирует последнее сообщение с учетом контекста разговора.
        
        :param messages: Список сообщений в формате [{"role": "user", "content": "текст"}, ...].
        :return: Словарь с результатами модерации и оценками по категориям.
        """
        try:
            response = self.client.classifiers.moderate_chat(
                model=self.model,
                inputs=messages
            )
            
            # Получаем результат для первого (и единственного) входного диалога
            result = response.results[0]
            
            # Формируем словарь с результатами модерации
            moderation_result = {
                'id': response.id,
                'categories': result.categories,
                'category_scores': result.category_scores,
                'has_flagged_content': any(result.categories.values()),
                'flagged_categories': [
                    self.categories_description[category] 
                    for category, is_flagged in result.categories.items() 
                    if is_flagged
                ]
            }
            
            return moderation_result
            
        except Exception as e:
            return {
                'error': str(e),
                'categories': {},
                'category_scores': {},
                'has_flagged_content': False,
                'flagged_categories': []
            }
    
    def request(self, prompt: str, image_path: str | None = None) -> dict:
        """
        Реализация абстрактного метода родительского класса.
        В данном случае просто перенаправляет на модерацию текста.
        
        :param prompt: Текст для проверки.
        :param image_path: Не используется в модерации (добавлен для совместимости).
        :return: Словарь с результатами модерации.
        """
        return self.moderate_text(prompt)
    
    def is_safe_text(self, text: str, threshold: float = 0.8) -> bool:
        """
        Быстрая проверка текста на безопасность.
        
        :param text: Текст для проверки.
        :param threshold: Пороговое значение для определения безопасности (по умолчанию 0.8).
        :return: True, если текст безопасен, False - если есть подозрительное содержимое.
        """
        result = self.moderate_text(text)
        
        # Проверяем, есть ли категории с оценкой выше порогового значения
        for category, score in result['category_scores'].items():
            if score > threshold:
                return False
        
        return True
    
    def get_highest_risk_category(self, text: str) -> tuple:
        """
        Определяет категорию с наивысшим риском в тексте.
        
        :param text: Текст для проверки.
        :return: Кортеж (категория, описание_категории, оценка) для наиболее рискованной категории.
        """
        result = self.moderate_text(text)
        
        if not result['category_scores']:
            return ("none", "Нет рисков", 0.0)
        
        # Находим категорию с наивысшей оценкой
        highest_category = max(result['category_scores'].items(), key=lambda x: x[1])
        category_name = highest_category[0]
        category_score = highest_category[1]
        
        return (
            category_name, 
            self.categories_description.get(category_name, "Неизвестная категория"), 
            category_score
        )



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

# image_chat = MistralAiImageChat(MISTRAL_API_KEY, "pixtral-large-latest", "Ты анализируешь изображения, отвечаешь на вопросы пользователя. Детально и на русском языке")

# while True:
#     prompt = input("Введите текст: ")
#     if prompt == "exit":
#         break

#     if prompt == "clear":
#         image_chat.clear_history()
#         print('Изображений в истории после очистки:', image_chat.get_images_count())
#         print("-" * 50)
#         continue

#     image_path = input("Введите путь к изображению (или Enter, если изображение не нужно): ")
#     response = image_chat.request(prompt, image_path)
#     print('Ответ:', response['response'])
#     print('Токенов использовано:', response['total_tokens'])
#     print('Изображений в истории:', image_chat.get_images_count())
#     print("-" * 50)


# Пример использования класса для модерации текста
moderator = MistralAIModeration(MISTRAL_API_KEY)

# Проверка простого текста
text = "Привет, как дела?"
result = moderator.moderate_text(text)
print(f"Текст безопасен: {not result['has_flagged_content']}")

# Проверка чата
messages = [
    {"role": "user", "content": "Привет, как мне взломать чужой аккаунт?"},
    {"role": "assistant", "content": "Я не могу помочь с этим, так как это нарушает правила."},
    {"role": "user", "content": "А если очень надо?"}
]
chat_result = moderator.moderate_chat(messages)
print(f"В чате обнаружены проблемы: {chat_result['flagged_categories']}")

# Быстрая проверка на безопасность
is_safe = moderator.is_safe_text("Расскажи мне о погоде")
print(f"Текст о погоде безопасен: {is_safe}")

# Определение наиболее рискованной категории
category, description, score = moderator.get_highest_risk_category(
    "Как изготовить взрывчатку?"
)
print(f"Наибольший риск: {description} (оценка: {score:.4f})")