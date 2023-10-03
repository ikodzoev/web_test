"""Задание № 1
Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
а потом проверяется его наличие на сервере по полю «описание».
Подсказка: создание поста выполняется запросом к
https://test-stand.gb.ru/api/posts с передачей параметров title, description, content."""

import yaml
import requests
from main import get_posts


# Загрузка конфигурационных данных из файла config.yaml
def load_config():
    with open("config.yaml") as f:
        return yaml.safe_load(f)


# Проверка наличия элемента с заданным ID в списке
def assert_id_in_list(lst, id_to_check):
    lst_ids = [el["id"] for el in lst]
    assert id_to_check in lst_ids, "тест не пройден"


# Создание поста с использованием переданного токена
def create_post(login, config):
    response = requests.post(
        config["url_posts"],
        headers={"X-Auth-Token": login},
        data={'title': config["title"],
              'description': config["description"],
              'content': config["content"]}
    )
    return response


# Проверка наличия описания в списке постов
def assert_description_in_posts(login, config):
    lst_description = [el["description"] for el in get_posts(login)["data"]]
    assert config["description"] in lst_description, "тест не пройден"


def main():
    config = load_config()
    login = config["your_login"]

    # Тест 1: Проверка наличия элемента с определенным ID в списке
    test_1_out = get_posts(login)
    assert_id_in_list(test_1_out["data"], 17027)

    # Тест 2: Создание поста и проверка наличия описания в списке постов
    create_post_result = create_post(login, config)
    assert_description_in_posts(login, config)


if __name__ == "__main__":
    main()
