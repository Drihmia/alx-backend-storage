-- A SQL script that creates a stored procedure AddBonus that adds
-- a new correction for a student.
-- Requirements:
-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (assuming user_id is linked to an existing users)
-- project_name, a new or already exists projects
-- if no projects.name found in the table, I should create it
-- score, the score value for the correction.
DELIMITER $$

CREATE PROCEDURE AddBonus(
    user_id INT,
    project_name VARCHAR(255),
    score INT
)
-- Begin main body
BEGIN
    DECLARE project_id INT DEFAULT NULL;

    -- Finding the project's id by its name 
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;

    -- If project does not exist, create new one
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Inesrt the correction record
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END$$
-- end begin main body

DELIMITER ;
