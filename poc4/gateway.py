import json
import logging
from tracer import *


app = falcon.App()


class Gateway:

    def on_get(self, req, resp):
        resp.text = "Gateway Services"

    def on_post(self, req, resp):
        try:
            data = json.loads(req.stream.read())

            conf = dict(
                host=os.environ["DB_MYSQL_HOST"], port=int(os.environ["DB_MYSQL_PORT"]),
                user=os.environ["DB_MYSQL_USER"], password=os.environ["DB_MYSQL_PASSWORD"]
            )

            conn = mysql.connector.connect(**conf)
            cur = conn.cursor()

            cur.execute(
                "SELECT api_name FROM dev.user WHERE user_name = '{}' GROUP BY api_name;".format(data["user_name"])
            )

            url = cur.fetchall()[0][0]

            ret = requests.get(url)

            resp.text = f"Result: {ret.text}"
        except Exception as ex:
            logging.error(str(ex), stack_info=True, exc_info=True)
            raise falcon.HTTP_500



app.add_route("/gateway", Gateway())
