import json
import os
import requests
from tracer import *




class User:
    def on_get(self, req, resp):
        url = os.environ["NUMBER-GENERATOR"]
        data = requests.get(url)
        url = os.environ["USER"]
        user_data = requests.get(url)
        resp.text = f"Number generate by number generator services: {data.text}, user_data: {user_data}"

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        url = os.environ["NUMBER-GENERATOR"]

        ret = requests.post(url=url, data=json.dumps(data))

        val = int(ret.text)
        url = os.environ["USER_DETAILS"]
        for i in range(val):
            data = requests.get(url)
            print(data)

        resp.text = f"Response from number generator adding: {ret.text}"

app = falcon.App()

app.add_route("/m3/user", User())
