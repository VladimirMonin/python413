"""
Lesson 34: Поведенческие паттерны проектирования
- Состояние музыкальный плеер
- Наблюдатель уведомления в блоге о новых постах
- Цепочка обязанностей поэтапная генерация поста в блог
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Post:
    """
    Класс - пост в блоге.
    """
    title: str
    content: str
    history: list = field(default_factory=list)


    def __post_init__(self):
        """
        Метод инициализации поста.
        """
        self.add_history(f"Пост '{id(self)}' создан.")

    def add_history(self, state: str) -> None:
        """
        Добавляет состояние поста в историю.
        """
        self.history.append(state)


class AbstractPostHandler(ABC):
    """
    Абстрактный класс обработчика поста.
    """
    
    @abstractmethod
    def handle(self, post: Post) -> None:
        """
        Абстрактный метод для обработки поста.
        """
        pass


class TitleHanderA(AbstractPostHandler):
    """
    Обработчик заголовка поста.
    Вариант А.
    """
    
    def handle(self, post: Post) -> None:
        """
        Обрабатывает заголовок поста.
        """
        result = f'Заголовок поста: {post.title}. Обработчик A.'
        print(result)
        post.add_history(result)
        post.title = result


class TitleHanderB(AbstractPostHandler):
    """
    Обработчик заголовка поста.
    Вариант B.
    """
    
    def handle(self, post: Post) -> None:
        """
        Обрабатывает заголовок поста.
        """
        result = f'Заголовок поста: {post.title}. Обработчик B.'
        print(result)
        post.add_history(result)
        post.title = result


class ContentHanderA(AbstractPostHandler):
    """
    Обработчик контента поста.
    Вариант A.
    """
    
    def handle(self, post: Post) -> None:
        """
        Обрабатывает контент поста.
        """
        result = f'Контент поста: {post.content}. Обработчик A.'
        print(result)
        post.add_history(result)
        post.content = result


class ContentHanderB(AbstractPostHandler):
    """
    Обработчик контента поста.
    Вариант B.
    """
    
    def handle(self, post: Post) -> None:
        """
        Обрабатывает контент поста.
        """
        result = f'Контент поста: {post.content}. Обработчик B.'
        print(result)
        post.add_history(result)
        post.content = result


class BlogProcessor:
    """
    Простой процессор для блоговых постов.
    Позволяет выбрать обработчики для заголовка и контента.
    """
    
    def __init__(self):
        """
        Инициализация процессора с наборами обработчиков.
        """
        # Доступные обработчики заголовков
        self.title_handlers = {
            "A": TitleHanderA(),
            "B": TitleHanderB()
        }
        
        # Доступные обработчики контента
        self.content_handlers = {
            "A": ContentHanderA(),
            "B": ContentHanderB()
        }
    
    def process_post_interactive(self, post: Post) -> Post:
        """
        Интерактивно обрабатывает пост, спрашивая пользователя
        о предпочтительных обработчиках.
        
        Args:
            post: Пост для обработки
            
        Returns:
            Обработанный пост
        """
        # Выводим доступные обработчики заголовков
        print("Доступные обработчики заголовков:")
        for key in self.title_handlers.keys():
            print(f"- {key}")
        
        # Спрашиваем пользователя о выборе
        title_choice = input("Выберите обработчик заголовка (или нажмите Enter для пропуска): ")
        
        # Выводим доступные обработчики контента
        print("Доступные обработчики контента:")
        for key in self.content_handlers.keys():
            print(f"- {key}")
        
        # Спрашиваем пользователя о выборе
        content_choice = input("Выберите обработчик контента (или нажмите Enter для пропуска): ")
        
        # Применяем выбранные обработчики
        if title_choice and title_choice in self.title_handlers:
            post.add_history(f"Применяется обработчик заголовка: {title_choice}")
            self.title_handlers[title_choice].handle(post)
        
        if content_choice and content_choice in self.content_handlers:
            post.add_history(f"Применяется обработчик контента: {content_choice}")
            self.content_handlers[content_choice].handle(post)
        
        post.add_history("Обработка завершена")
        return post
    
    def process_post(self, post: Post, title_handler_key: str = None, content_handler_key: str = None) -> Post:
        """
        Обрабатывает пост с указанными обработчиками.
        Удобно для автоматического использования без интерактива.
        
        Args:
            post: Пост для обработки
            title_handler_key: Ключ обработчика заголовка
            content_handler_key: Ключ обработчика контента
            
        Returns:
            Обработанный пост
        """
        if title_handler_key and title_handler_key in self.title_handlers:
            post.add_history(f"Применяется обработчик заголовка: {title_handler_key}")
            self.title_handlers[title_handler_key].handle(post)
        
        if content_handler_key and content_handler_key in self.content_handlers:
            post.add_history(f"Применяется обработчик контента: {content_handler_key}")
            self.content_handlers[content_handler_key].handle(post)
        
        post.add_history("Обработка завершена")
        return post
    

# Пример использования
def main():
    # Создаём процессор
    processor = BlogProcessor()
    
    # Создаём пост
    post = Post(title="Паттерны в Python", content="Простые решения часто лучше сложных!")
    
    # Вариант 1: Интерактивное использование (пользователь выбирает обработчики)
    processed_post = processor.process_post_interactive(post)
    
    # Выводим результат
    print("\nРезультат:")
    print(f"Заголовок: {processed_post.title}")
    print(f"Контент: {processed_post.content}")
    print("\nИстория обработки:")
    for entry in processed_post.history:
        print(f"- {entry}")

    # Вариант 2: Программное использование (для автоматизации)
    # another_post = Post(title="Весна 2025", content="Python 3.13 уже вышел!")
    # auto_processed = processor.process_post(another_post, "B", "A")
    # ... и так далее

if __name__ == "__main__":
    main()