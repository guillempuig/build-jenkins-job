import requests
import time


def test_endpoint():
    time.sleep(30)
    resp = requests.get("http://209.133.199.114:8500/services")
    print(resp.json())
    assert isinstance(resp.json(), list)
