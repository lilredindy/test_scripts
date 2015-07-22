

import psycopg2
import time

def foo2():
	print "foo2"

class Foo():

	def foo1(self):
		print "foo1"
		x = foo2()
		def foo3():
			x()
			print "hello"

		return foo3()



#Define our connection string
conn_string = "host='localhost' dbname='booktown' user='postgres' password='maverick'"

# print the connection string we will use to connect
print "Connecting to database\n ->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

while (True):
	time.sleep(1)