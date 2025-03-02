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
    # Расширение метода.
    def send_message(self, additional_message: str = ""):
        # result = AiChat.send_message(self, additional_message)
        result = super().send_message(additional_message)
        return f"{result} и ещё какой-то текст"


class MistralAiChat(AiChat):
    pass

image_ai_chat = ImageAiChat()
print(image_ai_chat.send_message("Привет!"))
