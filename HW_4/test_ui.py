import time
import pytest
import logging
import yaml

from testpage_ui import OperationsHelper


# Фикстура для загрузки тестовых данных из файла
@pytest.fixture(scope="session")
def testdata():
    with open("testdata.yaml") as f:
        return yaml.safe_load(f)


# Тест 1: Проверка входа в систему с неверными учетными данными
def test_step1(browser):
    logging.info("Test UI 1 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login("test")
    test_page.enter_pass("test")
    test_page.click_login_button()

    # Проверка наличия ошибки 401 при входе с неверными учетными данными
    assert test_page.get_error_text() == "401"


# Тест 2: Проверка входа в систему с верными учетными данными и доступа к блогу
def test_step2(browser, testdata):
    logging.info("Test UI 2 Starting")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata["login"])
    test_page.enter_pass(testdata["password"])
    test_page.click_login_button()

    # Проверка доступа к блогу после успешного входа в систему
    assert test_page.get_blog() == "Blog"


# Тест 3: Проверка отправки контактной формы
def test_step3(browser, testdata):
    logging.info("Test UI 3 Starting...")
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(testdata["login"])
    test_page.enter_pass(testdata["password"])
    test_page.click_login_button()

    # Заполнение и отправка контактной формы
    test_page.click_contact()
    test_page.enter_name("Junior")
    test_page.enter_email("larevaloraleva@mail.ru")
    test_page.enter_content("dontyouwantme")
    test_page.click_button_contact_as()
