CREATE DATABASE speedrunner;
USE speedrunner;

CREATE TABLE `Games`
(
  `game_id` int AUTO_INCREMENT PRIMARY KEY,
  `game` varchar(255),
  `create_date` datetime,
  `modify_date` datetime
);

CREATE TABLE `Categories`
(
  `category_id` int AUTO_INCREMENT PRIMARY KEY,
  `category` varchar(255),
  `create_date` datetime,
  `modify_date` datetime
);

CREATE TABLE `GameCategoryMap`
(
  `gamecategorymap_id` int AUTO_INCREMENT PRIMARY KEY,
  `game_id` int,
  `category_id` int,
  `create_date` datetime,
  `modify_date` datetime
);

CREATE TABLE `Players`
(
  `player_id` int AUTO_INCREMENT PRIMARY KEY,
  `Player` varchar(255),
  `create_date` datetime,
  `modify_date` datetime
);

CREATE TABLE `SpeedRuns`
(
  `speedrun_id` int AUTO_INCREMENT PRIMARY KEY,
  `game_id` int,
  `player_id` int,
  `duration` time,
  `create_date` datetime,
  `modify_date` datetime
);

ALTER TABLE `GameCategoryMap` ADD FOREIGN KEY (`game_id`) REFERENCES `Games` (`game_id`);

ALTER TABLE `GameCategoryMap` ADD FOREIGN KEY (`category_id`) REFERENCES `Categories` (`category_id`);

ALTER TABLE `SpeedRuns` ADD FOREIGN KEY (`game_id`) REFERENCES `Games` (`game_id`);

ALTER TABLE `SpeedRuns` ADD FOREIGN KEY (`player_id`) REFERENCES `Players` (`player_id`);
