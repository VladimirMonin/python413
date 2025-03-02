"""
Тема: ООП Ч3. Инкапсуляция. Приватные методы и атрибуты. Урок: 24
Два уровня сокрытия
_ это protected - досупно при наследовании
__ это private - доступно только внутри класса

Собственные getters и setters
@property
@speed.setter
@speed.deleter

"""
# pip install mistralai
from mistralai import Mistral

api_key = "wo1LStEQv5lnBZd9RakzmRbasGrjU6Dj"
model = "mistral-large-latest"

# client = Mistral(api_key=api_key)

# chat_response = client.chat.complete(
#     model= model,
#     messages = [
#         {
#             "role": "user",
#             "content": "Напиши шутку про мартышку и итератор",
#         },
#     ]
# )
# print(chat_response.choices[0].message.content)

# mistral-small-latest
# mistral-large-latest
# mistral-moderation-latest
# pixtral-12b-2409

from mistralai import Mistral

api_key = "wo1LStEQv5lnBZd9RakzmRbasGrjU6Dj"
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
chat = MistralAIChat(api_key=api_key, model="pixtral-12b-2409", system_role="Ты банан")
print(chat.text_completion("Напиши шутку про мартышку и итератор"))

# https://docs.mistral.ai/capabilities/vision/