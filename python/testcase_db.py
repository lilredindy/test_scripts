import unittest
import os
import sqlalchemy

class TestDB(unittest.TestCase):

	def setUp(self):

		USR = "postgres"
		PWD = ""
		SQLALCHEMY_DATABASE_URI = 'postgres://{}:{}@localhost:5432/postgres'.format(USR, PWD)
		print SQLALCHEMY_DATABASE_URI
   		if not SQLALCHEMY_DATABASE_URI:
   			self.skipTest("No database URL set")
   		self.engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)
   		self.connection = self.engine.connect()

	def test_1(self):
		print "hello"
		result= self.connection.execute("select * from pg_user")
		print type(result), result	
		for row in result:
			print type(row)
			print row
			l = list(row)
			print l

	def tearDown(self):
		self.connection.close()

 

if __name__ == '__main__':
	unittest.main()
