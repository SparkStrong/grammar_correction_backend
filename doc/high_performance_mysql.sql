
CREATE TABLE People (
  last_name VARCHAR(50) NOT NULL ,
  first_name VARCHAR(50) NOT NULL ,
  dob DATE NOT NULL ,
  gender ENUM('m', 'f') NOT NULL ,
  KEY (last_name, first_name, dob)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

SELECT * FROM People WHERE to_days(current_date) - to_days(date_col) <= 10;