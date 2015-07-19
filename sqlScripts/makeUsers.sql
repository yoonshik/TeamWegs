CREATE TABLE IF NOT EXISTS FoodTracker.Users (
	uuid int PRIMARY KEY AUTO_INCREMENT,
	first_name varchar(100) NULL,
	last_name varchar(250) NULL,
	username varchar(100) NOT NULL UNIQUE,
	password varchar(300) NOT NULL,
	is_admin BIT(1) NOT NULL DEFAULT 0
	);

SHOW COLUMNS FROM FoodTracker.Users;
