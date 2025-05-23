import sqlite3 as sl3

SQL_SCRIPT = "./lesson_43.sql"
DB_FILE = r"./data/academy_orm.db"

# 1. Читаем SQL файл и берем скрипты на создание таблиц и наполнение данными
with open(SQL_SCRIPT, "r", encoding="utf-8") as file:
    sql_script = file.read()


# 2. Создаем подключение к базе данных и выполняем весь скрипт
try:
    with sl3.connect(DB_FILE) as connection:
        connection.executescript(sql_script)
        print("База данных успешно создана!")
except sl3.Error as e:
    print(f"Ошибка при выполнении SQL скрипта: {e}")


# Альтернативный способ - по командам (если нужна детальная диагностика)
# # 2. Разбиваем SQL-скрипт на отдельные команды по символу ";"
# list_of_sql_commands = sql_script.split(";")

# # [print(command + '\n\n---------------') for command in list_of_sql_commands]

# # Выполняем команды в цикле, и печатаем ошибку + команду которая дала ошибку
# for command in list_of_sql_commands:
#     try:
#         with sl3.connect(DB_FILE) as connection:
#             cursor = connection.cursor()
#             cursor.execute(command)
#     except sl3.Error as e:
#         print(f"Ошибка при выполнении команды: {command}\n{e}")
#         # raise # Передаем исключение выше, чтобы обработать его в вызывающем коде
#     finally:
#         # Закрываем курсор
#         cursor.close()
