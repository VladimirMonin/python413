-- Lesson 36: Знакомство с Group By и Aggregate Functions

-- 1. Получили уникальные значения по цвету волос 2мс
SELECT DISTINCT HAIR
FROM MarvelCharacters;

-- 2. Вроде бы тоже самое, но БД будет хранить данные о каждом уникальном значении (соберет их в группы)
-- Выполнятся почти в 3 раза дольше! - другие алгоритмы
SELECT HAIR
FROM MarvelCharacters
GROUP BY HAIR;

-- 3. Функция COUNT - подсчет количества строк в таблице
-- COUNT(*) - подсчет всех строк в таблице
SELECT COUNT(*)
FROM MarvelCharacters;

-- 4. Подсчет количества строк в таблице, где есть значение в столбце HAIR
-- Передав аргумент в COUNT, мы получаем количество строк, где есть значение в этом столбце
SELECT COUNT(HAIR)
FROM MarvelCharacters;

-- 5. Подсчет количества строк в таблице, где есть значение в столбце HAIR и это значение 'Bald'
-- COUNT(HAIR) - подсчет всех строк, где есть значение в столбце HAIR и это значение 'Bald'
SELECT COUNT(HAIR)
FROM MarvelCharacters
WHERE HAIR = 'Bald';

-- 6. Подсчет уникальных значений в столбце HAIR
SELECT COUNT(DISTINCT HAIR)
FROM MarvelCharacters;

-- 7. Вывод названия и подсчет лысых
SELECT HAIR, COUNT(HAIR)
FROM MarvelCharacters
WHERE HAIR = 'Bald';

-- 8. Первый зарпос с группировкой. Считаем сколько персонажей с каждым цветом волос
SELECT HAIR, COUNT(*)
FROM MarvelCharacters
GROUP BY HAIR
ORDER BY COUNT(*) DESC;

-- 9. Считаем сколько персонажей с каждым цветом волос, но только тех, у кого есть значение в этом столбце
SELECT HAIR, COUNT(*) AS hair_count
FROM MarvelCharacters
WHERE HAIR IS NOT NULL
GROUP BY HAIR
ORDER BY hair_count DESC;

--TODO: Напишите подобный запрос для цвета глаз
-- 10.
SELECT EYE, COUNT(*) AS eye_count
FROM MarvelCharacters
WHERE EYE IS NOT NULL
GROUP BY EYE
ORDER BY eye_count DESC;

-- SUM - сумма значений в столбце
-- 11. Группировка по цвету глаз, подсчет кол-ва персонажей, а так же же суммы APPEARANCES

SELECT EYE, COUNT(*) AS eye_count, SUM(APPEARANCES) AS total_appearances
FROM MarvelCharacters
WHERE EYE IS NOT NULL
GROUP BY EYE
ORDER BY total_appearances DESC;


-- TODO - Сделайте группировку по году. Посчитайте кол-во персонажей в каждом году
SELECT year, COUNT(*) AS year_count
FROM MarvelCharacters
GROUP BY year
ORDER BY year_count DESC;


SELECT year, COUNT(*) AS year_count, SUM(APPEARANCES) AS total_appearances
FROM MarvelCharacters
GROUP BY year
ORDER BY total_appearances DESC;



SELECT year, COUNT(*) AS year_count, name
FROM MarvelCharacters
GROUP BY year
ORDER BY year_count DESC;



-- avg() — вычисляет среднее значение
-- count() — подсчитывает количество строк или значений
-- group_concat() — объединяет строки с разделителем
-- max() — находит максимальное значение
-- min() — находит минимальное значение
-- sum() — вычисляет сумму значений
-- total() — аналогична sum(), но преобразует целые числа в вещественные

SELECT year, COUNT(*) AS year_count, MAX(APPEARANCES) AS max_appearances, ROUND(AVG(APPEARANCES), 2) AS avg_appearances, SUM(APPEARANCES) AS total_appearances
FROM MarvelCharacters
GROUP BY year;


-- TODO - Сделайте группировку по identify - Посчитайте количество персонажей 
-- TODO - Сделайте группировку по Alive - Посчитайте количество персонажей, сделайте сортировку по количеству персонажей


-- ПОДЗАПРОСЫ
-- Это возможность сделать запрос внутри запроса
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > AVG(APPEARANCES)
ORDER BY APPEARANCES DESC;


SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > (
    SELECT AVG(APPEARANCES)
    FROM MarvelCharacters
)
ORDER BY APPEARANCES DESC;

-- CTE - Common Table Expression
-- Это возможность сделать запрос внутри запроса, но более читабельно

WITH AverageAppearances AS (
    SELECT AVG(APPEARANCES) AS avg_appearances
    FROM MarvelCharacters
)

SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > (SELECT avg_appearances FROM AverageAppearances)
ORDER BY APPEARANCES DESC;


WITH AverageAppearances AS (
    SELECT AVG(APPEARANCES) AS avg
    FROM MarvelCharacters
)
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > (SELECT avg FROM AverageAppearances)
ORDER BY APPEARANCES DESC;




SELECT 
    Year,
    COUNT(*) AS num_characters,
    SUM(APPEARANCES) AS total_appearances,
    MAX(APPEARANCES) AS max_appearances,
    ROUND(AVG(APPEARANCES), 2) AS avg_appearances,
    (SELECT name
     FROM MarvelCharacters marvel_character_2
     WHERE marvel_character_2.Year = marvel_character_1.Year
     ORDER BY APPEARANCES DESC
     LIMIT 1) AS most_frequent_character
FROM MarvelCharacters marvel_character_1
WHERE Year IS NOT NULL
GROUP BY Year
ORDER BY COUNT(*) DESC;

WITH CharactersWithYears AS (
    SELECT *
    FROM MarvelCharacters
    WHERE Year IS NOT NULL
),
PopularCharactersByYear AS (
    SELECT 
        Year,
        name,
        APPEARANCES,
        ROW_NUMBER() OVER (PARTITION BY Year ORDER BY APPEARANCES DESC) as popularity_rank
    FROM CharactersWithYears
);


================== Marvel Normal ==============

-- Получить имена и цвета глаз
SELECT name, eye_id
FROM MarvelCharacters;

SELECT eye_id, color
FROM EyeColor
WHERE eye_id = 1;

SELECT name, color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id
