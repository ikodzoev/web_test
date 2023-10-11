import logging
import requests
import yaml

# Загрузка тестовых данных из файла
with open("testdata.yaml") as f:
    data = yaml.safe_load(f)

# Функция для получения данных постов
def get_data_posts(token, params=None):
    if token:
        try:
            response = requests.get(data["url_posts"],
                                    headers={"X-Auth-Token": token},
                                    params=params)
        except requests.exceptions.RequestException as e:
            logging.exception("Exception occurred while getting data posts: %s", e)
        else:
            if response.status_code == 200:
                logging.debug("Data posts successfully received")
                return response.json()
            else:
                logging.error("Failed to get data posts. Status code: %s", response.status_code)
    else:
        logging.error("Token not received")

# Функция для создания поста
def test_create_post(login, title, description, content):
    try:
        response = requests.post(data["url_posts"],
                                 headers={"X-Auth-Token": login},
                                 data={'title': title,
                                       'description': description,
                                       'content': content})
    except requests.exceptions.RequestException as e:
        logging.exception("Exception occurred while creating post: %s", e)
    else:
        if response.status_code == 200:
            logging.debug("Post %s was successfully published", title)
            return True
        else:
            logging.error("Failed to create post. Status code: %s", response.status_code)
