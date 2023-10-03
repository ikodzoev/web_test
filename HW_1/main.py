import requests
import yaml


def get_posts(token, owner="Me"):
    with open("config.yaml") as f:
        data = yaml.safe_load(f)

    params = {"owner": owner}
    headers = {"X-Auth-Token": token}
    resource = requests.get(data["url_posts"], headers=headers, params=params)
    return resource.json()
