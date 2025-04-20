SELECT name, eye_id
FROM MarvelCharacters;

SELECT name, color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id;

SELECT MarvelCharacters.name, EyeColor.color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id;

SELECT mc.name, ec.color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id;

SELECT mc.name AS character_name, ec.color AS eye_color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id;


SELECT mc.id AS character_id, mc.name AS character_name, mc.eye_id AS mc_eye_id,
ec.eye_id AS eye_id, ec.color AS eye_color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id;