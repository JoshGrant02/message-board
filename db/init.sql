CREATE DATABASE messageboard;
use messageboard;

-- SCHEMA
CREATE TABLE message (
    messageId INT NOT NULL AUTO_INCREMENT,
    message VARCHAR(200) NOT NULL,
    createdWhen TIMESTAMP NOT NULL,
    createdWho VARCHAR(50) NOT NULL,
    PRIMARY KEY (messageId)
);

DELIMITER //

-- CREATE MESSAGE
CREATE PROCEDURE message_i (
    message_p VARCHAR(200),
    createdWhen_p TIMESTAMP,
    createdWho_p VARCHAR(50)
)
BEGIN
    INSERT INTO message
    (
        message,
        createdWhen,
        createdWho
    )
    VALUES
    (
        message_p,
        createdWhen_p,
        createdWho_p
    );
END //

-- GET MESSAGES
CREATE PROCEDURE message_s()
BEGIN
    SELECT messageId, message, createdWhen, createdWho
    FROM message ORDER BY createdWhen desc;
END //

-- CREATE INITIAL MESSAGES
INSERT INTO message (message, createdWhen, createdWho) VALUES 
('Welcome', '2024-10-20 14:30:00', 'Admin'),
('This is a message', '2024-10-20 14:31:00', 'Josh') //