"""
16.02.2025
Python: ООП. Ч2. Простое взаимодействие классов. Практика. Урок: 23
- Класс TxtHandler - для работы с текстовыми документами
"""

from openai import OpenAI

# client = OpenAI(api_key="BANANA", base_url="https://api.deepseek.com")

# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "Ты автор смешных шуток для программистов. Пишешь шутки на русском языке которые понимают жители СНГ"},
#         {"role": "user", "content": "Напиши шутку про мартышку и итератор"},
#     ],
#     stream=False
# )
 
# print(response.choices[0].message.content)

class DeepSeekChat:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")
        self.system_role = "Ты опытный ассистент помощник, отлично знаешь русский язык"

    def set_system_role(self, role:str):
        self.system_role = role

    def completition(self, message:str):
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": self.system_role},
                {"role": "user", "content": message},
            ],
            stream=False
        )
        return response.choices[0].message.content

# Пример использования
chat = DeepSeekChat(api_key="BANANA")
chat.set_system_role("Ты автор смешных шуток для программистов. Пишешь шутки на русском языке которые понимают жители СНГ")
response = chat.completition("Напиши шутку про мартышку и ООП в Python")
print(response)

"""— Сидит мартышка в зоопарке, изучает Python. Подходит к ней смотритель и спрашивает:  
— Ну что, освоила ООП?  
— Конечно! — отвечает мартышка. — Я уже создала класс `Banana`, наследовала от него `YellowBanana` и `GreenBanana`, а потом переопределила метод `eat()` в дочерних классах.  
— Молодец! — говорит смотритель. — А зачем тебе это?  
— Ну как зачем? Чтобы не нарушать принцип открытости/закрытости: хочу жёлтый банан — жёлтый, хочу зелёный — зелёный. А если захочу красный — просто создам новый класс!  
— А если захотела банан, а его нет?  
— Тогда выброшу исключение `NoBananaError` и пойду спать! """