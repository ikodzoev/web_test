import yaml
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# Загрузка тестовых данных из файла
@pytest.fixture(scope="session")
def testdata():
    with open("testdata.yaml") as f:
        return yaml.safe_load(f)


# Фикстура для инициализации веб-драйвера
@pytest.fixture(scope="session")
def browser(testdata):
    browser = testdata["browser"]
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(testdata["driver_path"])
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


# Фикстура для выполнения входа в систему и получения токена
@pytest.fixture(scope="session")
def login(testdata):
    try:
        response = requests.post(testdata["url_login"],
                                 data={'username': testdata["login"], 'password': testdata["password"]})
        response.raise_for_status()
        return response.json()["token"]
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Failed to login: {e}")
