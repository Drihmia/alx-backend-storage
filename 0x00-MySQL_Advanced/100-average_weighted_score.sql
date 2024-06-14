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
SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
INTO average_weight
FROM corrections
INNER JOIN projects
    ON corrections.project_id = projects.id
WHERE corrections.user_id = p_user_id;


-- Update its average_score in the users table.
UPDATE users
SET average_score = average_weight
WHERE id = p_user_id;
END$$
-- END main body
DELIMITER ;
