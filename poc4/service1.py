from tracer import *

app = falcon.App()


class Service1:
    def on_get(self, req, resp):
        resp.text = "Service1 Services"


app.add_route("/service", Service1())

