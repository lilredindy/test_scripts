from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        #self.login()
        pass
            
    @task(2)
    def login(self):
        print "login"
        self.client.post("/login", {"username":"ellen_key", "password":"education"})

    @task(2)
    def index(self):
        print "index"
        self.client.get("/")

    #@task(1)
    #def resumes(self):
    #    self.client.get("/resumes")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    #the wait time btwn a single user's tasks 
    min_wait=2000
    max_wait=4000

