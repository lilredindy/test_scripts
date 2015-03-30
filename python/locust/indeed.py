from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        #self.login()
        pass
            

    def login(self):
        #self.client.post("/login", {"username":"ellen_key", "password":"education"})
        pass

    @task(2)
    def index(self):
        print "get me outta here!"
        self.client.get("/")

    #@task(1)
    #def resumes(self):
    #    self.client.get("/resumes")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=2000
    max_wait=4000

