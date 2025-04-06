"""
Lesson 33 - Паттерны проектирования на ООП
- Абстрактная фабрика
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

"""
Абстрактная фабрика на примере имитации библиотеки работы с разными БД
- SQLite
- PostgreSQL

Продукты
- Простой запрос в БД
- Вызов оконной функции


- Описание классов
- Абстрактная фабрика SQL подключний
- Фабрика подключения к SQLite
- Фабрика подключения к PostgreSQL

- Абстрактный класс простого запроса
- Абстрактный класс оконной функции
- Простой запрос SQLite
- Простой запрос PostgreSQL
- Оконная функция SQLite
- Оконная функция PostgreSQL 
"""

# Абстрактный "Продукт" - Простой SQL запрос

class AbstractSimpleQuery(ABC):
    """
    Абстрактный класс простого SQL запроса.
    """
    @abstractmethod
    def execute(self):
        """
        Выполнение простого SQL запроса.
        """
        pass

# Абстрактный "Продукт" - Оконная функция SQL
class AbstractWindowFunction(ABC):
    """
    Абстрактный класс оконной функции SQL.
    """
    @abstractmethod
    def execute_window_function(self):
        """
        Выполнение оконной функции SQL.
        """
        pass

# Реальные "продукты" - Простой SQL запрос для SQLite
class SQLiteSimpleQuery(AbstractSimpleQuery):
    """
    Реализация простого SQL запроса для SQLite.
    """
    def execute(self):
        print(f'Выполняется простой SQL запрос для SQLite классом {self.__class__.__name__}')


# Реальные "продукты" - Простой SQL запрос для PostgreSQL
class PostgreSQLSimpleQuery(AbstractSimpleQuery):
    """
    Реализация простого SQL запроса для PostgreSQL.
    """
    def execute(self):
        print(f'Выполняется простой SQL запрос для PostgreSQL классом {self.__class__.__name__}')

# Реальные "продукты" - Оконная функция для SQLite
class SQLiteWindowFunction(AbstractWindowFunction):
    """
    Реализация оконной функции для SQLite.
    """
    def execute_window_function(self):
        print(f'Выполняется оконная функция для SQLite классом {self.__class__.__name__}')


# Реальные "продукты" - Оконная функция для PostgreSQL
class PostgreSQLWindowFunction(AbstractWindowFunction):
    """
    Реализация оконной функции для PostgreSQL.
    """
    def execute_window_function(self):
        print(f'Выполняется оконная функция для PostgreSQL классом {self.__class__.__name__}')


# Абстрактная фабрика SQL подключения
class AbstractSQLConnectionFactory(ABC):
    """
    Абстрактная фабрика SQL подключения.
    """
    @abstractmethod
    def create_simple_query(self) -> AbstractSimpleQuery:
        """
        Создание простого SQL запроса.
        """
        pass

    @abstractmethod
    def create_window_function(self) -> AbstractWindowFunction:
        """
        Создание оконной функции SQL.
        """
        pass

# Фабрика подключения к SQLite
class SQLiteConnectionFactory(AbstractSQLConnectionFactory):
    """
    Фабрика подключения к SQLite.
    """
    def create_simple_query(self) -> AbstractSimpleQuery:
        return SQLiteSimpleQuery()

    def create_window_function(self) -> AbstractWindowFunction:
        return SQLiteWindowFunction()
    

# Фабрика подключения к PostgreSQL
class PostgreSQLConnectionFactory(AbstractSQLConnectionFactory):
    """
    Фабрика подключения к PostgreSQL.
    """
    def create_simple_query(self) -> AbstractSimpleQuery:
        return PostgreSQLSimpleQuery()

    def create_window_function(self) -> AbstractWindowFunction:
        return PostgreSQLWindowFunction()
    

# Пример использования
def main():
    # Словарь с фабриками подключения
    factories = {
        'sqlite': SQLiteConnectionFactory,
        'postgresql': PostgreSQLConnectionFactory
    }

    # Выбор фабрики подключения
    choice = input("Выберите тип подключения (sqlite/postgresql): ").strip().lower()
    factory = factories.get(choice)
    if not factory:
        print("Неверный выбор подключения.")
        return
    
    # Создание фабрики подключения
    connection_factory = factory()
    simple_query = connection_factory.create_simple_query()
    window_function = connection_factory.create_window_function()

    # Выполнение простого SQL запроса
    simple_query.execute()
    # Выполнение оконной функции SQL
    window_function.execute_window_function()

if __name__ == "__main__":
    main()