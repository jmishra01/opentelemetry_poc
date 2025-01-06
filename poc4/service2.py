from tracer import *

app = falcon.App()


class Service2:
    def on_get(self, req, resp):
        resp.text = "Service2 Services"

class Service3:
    def on_get(self, req, resp):
        raise falcon.http_500()


app.add_route("/service", Service2())
app.add_route("/service3", Service3())


