-- A SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (assumimg user_id is linked to an existing users)

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    user_id INT
)
-- Begin main body
BEGIN
    DECLARE average float default 0;

    -- Compute the average for a user identified by its ID
    -- from the corrections table.
    SELECT AVG(score) INTO average FROM corrections
    WHERE user_id = user_id;
   
    -- Update its average_score in the users table.
    UPDATE users
    SET average_score = average
    WHERE id = user_id;
END$$
-- END main body
DELIMITER ;
