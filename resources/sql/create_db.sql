-- create databases
CREATE DATABASE IF NOT EXISTS `buzzvil` DEFAULT CHARACTER SET utf8;


CREATE USER `test_user`@'%' IDENTIFIED BY 'zxcsfqersdr123@~!';

GRANT ALL PRIVILEGES ON `buzzvil`.* TO 'test_user'@'%';
