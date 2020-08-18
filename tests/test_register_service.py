# This tests aims to create a service and register it to fluid_controller
import os

import requests

config = {
    "fluid_controller": "scrapper12",
    "service":
        {
            "service_name": "testing_image",
            "service_version": "1.0",
            "docker_image": "docker-reg.goldenspear.com/goldenspear_ai/testing_image:latest",
        }
}

URL = os.environ['TESTING_SERVER_URL']
PORT = os.environ['CONTROLLER_PORT']
controller = URL + ":" + PORT


def test_register_service():
    service = config["service"]
    fluid_controller = f"{controller}/service"
    # register service
    resp = requests.post(fluid_controller, json=service)
    # assert request response is successful
    assert resp.status_code == 200
    assert resp.json()["status"] == 'Success'

    service_name = service["service_name"]
    service_url = f"{controller}/{service_name}"

    res_service = requests.get(service_url)
    assert res_service.status_code == 200

    # list controller services (one added)
    url = f"{controller}/services"
    services = requests.get(url).json()
    print(services)
    assert isinstance(services, list)
    assert len(services) == 1
    assert services[0]['name'] == 'testing_image'

