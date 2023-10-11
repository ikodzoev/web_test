import logging
import pytest
import yaml

from testpage_api import get_data_posts, test_create_post

# Фикстура для загрузки тестовых данных из файла
@pytest.fixture(scope="session")
def testdata():
    with open("testdata.yaml") as f:
        return yaml.safe_load(f)

# Тест 1: Проверка получения данных постов
def test_1(login, testdata):
    logging.info("Test api 1 Starting")
    # Получение данных постов
    res = get_data_posts(login, {"owner": "notMe"})
    lst = res["data"] if res else []
    # Проверка наличия идентификатора в полученных данных
    assert testdata["find_id"] in [el["id"] for el in lst]

# Тест 2: Проверка создания поста
def test_2(login, testdata):
    logging.info("Test api 2 Starting")
    # Создание поста
    if test_create_post(login, testdata["title"], testdata["description"], testdata["content"]):
        # Получение описаний всех постов, если создание поста прошло успешно
        lst_description = [el["description"] for el in get_data_posts(login)["data"]]
    else:
        lst_description = []
    # Проверка наличия описания в полученных данных
    assert testdata["description"] in lst_description
