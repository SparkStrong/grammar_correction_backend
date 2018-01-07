
DROP DATABASE IF EXISTS `grammar_correction`;
CREATE DATABASE `grammar_correction` CHARACTER SET utf8;

USE grammar_correction;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '自增长id',
  `user_name` varchar(64) NOT NULL,
  `password` varchar(128) NOT NULL,
  `user_type` INT NOT NULL DEFAULT(0) COMMENT '用户类型，0是普通用户，1是教师用户'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

# DROP TABLE IF EXISTS `teacher`;
# CREATE TABLE `teacher` (
#   `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '自增长id',
#   `user_name` varchar(64) NOT NULL
# ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `feedback_results`;
CREATE TABLE `feedback_result` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '自增长id',
  `user_name` varchar(64) NOT NULL,
  `original_text` TEXT COMMENT '原始错误文本',
  `system_correction_result` TEXT COMMENT '系统纠错结果',
  `user_correction_suggestion` TEXT COMMENT '用户修改建议'
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;