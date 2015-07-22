from locust import Locust, TaskSet, task, events
import time
import xmlrpclib

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
		pass

	@task(2)
	def task1(self):
		print "task1"

	@task(2)
	def select_customers(self):
		#foo = self.client.db_test()
		foo = self.client.__getattr__('db_test')
		print foo
		foo()


class DBLocust(Locust):
	def __init__(self):
		host = "http://127.0.0.1:8877/"
		self.client = DBClient(host)

	task_set = UserBehavior

