CREATE DATABASE lolalabartola_bot;

USE lolalabartola_bot;

CREATE TABLE animal(
    id_animal int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_animal varchar(100) NOT NULL,
    cartucho varchar(50) NOT NULL,
    calibre varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO animal (nombre_animal, cartucho, calibre)
VALUES ('venado jabali codorniz',' alta velocidad, posta. No. 00B', 'Calibre 12'),
('alta velocidad munición. No. 2,4,6,71/2,8,9','pato ganso liebre conejo','Calibre 12'),
('Cartucho: velocidad std munición No 2,4,6,71/2,8,9','pato faisan codorniz','Calibre 12');

SHOW TABLES;

SELECT * FROM animal;

DESCRIBE animal;

CREATE USER 'agus'@'localhost' IDENTIFIED BY 'agus.2019';
GRANT ALL PRIVILEGES ON lolalabartola_bot.* TO 'agus'@'localhost';
FLUSH PRIVILEGES;
