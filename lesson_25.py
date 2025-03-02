"""
.env - Содержит секретные ключи. Обязательно добавлять в .gitignore и никогда не коммитить.
.env.example - Пример файла .env - обязательно идет на Github.
- Класс для работы с MistralAI чатом
- Класс для работы с MistralAI изображениями и текстом
- Знакомство с наследованием
"""

class AiChat():
    message = "Моё послание"
    def __str__(self):
        return f"Я есть {self.__class__.__name__}. {self.message}"
    
    def send_message(self, additional_message: str = ""):
        return f"{self.message} {additional_message}"

class ImageAiChat(AiChat):
    pass

class MistralAiChat(AiChat):
    pass

ai_chat = AiChat()
print(ai_chat)
image_ai_chat = ImageAiChat()
print(image_ai_chat)
mistral_ai_chat = MistralAiChat()
print(mistral_ai_chat)

print(type(ai_chat))
print(type(image_ai_chat))
print(type(mistral_ai_chat))

# А теперь is instance
# Проверим наследника на принадлежность к родителю
print(isinstance(ai_chat, AiChat))
print(isinstance(image_ai_chat, AiChat))
print(isinstance(mistral_ai_chat, AiChat))
