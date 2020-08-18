import os

import requests

URL = os.environ['TESTING_SERVER_URL']
PORT = os.environ['CONTROLLER_PORT']
CLIENT = 'gs'
ENV = 'dev'
controller = URL + ":" + PORT


def test_remove_service():
    service_name = f"{CLIENT}_{ENV}_testing"
    fluid_controller = f"{controller}/service/{service_name}"


