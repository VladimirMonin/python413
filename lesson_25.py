"""
.env - Содержит секретные ключи. Обязательно добавлять в .gitignore и никогда не коммитить.
.env.example - Пример файла .env - обязательно идет на Github.
"""

from dotenv import load_dotenv
# pip install python-dotenv
import os

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Тут мы можем вылавливать из переменных окружения ключи к API

from mistralai import Mistral
model = "mistral-large-latest"


class MistralAIChat:
    
    MODELS = [
    "mistral-small-latest",
    "mistral-large-latest",
    "mistral-moderation-latest",
    "pixtral-12b-2409",
]

    def __init__(self, api_key: str, model: str, system_role: str):
        self.api_key = api_key
        self.__model = self.__validate_model(model)
        self.system_role = system_role
        self.client = Mistral(api_key=self.api_key)

    def __validate_model(self, model: str):
        if model not in self.MODELS:
            raise ValueError(f"Некорректная модель: {model}. Доступные модели: {self.MODELS}")
        
        return model
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model: str):
        self.__model = self.__validate_model(model)

    def text_completion(self, prompt: str):
        response = self.client.chat.complete(
            model= self.model,
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )
        return response.choices[0].message.content


# Тестовый запуск
chat = MistralAIChat(api_key=MISTRAL_API_KEY, model=model, system_role="Ты банан")
print(chat.text_completion("Напиши басню в стиле Крылова, русского писателя, про мартышку и итератор"))