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
		tuple_results = cursor.fetchall()

		#Convert results to array
		results = []
		for result in tuple_results:
			results.append(result)

		return results

	def show_users(self):
		query = "SELECT first_name, last_name, username FROM Users"
		result = self._run_query(query, [])
		print("Users:")
		for (first_name, last_name, username) in result:
			print(username)
		print("--------")

	def get_users(self):
		query = "SELECT username, phone FROM Users"
		result = self._run_query(query, [])
		print(result)
		return result

	def add_user(self, username, password, phone):
		query = "INSERT INTO Users (username, password, phone) VALUES (%s, %s, %s)"
		parameters = [username, password, phone]
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

	def authenticate_user(self, username, password):
		query = "SELECT username FROM Users WHERE username = %s AND password = %s"
		parameters = [username, password]
		result = self._run_query(query, parameters)
		return len(result) > 0
		

	def get_approved_events(self, time_diff):
		query = "SELECT uuid, time_stamp FROM Events WHERE is_food = 'Y' AND time_stamp > NOW() - INTERVAL %s MINUTE"
		return self._run_query(query, [time_diff])

	def get_unapproved_events(self, time_diff):
		query = "SELECT uuid, time_stamp FROM Events WHERE is_food = '?' AND time_stamp > NOW() - INTERVAL %s MINUTE ORDER BY time_stamp"
		return self._run_query(query, [time_diff])

	def approve_event(self, uuid):
		query = "UPDATE Events SET is_food = 'Y' WHERE uuid = %s"
		result = self._run_query(query, [uuid])
		print(result)
	def approve_all_event(self, uuid_list):
		for uuid in uuid_list:
			self.approve_event(uuid)

	def new_event(self):
		query = "INSERT INTO Events (is_food) VALUES ('?')"
		result = self._run_query(query, [])
		print(result)
def main():

	db_link = dbLink()
	#db_link.add_user("Rory", "viasat", "5713574662")
	db_link.make_admin("Rory")
	#db_link.add_user("Yoonshik", "ILuvChineseFood", "7037577461")
	db_link.get_users()
	db_link.show_users()
	print("Getting admins")
	db_link.get_admins()

	print(db_link.authenticate_user("Rory", "viasat"))
	print(db_link.authenticate_user("Rory", "hacker"))

	print("Testing events system")
	db_link.new_event()
	print("Getting unapproved events")
	unapproved = db_link.get_unapproved_events(time_diff=10)
	for (uuid, time_stamp) in unapproved:
		print(str(uuid) + ":" + str(time_stamp))
		db_link.approve_event(uuid)
	print("Getting approved events")
	print(db_link.get_approved_events(2))

if __name__ == "__main__":
	main()
