from locust import Locust, TaskSet, task,events
import time

class MyTaskSet(TaskSet):
    @task
    def my_task(l):
    	#time.sleep(10)
        print "executing my_task"
        events.request_success.fire(request_type="basic", name="my_task", response_time=0, response_length=0)

class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 1000	