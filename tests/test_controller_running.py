import requests
import pytest
import os

URL = os.environ['TESTING_SERVER_URL']
PORT = os.environ['CONTROLLER_PORT']
controller = URL + ":" + PORT


@pytest.mark.asyncio
async def test_controller_is_running():
    endpoint = "/services"
    resp = requests.get(controller+endpoint)
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)