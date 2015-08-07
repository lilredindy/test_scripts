from locust import Locust, TaskSet, task, events
import time
import xmlrpclib
import psycopg2

class DBClient(xmlrpclib.ServerProxy):
	def __getattr__(self, name):
		func = xmlrpclib.ServerProxy.__getattr__(self, name)
		def wrapper2(*args, **kwargs):
			start_time = time.time()
			try:	
				result = func(*args, **kwargs)
				print name, result
			except xmlrpclib.Fault as e:
				total_time = int((time.time() - start_time) * 1000)
				events.request_failure.fire(request_type="xmlrpc", name=name, response_time=total_time, exception=e)
			else:
				total_time = int((time.time() - start_time) * 1000)
				#print start_time, time.time(), total_time
				events.request_success.fire(request_type="xmlrpc", name=name, response_time=total_time, response_length=0)
				# In this example, I've hardcoded response_length=0. If we would want the response length to be 
				# reported correctly in the statistics, we would probably need to hook in at a lower level
		return wrapper2
		


class UserBehavior(TaskSet):
	def on_start(self):
		#Define our connection string
		conn_string = "host='localhost' dbname='booktown' user='postgres' password='maverick'"

		# print the connection string we will use to connect
		print "Connecting to database\n ->%s" % (conn_string)

		# get a connection, if a connect cannot be made an exception will be raised here
		conn = psycopg2.connect(conn_string)

		# conn.cursor will return a cursor object, you can use this cursor to perform queries
		cursor = conn.cursor()
		print "Connected!\n"

		self.cursor = cursor

	@task(2)
	def task1(self):
		pass

	@task(2)
	def select_customers(self):
		self.client.db_test(self.cursor)


class DBLocust(Locust):
	def __init__(self):
		host = "http://127.0.0.1:8877/"
		self.client = DBClient(host)

	task_set = UserBehavior

