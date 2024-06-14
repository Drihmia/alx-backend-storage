-- A SQL script that creates a stored procedure called:
-- ComputeAverageWeightedScoreForUser
-- that computes and store the  average weighted score for a student.
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (assumimg user_id is linked to an existing users)

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    p_user_id INT
)
-- Begin main body
BEGIN
DECLARE average_weight FLOAT DEFAULT 0;

-- performe A (SUMPRODUCT/ SUM of weights) function similar in Excel
SELECT SUM(score * weight) / SUM(weight)
INTO average_weight
FROM (
    -- Get a table of two fields : score and project's
    -- weight using inner join
    SELECT
        corrections.score,
        projects.weight
    FROM corrections, projects
    WHERE corrections.project_id = projects.id
    AND corrections.user_id = p_user_id
    ) AS red;

-- Update its average_score in the users table.
UPDATE users
SET average_score = average_weight
WHERE id = p_user_id;
END$$
-- END main body
DELIMITER ;
