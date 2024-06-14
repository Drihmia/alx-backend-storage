-- A SQL script that creates a stored procedure called:
-- ComputeAverageWeightedScoreForUser
-- that computes and store the  average weighted score for a student.
-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (assumimg user_id is linked to an existing users)

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
-- Begin main body
main_block: BEGIN

-- max_users based on the highest ID value
DECLARE max_users INT DEFAULT NULL;

-- n would represent user_id in the loop
DECLARE n INT DEFAULT 1;

DECLARE average_weight FLOAT DEFAULT 0;

-- getting the maximum ID from users table.
SELECT MAX(id) INTO max_users FROM users;

-- check if max_users is not null or zero
IF max_users IS NULL OR max_users = 0 THEN
    LEAVE main_block;
END IF;

-- ---------Starting the loop ---------
main_loop: LOOP

IF n > max_users THEN
    LEAVE main_loop;
END IF;

-- if n is not an ID of any user
IF n NOT IN (SELECT id FROM users) THEN
    SET n = n + 1;
    ITERATE main_loop;
END IF;


-- performe A (SUMPRODUCT/ SUM of weights) function similar in Excel
SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
INTO average_weight
FROM corrections
INNER JOIN projects
    ON corrections.project_id = projects.id
WHERE corrections.user_id = n;


-- Update its average_score in the users table.
UPDATE users
SET average_score = average_weight
WHERE id = n;

-- reset average_weight for next loop
set average_weight = 0;

-- increment n by 1
set n = n + 1;

-- end main_loop
END LOOP;

-- END main body
END main_block$$
-- reset the delimiter to semiculomn
DELIMITER ;
