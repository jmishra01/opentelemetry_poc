from tracer import *

app = falcon.App()


class Service2:
    def on_get(self, req, resp):
        resp.text = "Service2 Services"


app.add_route("/service", Service2())


