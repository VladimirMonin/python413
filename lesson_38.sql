-- Lesson 38 - Создание собственной системы таблиц 
-- Students - Таблица студентов
-- Groups - Таблица групп
-- Teachers - Таблица преподавателей
-- TeacherGroups - Таблица групп преподавателей
-- StudentsCards - Таблица студенческих карточек




-- 1. 
-- Students создать если не существует
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER DEFAULT 0,
    group_name TEXT NOT NULL
);

-- 2. Добавляем одного студента в БД
INSERT INTO Students (first_name, last_name, group_name)
VALUES ('Филлип', 'Киркоров', 'python411');

INSERT INTO Students (first_name, middle_name, last_name, age, group_name)
-- Перечисляем 5 студентов в группу python412
VALUES 
('Светозара', 'Питоновна', 'Джангова', 20, 'python412'),
('Кодислав', 'Гитович', 'Коммитов', 21, 'python412'),
('Серверина', 'Базоданных', 'Селектова', 22, 'python412'),
('Фронтендий', 'Вебович', 'Реактов', 23, 'python412'),
('Линуксина', 'Убунтовна', 'Баширова', 24, 'python412'),
-- Еще 5 в 413 группу
('Алгоритм', 'Сортирович', 'Рекурсионов', 23, 'python413'),
('Нейросеть', 'Вижновна', 'Трансформерова', 23, 'python413'),
('Блокчейн', 'Криптович', 'Токенов', 23, 'python413'),
('Явана', 'Скриптовна', 'Ноутация', 23, 'python413'),
('Облакос', 'Докерович', 'Кубернетов', 23, 'python413');


-- 3. Создадим еще одного лишнего студента в группу python413
INSERT INTO Students (first_name, last_name, group_name)
VALUES ('Филлип', 'Киркоров', 'python413');

-- -- 4. Удалим лишнего студента из группы python413
-- DELETE FROM Students
-- WHERE first_name = 'Филлип' AND last_name = 'Киркоров' AND group_name = 'python413';

DELETE FROM Students
WHERE id = 666;

DELETE FROM Students
WHERE id = (SELECT id 
            FROM Students 
            WHERE first_name = 'Филлип' 
                AND last_name = 'Киркоров' 
                AND group_name = 'python413'
            LIMIT 1);


-- 5. Удалим по вхождению в кортеж ID
DELETE FROM Students
WHERE id IN (23, 2);

-- 6. Обновим данные студента ID 1
UPDATE Students
SET middle_name = 'Бедросович', age = 45
WHERE id = 1;

-- 7. Создание таблицы Groups

CREATE TABLE IF NOT EXISTS Groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL UNIQUE,
    start_date DATE DEFAULT CURRENT_TIMESTAMP,
    end_date DATE
);

-- 8. Добавляем группы в БД
INSERT INTO Groups (group_name)
VALUES 
('python411'),
('python412'),
('python413');

------------ Нормализация таблицы студентов -------------
-- Так как SQLITE не поддерживает переименование и удаление столбцов, нам нужно 
-- 1. Создать таблицу StudentsNew с нужными столбцами
-- 2. Убедится что все группы из Students есть в Groups
-- 3. Пернести данные из Students в StudentsNew
-- 4. Удалить таблицу Students
-- 5. Переименовать StudentsNew в Students

-- 1. Создаем таблицу StudentsNew с нужными столбцами
CREATE TABLE IF NOT EXISTS StudentsNew (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER DEFAULT 0,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES Groups(id)
);

-- DROP TABLE IF EXISTS StudentsNew;

-- 3. Выбираем из Students Вставляем данные из Students в StudentsNew. Для group_id нужен подзапрос
-- который вернет id группы по ее имени

INSERT INTO StudentsNew (id, first_name, middle_name, last_name, age, group_id)
SELECT s.id, s.first_name, s.middle_name, s.last_name, s.age, g.id
FROM Students AS s
JOIN Groups AS g ON s.group_name = g.group_name;

-- 4. Удаляем таблицу Students
DROP TABLE IF EXISTS Students;

-- 5. Переименовываем StudentsNew в Students
ALTER TABLE StudentsNew RENAME TO Students;


-- Выборка, обновление, удаление и вставка связанных данных
-- Многие ко многим
-- Выборка, обновление, удаление и вставка связанных данных m-to-m
-- Индексы