import pytest
import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def login():
    response = requests.post(data["url_login"],
                             data={'username': data["login"], 'password': data["password"]})
    if response.status_code == 200:
        return response.json()["token"]

