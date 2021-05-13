import socket
import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    ctrname = socket.gethostname()
    return "Hit refresh to show the number of times you refreshed the page. You've only refreshed {} times. Request served by {} \n".format(count, ctrname)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
