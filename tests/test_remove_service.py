import os

import requests

URL = os.environ['TESTING_SERVER_URL']
PORT = os.environ['CONTROLLER_PORT']
controller = URL + ":" + PORT


def test_remove_service():
    service_name = "testing_image"
    fluid_controller = f"{controller}"
    rm_url = fluid_controller+f"/service/{service_name}"

    rm_resp = requests.delete(rm_url)
    assert rm_resp.status_code == 200

    # retrieve list of services and check testing_image has been removed
    services = requests.get(fluid_controller+"/services")
    assert services.status_code == 200
    assert len(list(filter(lambda service: service['name'] == 'testing_image', services.json()))) == 0
