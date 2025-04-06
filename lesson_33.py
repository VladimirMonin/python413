"""
Lesson 33 - Паттерны проектирования на ООП
- Абстрактная фабрика
- Прокси
"""

"""
Класс - Абстрактный запрос к ИИ
Класс - Прокси запрос к ИИ
Класс - Реальный запрос к ИИ
Класс - Проверка "Токенов" 
"""

from abc import ABC, abstractmethod

class AbstractAIRequest(ABC):
    """
    Абстрактный класс для запроса к ИИ.
    """
    @abstractmethod
    def request(self, prompt: str) -> str:
        """
        Метод для отправки запроса к ИИ.
        """
        pass


class RealAIRequest(AbstractAIRequest):
    """
    Реальный класс для запроса к ИИ.
    """
    def request(self, prompt: str) -> str:
        """
        Отправляет запрос к ИИ и возвращает ответ.
        """
        # Здесь должен быть код для отправки запроса к ИИ
        return f"Отправка запроса к ИИ: {prompt}"

class CheckTokens:
    """
    Класс для проверки токенов.
    """
    max_tokens: int = 20

    def check_tokens(self, tokens: int) -> bool:
        """
        Проверяет, достаточно ли токенов для выполнения запроса.
        """
        if tokens > self.max_tokens:
            print(f"Превышено количество токенов: {tokens} > {self.max_tokens}")
            return False
        return True
    

class ProxyAIRequest(AbstractAIRequest):
    """
    Прокси-класс для запроса к ИИ.
    """
    def __init__(self):
        self.real_request = RealAIRequest()
        self.check_tokens = CheckTokens()

    def request(self, prompt: str) -> str:
        """
        Проверяет токены и отправляет запрос к ИИ.
        """
        tokens = len(prompt)
        if self.check_tokens.check_tokens(tokens):
            print(f'Прокси: количество токенов {tokens} для запроса "{prompt}"')
            return self.real_request.request(prompt)
        else:
            return "Ошибка: недостаточно токенов для выполнения запроса."
        

# Пример использования
if __name__ == "__main__":
    proxy_request = ProxyAIRequest()
    prompt = "Какой чудесный день! Какой чудесный пень!"
    response = proxy_request.request(prompt)
    print(response)