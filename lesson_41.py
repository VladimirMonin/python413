"""
- executescript() - выполняет несколько SQL-команд из файла
- execute() - выполняет одну SQL-команду
"""

import sqlite3 as sl3
from tabulate import tabulate

SQL_SCRIPT = "./lesson_39.sql"
DB_FILE = r"./data/students.db"

# 1. Читаем SQL файл и берем скрипты на создание таблиц и наполнение данными
# with open(SQL_SCRIPT, "r", encoding="utf-8") as file:
#     sql_script = file.read()

# # 2. Создаем подключение к базе данных
# connection = sl3.connect(DB_FILE)

# # 3. Создаем курсор для выполнения SQL-запросов
# cursor = connection.cursor()

# # 4. Выполняем SQL-скрипт
# cursor.executescript(sql_script)

# # 5. Закрываем курсор и соединение
# cursor.close()
# connection.close()

# 1. Создаем функцию на получение данных из таблицы

def get_data_from_table(connection: sl3.Connection, sql_query: str)-> tuple:
    
    # Создаем курсор на базе соединения полученного в аргументе функции
    cursor = connection.cursor()
    try:
        # Выполняем SQL-запрос
        cursor.execute(sql_query)
        # Получаем все строки результата запроса
        data = cursor.fetchall()
        # Получаем названия столбцов из результата запроса
        columns = cursor.description
        columns_list = [column[0] for column in columns]
        return data, columns_list
    
    except sl3.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        raise # Передаем исключение выше, чтобы обработать его в вызывающем коде
    finally:
        # Закрываем курсор
        cursor.close()

def render_table(data: list, column: list, table_style: str = 'grid') -> str:
    """
    Функция для форматирования данных в виде таблицы с использованием библиотеки tabulate.
    
    :param data: Список данных для отображения.
    :param column: Список названий столбцов.
    :param table_style: Стиль таблицы (по умолчанию 'grid').
    :return: Строка с отформатированной таблицей.
    """
    return tabulate(data, headers=column, tablefmt=table_style, stralign="center", numalign="center")



# Создаем подключение к базе данных
connection = sl3.connect(DB_FILE)


# ТЕСТИРУЕМ
SQL_SCRIPT1 = "SELECT * FROM students"
SQL_SCRIPT2 = "SELECT * FROM teachers"
SQL_SCRIPT3 = "SELECT * FROM groups"

sql_scripts = [SQL_SCRIPT1, SQL_SCRIPT2, SQL_SCRIPT3]

for sql_script in sql_scripts:
    print(render_table(*get_data_from_table(connection, sql_script)))


# Функция для создания студента в БД
def create_student(connection: sl3.Connection, **student_data: str|int) -> None:
     
     # Создаем курсор
    cursor = connection.cursor()

    # Проверяем на наличие обязательных полей
    main_fields = ["first_name", "last_name"]
    if not all(field in student_data for field in main_fields):
        raise ValueError("Отсутствуют обязательные поля: first_name, last_name")
    
    # Формируем параметризованный SQL-запрос с подстановкой значений через ?
    sql_query = """
    INSERT INTO students (first_name, middle_name, last_name, age, group_id)
    VALUES (?, ?, ?, ?, ?)
    """

    # Извлекаем значения
    values = (
        student_data.get("first_name"),
        student_data.get("middle_name"),
        student_data.get("last_name"),
        student_data.get("age", None),  # Возраст может быть None
        student_data.get("group_id", None)  # ID группы может быть None
    )

    try:
        # Выполняем SQL-запрос с параметрами
        cursor.execute(sql_query, values)
        # Сохраняем изменения в базе данных
        connection.commit()
    except sl3.Error as e:
        print(f"Ошибка при добавлении студента: {e}")
        raise
    finally:
        # Закрываем курсор
        cursor.close()

# Напишем тест добавления студента

new_student = {
    "first_name": "Арагорн",
    "middle_name": "Арахорнович",
    "last_name": "Арагорнов",
    "age": 50,
    "group_id": 1
}

# Добавим студента и выведем таблицу студентов
# create_student(connection, **new_student)
# Получим данные из таблицы студентов и выведем их
data, columns = get_data_from_table(connection, SQL_SCRIPT1)
print(render_table(data, columns))
# Закрываем соединение с базой данных
connection.close()


# Универсальная функция с использованием параметризованных запросов принимающая на входе параметризованный SQL-запрос и значения для подстановки, выполняющая запрос и возвращающая результат:

def execute_query(connection: sl3.Connection, sql_query: str, params: tuple) -> tuple| None:
    # Проверяем что в запросе есть параметры
    if "?" not in sql_query:
        raise ValueError("SQL-запрос должен содержать параметры для подстановки (знак '?')")
    
    # Проверяем что количество вопросов в запросе соответствует количеству параметров
    if sql_query.count("?") != len(params):
        raise ValueError("Количество параметров не соответствует количеству знаков '?' в SQL-запросе")

    # Создаем курсор
    cursor = connection.cursor()
    try:
        cursor.execute(sql_query, params)
        # Если запрос на чтение данных (SELECT), то возвращаем результат
        if sql_query.strip().upper().startswith("SELECT"):
            # Получаем название столбцов
            columns = [description[0] for description in cursor.description]
            # Получаем все строки результата запроса
            data = cursor.fetchall()
            return data, columns
        connection.commit()
    except sl3.Error as e:
        print(f"Ошибка при выполнении запроса: {e}")
        raise
    finally:
        cursor.close()


# Пример использования функции execute_query
sql_query_1 = "SELECT * FROM students WHERE age > ?"
params_1 = (20,)

# Делаем запрос и выводим результат
connection = sl3.connect(DB_FILE)
data_1 = execute_query(connection, sql_query_1, params_1)

# Выводим данные в виде таблицы
print(render_table(*data_1))

# TODO - Напишите собственный параметризованный SQL запрос на добавление преподавателя в таблицу teachers
sql_query_2 = """
INSERT INTO teachers (first_name, last_name, subject, age)
VALUES (?, ?, ?, ?)
"""

params_2 = ("Гендальф", "Серый", "Магия", 3000)


# Посчитаем всех студентов с именем "Арагорн" через COUNT
sql_query_3 = """
SELECT COUNT(*) FROM students WHERE first_name = ?"""
params_3 = ("Арагорн",)

# Вывод на экран
data_3 = execute_query(connection, sql_query_3, params_3)
# Выводим данные в виде таблицы
print(render_table(*data_3))

# Положим результат в переменную
count_aragorn = data_3[0][0] if data_3 else 0

# 