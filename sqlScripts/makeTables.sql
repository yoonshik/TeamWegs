CREATE TABLE IF NOT EXISTS FoodTracker.Users (
        uuid int PRIMARY KEY AUTO_INCREMENT,
        first_name varchar(100) NULL,
        last_name varchar(250) NULL,
        username varchar(100) NOT NULL UNIQUE,
	phone varchar(30) NOT NULL UNIQUE,
        password varchar(300) NOT NULL,
        is_admin BIT(1) NOT NULL DEFAULT 0
);

SHOW COLUMNS FROM FoodTracker.Users;

CREATE TABLE IF NOT EXISTS FoodTracker.Events (
	uuid int PRIMARY KEY AUTO_INCREMENT,
	time_stamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	is_food char(1) DEFAULT '?'
);

SHOW COLUMNS FROM FoodTracker.Events;
