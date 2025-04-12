"""
Lesson 34: Поведенческие паттерны проектирования
- Состояние музыкальный плеер
- Наблюдатель уведомления в блоге о новых постах
"""

from abc import ABC, abstractmethod
import email

class AbstractNotification(ABC):
    """
    Абстрактный класс уведомления.
    """
    
    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Абстрактный метод для отправки уведомления.
        """
        pass


class EmailNotification(AbstractNotification):
    """
    Конкретная реализация уведомления по электронной почте.
    """
    
    def notify(self, message: str) -> None:
        """
        Отправляет уведомление по электронной почте.
        """
        print(f"Отправлено уведомление по электронной почте: {message}")


class TelegramNotification(AbstractNotification):
    """
    Конкретная реализация уведомления в Telegram.
    """
    
    def notify(self, message: str) -> None:
        """
        Отправляет уведомление в Telegram.
        """
        print(f"Отправлено уведомление в Telegram: {message}")


class Blog:
    """
    Класс блога, который уведомляет подписчиков о новых постах.
    """
    
    def __init__(self):
        self.subscribers = []
    
    def subscribe(self, subscriber: AbstractNotification) -> None:
        """
        Подписывает пользователя на уведомления.
        """
        self.subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber: AbstractNotification) -> None:
        """
        Отписывает пользователя от уведомлений.
        """
        self.subscribers.remove(subscriber)
    
    def new_post(self, title: str) -> None:
        """
        Уведомляет подписчиков о новом посте.
        """
        message = f"Новый пост: {title}"
        for subscriber in self.subscribers:
            subscriber.notify(message)


# Пример использования паттерна Наблюдатель
blog = Blog()
email_notification = EmailNotification()
telegram_notification = TelegramNotification()

# Подписываемся на уведомления
blog.subscribe(email_notification)
blog.subscribe(telegram_notification)

# Создаем новый пост
blog.new_post("Паттерны проектирования в Python")

# Отписываемся от уведомлений
blog.unsubscribe(email_notification)

# Создаем новый пост
blog.new_post("Наблюдатель в Python")