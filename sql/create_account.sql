CREATE USER 'speedrunner'@'localhost' IDENTIFIED BY 'for_glory';
GRANT ALL PRIVILEGES ON speedruns.* TO 'speedrunner'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
