import time
import random
from SimpleXMLRPCServer import SimpleXMLRPCServer

import psycopg2


def get_time():
	time.sleep(random.random())
	return time.time()


def get_random_number(low, high):
	time.sleep(random.random())
	return random.randint(low, high)

def db_test():

	#Define our connection string
	conn_string = "host='localhost' dbname='booktown' user='postgres' password='maverick'"

	# print the connection string we will use to connect
	print "Connecting to database\n ->%s" % (conn_string)

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print "Connected!\n"
	cursor.execute("SELECT * FROM customers")
	records = cursor.fetchall()
	print(records)
	return 1


server = SimpleXMLRPCServer(("localhost", 8877))
print "Listening on port 8877..."
server.register_function(get_time, "get_time")
server.register_function(get_random_number, "get_random_number")
server.register_function(db_test, "db_test")
server.serve_forever()

#for db connectivity need to have a pool of connections
