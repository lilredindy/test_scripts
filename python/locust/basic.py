from locust import Locust, TaskSet, task

import psycopg2
import pprint


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        #Define our connection string
        conn_string = "host='localhost' dbname='booktown' user='postgres' password='maverick'"

        # print the connection string we will use to connect
        print "Connecting to database\n ->%s" % (conn_string)

        # get a connection, if a connect cannot be made an exception will be raised here
        self.conn = psycopg2.connect(conn_string)

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        self.cursor = self.conn.cursor()
        print "Connected!\n"
        

    @task(2)
    def task1(self):
        print "task1"


    @task(2)
    def select_customers(self):
		# execute our Query
		self.cursor.execute("SELECT * FROM customers")
 
		# retrieve the records from the database
		records = self.cursor.fetchall()
	 
		# print out the records using pretty print
		# note that the NAMES of the columns are not shown, instead just indexes.
		# for most people this isn't very useful so we'll show you how to return
		# columns as a dictionary (hash) in the next example.
		print(records)

class DBLocust(Locust):

	task_set = UserBehavior

