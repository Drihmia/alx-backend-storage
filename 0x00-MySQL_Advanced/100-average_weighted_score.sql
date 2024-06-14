-- A SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (assumimg user_id is linked to an existing users)

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    p_user_id INT
)
-- Begin main body
BEGIN
    DECLARE average float default 0;

    CREATE TEMPORARY TABLE scores (
        t_project_id INT,
        t_score INT
    )

    insert into scores (t_project_id, t_score)
    select (project_id, score)
    from corrections
    WHERE user_id = p_user_id;

    select * from scores;
END$$
-- END main body
DELIMITER ;

    -- Compute the average for a user identified by its ID
    -- from the corrections table.
/*    SELECT AVG(score) INTO average*/
    /*FROM corrections*/
    /*WHERE user_id = p_user_id;*/
    
    -- Update its average_score in the users table.
/*    UPDATE users*/
    /*SET average_score = average*/
    /*WHERE id = p_user_id;*/
