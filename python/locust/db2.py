
from locust import Locust, TaskSet, task, events
import psycopg2
import time

class DBClient():

	def execute_query(self):
		#time.sleep(10)
		try:
			# execute our Query
			self.cursor.execute("SELECT * FROM customers")
		except:
			print "Some kind of error"
			raise
		else:
			events.request_success.fire(request_type="db_access", name="execute_query", response_time=0, response_length=0)
		
		# retrieve the records from the database
		#records = self.cursor.fetchall()
		#print(records)

	def connection(self):
		#Define our connection string
		conn_string = "host='localhost' dbname='booktown' user='postgres' password='maverick'"

		# print the connection string we will use to connect
		print "Connecting to database\n ->%s" % (conn_string)

		# get a connection, if a connect cannot be made an exception will be raised here
		self.conn = psycopg2.connect(conn_string)

		# conn.cursor will return a cursor object, you can use this cursor to perform queries
		self.cursor = self.conn.cursor()
		print "Connected!\n"


class UserBehavior(TaskSet):
	def on_start(self):
		print "start"
		self.client.connection()

	@task(2)
	def select_customers(self):
		print "select_customers"
		self.client.execute_query()


class DBLocust(Locust):
	def __init__(self):
		print "locust init"
		self.client = DBClient()
	min_wait = 1000
	max_wait = 1000
	task_set = UserBehavior

