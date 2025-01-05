import json
import os
import random
import requests
from tracer import *


class User:
    def on_get(self, req, resp):
        url = os.environ["USER_SERVICES"]
        data = requests.get(url)
        resp.text = f"data recevied from user_services: {data.text}"

class NumberGenerator:
    def on_get(self, req, resp):
        num = random.randint(1, 10)
        resp.text = str(num)

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        resp.text = str(data["x"] + data["y"])


app = falcon.App()

app.add_route("/m1/user", User())
app.add_route("/m1/number-generator", NumberGenerator())
