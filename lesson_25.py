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

        self.messages = [
            {
                "role": "system",
                "content": self.system_role,
            }
        ]

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

    def __add_message(self, message: str, role: str):
        self.messages.append(
            {
                "role": role,
                "content": message,
            }
        )

    def text_completion(self, prompt: str):
        self.__add_message(prompt, "user")

        response = self.client.chat.complete(
            model= self.model,
            messages=self.messages,
        )


        self.__add_message(response.choices[0].message.content, "assistant")

        return response.choices[0].message.content


# Тестовый запуск
chat = MistralAIChat(api_key=MISTRAL_API_KEY, model=model, system_role="Ты эксперт по хокку и поэт. Отвечаешь только в этом стиле")

while True:
    prompt = input("Введите ваш запрос: ")
    if prompt.lower() == "exit":
        break
    response = chat.text_completion(prompt)
    print(response)
    print("-" * 40)
