-- Lesson 39 - Создание собственной системы таблиц 
-- Students - Таблица студентов
-- Groups - Таблица групп
-- Teachers - Таблица преподавателей
-- TeacherGroups - Таблица групп преподавателей
-- StudentsCards - Таблица студенческих карточек

-- Удаление старых таблиц
DROP TABLE IF EXISTS Groups;
DROP TABLE IF EXISTS Students;

-- 1. Таблица групп студентов
CREATE TABLE
    IF NOT EXISTS Groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name TEXT NOT NULL UNIQUE,
        start_date DATE DEFAULT CURRENT_TIMESTAMP,
        end_date DATE
    );

-- 2. Таблица студентов
CREATE TABLE
    IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        middle_name TEXT,
        last_name TEXT NOT NULL,
        age INTEGER DEFAULT 0,
        group_id INTEGER DEFAULT NULL,
        FOREIGN KEY (group_id) REFERENCES Groups (id)
    );

-- 3. Добавление групп в БД
INSERT INTO
    Groups (group_name)
VALUES
    ('python411'),
    ('python412'),
    ('python413');

INSERT INTO Students (first_name, middle_name, last_name, age, group_id)
VALUES 
('Светозара', 'Питоновна', 'Джангова', 20, (SELECT id FROM Groups WHERE group_name = 'python412')),
('Кодислав', 'Гитович', 'Коммитов', 21, (SELECT id FROM Groups WHERE group_name = 'python412')),
('Серверина', 'Базоданных', 'Селектова', 22, (SELECT id FROM Groups WHERE group_name = 'python412')),
('Фронтендий', 'Вебович', 'Реактов', 23, (SELECT id FROM Groups WHERE group_name = 'python412')),
('Линуксина', 'Убунтовна', 'Баширова', 24, (SELECT id FROM Groups WHERE group_name = 'python412')),
('Алгоритм', 'Сортирович', 'Рекурсионов', 23, (SELECT id FROM Groups WHERE group_name = 'python413')),
('Нейросеть', 'Вижновна', 'Трансформерова', 23, (SELECT id FROM Groups WHERE group_name = 'python413')),
('Блокчейн', 'Криптович', 'Токенов', 23, (SELECT id FROM Groups WHERE group_name = 'python413')),
('Явана', 'Скриптовна', 'Ноутация', 23, (SELECT id FROM Groups WHERE group_name = 'python413')),
('Облакос', 'Докерович', 'Кубернетов', 23, (SELECT id FROM Groups WHERE group_name = 'python413'));

