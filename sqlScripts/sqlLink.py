#!/usr/bin/python
import pymysql

class dbLink:

	def __init__(self):
		self.SQL_CON = pymysql.connect(host='localhost', user='root', db="FoodTracker")
		print("Connected to SQL Server as root")

	def _run_query(self, query, parameters):
		cursor = self.SQL_CON.cursor()
		cursor.execute(query, parameters)
		self.SQL_CON.commit()
		return cursor.fetchall()

	def show_users(self):
		query = "SELECT first_name, last_name, username FROM Users"
		result = self._run_query(query, [])
		print("Users:")
		for (first_name, last_name, username) in result:
			print(username)
		print("--------")

	def add_user(self, username, password):
		query = "INSERT INTO Users (username, password) VALUES (%s, %s)"
		parameters = [username, password]
		result = self._run_query(query, parameters)

	def make_admin(self, username):
		query = "UPDATE Users SET is_admin = 1 WHERE username=%s"
		parameters = [username]
		result = self._run_query(query, parameters)
	
	def get_admins(self):
		query = "SELECT username FROM Users WHERE is_admin = 1"
		result = self._run_query(query, [])
		print(result)
		return result
def main():
	db_link = dbLink()
	db_link.show_users()
	#db_link.add_user("Rory", "viasat")
	#db_link.make_admin("Rory")
	#db_link.add_user("Yoonshik", "ILuvChineseFood")
	db_link.get_admins()

if __name__ == "__main__":
	main()
