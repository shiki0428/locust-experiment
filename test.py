from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    host = "http://127.0.0.1:8000"
    @task
    def hello_world(self):
        self.client.get("/test")

    @task
    def hello_world_put(self):
        self.client.put("/items/2",        
        headers={'content-type': 'application/json'},
        json={
  "name": "string",
  "price": 0,
  "is_offer": True
})
