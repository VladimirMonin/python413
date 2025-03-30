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

load_dotenv()

class Joke(BaseModel):
    title: str
    full_text: str
    theme: str
    hashtags: list[str]


PROMPT = "Ты шутник юморист. Придумай шутку на тему как роботы захватят человеков."

api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.parse(
    model=model,
    messages=[
        {
            "role": "user", 
            "content": PROMPT
        },
    ],
    response_format=Joke,
    max_tokens=8000,
    temperature=0.6
)

# print(chat_response.choices[0].message.content)
print(chat_response.choices[0].message.parsed)
print(type(chat_response.choices[0].message.parsed))
# print(chat_response)
# id='e967e2027d1143699971a8d4513017cf' object='chat.completion' model='mistral-large-latest' usage=UsageInfo(prompt_tokens=35, completion_tokens=112, total_tokens=147) created=1743330896 choices=[ParsedChatCompletionChoice(index=0, message=ParsedAssistantMessage(content='{\n  "full_text": "Почему роботы никогда не захватят людей? Потому что им постоянно придется перезагружаться из-за наших бесконечных обновлений!",\n  "hashtags": ["роботы", "юмор", "технологии"],\n  "theme": "технологии",\n  "title": "Роботы и обновления"\n}', tool_calls=None, prefix=False, role='assistant', parsed=Joke(title='Роботы и обновления', full_text='Почему роботы никогда не захватят людей? Потому что им постоянно придется перезагружаться из-за наших бесконечных обновлений!', theme='технологии', hashtags=['роботы', 'юмор', 'технологии'])), finish_reason='stop')]