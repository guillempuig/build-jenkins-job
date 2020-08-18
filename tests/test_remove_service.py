import os

import requests

URL = os.environ['TESTING_SERVER_URL']
PORT = os.environ['CONTROLLER_PORT']
CLIENT = 'gs'
ENV = 'dev'
controller = URL + ":" + PORT


def test_remove_service():
    service_name = f"{CLIENT}_{ENV}_testing_image"
    fluid_controller = f"{controller}/service"

    rm_resp = requests.delete(fluid_controller+f"/{service_name}")
    assert rm_resp.status_code == 200

    # retrieve list of services and check testing_image has been removed
    services = requests.get(fluid_controller)
    assert services.status_code == 200
    assert len(list(filter(lambda service: service['name'] == 'testing_image', services.json()))) == 0
