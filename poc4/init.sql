CREATE DATABASE IF NOT EXISTS dev;
CREATE DATABASE IF NOT EXISTS test;

USE dev;

CREATE TABLE IF NOT EXISTS user (
  user_id INT not null auto_increment,
  user_name varchar(500) not null,
  api_name varchar(500) not null,
  created_on timestamp not null default CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT pk_person PRIMARY KEY (user_id)
  );

INSERT INTO user (user_name, api_name) VALUES ('jitendra', 'http://service-1:6002/service');
INSERT INTO user (user_name, api_name) VALUES ('amit', 'http://service-2:6003/service');
INSERT INTO user (user_name, api_name) VALUES ('fail', 'http://service-2:6003/service3');

