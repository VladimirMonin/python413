# Lesson 40 - Знакомство с SQLite3 встроенной библиотекой Python
import sqlite3 as sl3
# Импорт tabulate или pip install tabulate
from tabulate import tabulate


DB_FILE = r"./data/students.db"

# Создание подключения к базе данных
# Объект соединения к базе данных - ресурсоемкий объект, для функций можно сделать его глобальным
connection = sl3.connect(DB_FILE)

# Создание курсора для выполнения SQL-запросов
cursor = connection.cursor()

# Инструметы курсора:
# cursor.execute("SQL-запрос") - выполнение SQL-запроса
# cursor.fetchall() - получение всех строк результата запроса
# cursor.fetchone() - получение одной строки результата запроса
# cursor.lastrowid - получение id последней вставленной строки
# cursor.close() - закрытие курсора
# cursor.commit() - фиксация изменений в базе данных
# cursor.rollback() - откат изменений в базе данных

# Выполним запрос SELECT * FROM students
cursor.execute("SELECT * FROM students")

# Получим все строки результата запроса
students = cursor.fetchall()

# Получим названия столбцов из таблицы students
columns = cursor.execute("PRAGMA table_info(students)").fetchall()

# Список столбцов
columns_list = [column[1] for column in columns]

# Выведем результат запроса
# print("Список студентов:")
# print(students)

# Закроем курсор
cursor.close()
# Закроем соединение с базой данных
connection.close()

# Выведем результат запроса в виде таблицы
print("Список студентов:")
print(tabulate(students, headers=columns_list, tablefmt="grid", stralign="center", numalign="center"))