CREATE USER 'speedrunner_admin'@'localhost' IDENTIFIED BY 'for_glory';
GRANT ALL PRIVILEGES ON speedrunner.* TO 'speedrunner_admin'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
