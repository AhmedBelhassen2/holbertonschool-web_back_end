-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    UPDATE users
    SET corrections (user_id) VALUES (user_id, (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
    WHERE id = user_id;
END$$