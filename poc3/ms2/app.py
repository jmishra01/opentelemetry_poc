from tracer import * 

import random

class User:
    def on_get(self, req, resp):

        user_name: list[str] = [
            "User 1",
            "User 2",
            "User 3",
            "User 4",
            "User 5",
        ]

        resp.text = random.choice(user_name)


app = falcon.App()

app.add_route("/m2/user-details", User())
