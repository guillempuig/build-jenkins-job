import time

import requests
import os

URL = os.environ['TESTING_SERVER_URL']
PORT = os.environ['CONTROLLER_PORT']
controller = URL + ":" + PORT


def test_controller_is_running():
    endpoint = "/services"
    resp = requests.get(controller + endpoint)
    assert resp.status_code == 200
    time.sleep(100)
    assert isinstance(resp.json(), list)

