from locust import HttpUser, task#, TaskSet, task


#class UserBehavior(TaskSet):
#
#    @task(1)
#    def index(self):
#        raise NotImplementedError
#
#    @task(3)
#    def predict(self):
#        raise NotImplementedError
#
#
#class APIUser(HttpLocust):
#    task_set = UserBehavior
#    min_wait = 1000
#    max_wait = 5000
#

class QuickstartUser(HttpUser):

    @task(1)
    def index(self):
        self.client
        self.client.get('/')

    @task(3)
    def predict(self):
        self.client.post('/predict',params={'text':'dolar'})

    def on_start(self):
        pass
