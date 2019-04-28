CREATE DATABASE speedruns;
USE speedruns;

CREATE TABLE `Game`
(
  `game_id` int PRIMARY KEY,
  `game` varchar(255),
  `create_date` datetime,
  `modify_date` datetime
);

CREATE TABLE `Category`
(
  `category_id` int PRIMARY KEY,
  `category` varchar(255),
  `create_date` datetime,
  `modify_date` datetime
);

CREATE TABLE `GameCategoryMap`
(
  `gamecategorymap_id` int PRIMARY KEY,
  `game_id` int,
  `category_id` int,
  `create_date` datetime,
  `modify_date` datetime
);

CREATE TABLE `Player`
(
  `player_id` int PRIMARY KEY,
  `Player` varchar(255),
  `create_date` datetime,
  `modify_date` datetime
);

CREATE TABLE `SpeedRun`
(
  `speedrun_id` int PRIMARY KEY,
  `game_id` int,
  `player_id` int,
  `duration` time,
  `create_date` datetime,
  `modify_date` datetime
);

ALTER TABLE `GameCategoryMap` ADD FOREIGN KEY (`game_id`) REFERENCES `Game` (`game_id`);

ALTER TABLE `GameCategoryMap` ADD FOREIGN KEY (`category_id`) REFERENCES `Category` (`category_id`);

ALTER TABLE `SpeedRun` ADD FOREIGN KEY (`game_id`) REFERENCES `Game` (`game_id`);

ALTER TABLE `SpeedRun` ADD FOREIGN KEY (`player_id`) REFERENCES `Player` (`player_id`);
