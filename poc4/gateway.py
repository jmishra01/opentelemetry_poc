import falcon
import os
import json
from mysql.connector import connect
from tracer import *


app = falcon.App()


conn = connect(host=os.environ["DB_MYSQL_HOST"], port=os.environ["DB_MYSQL_PORT"],
        user=os.environ["DB_MYSQL_USER"], password=os.environ["DB_MYSQL_PASSWORD"])


class Gateway:

    def on_get(self, req, resp):
        resp.text = "Gateway Services"

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())

        cur = conn.cursor()

        cur.execute(
            "SELECT api_name FROM user WHERE user_name = '{}' GROUP BY api_name;".format(data["user_name"])
        )

        url = cur.fetchall()[0][0]

        ret = requests.get(url)

        resp.text = f"Result: {ret.text}"


app.add_route("/gateway", Gateway())
