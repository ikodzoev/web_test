import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Определение базового класса страницы
class BasePage:
    # Инициализация драйвера и базового URL
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    # Метод для поиска элемента на странице с заданным локатором и временем ожидания
    def find_element(self, locator, time=10):
        try:
            # Возвращаем элемент, если он найден в течение заданного времени ожидания
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}")
        except TimeoutException:
            # Записываем исключение в лог, если время ожидания истекло и элемент не был найден
            logging.exception("Timeout exception while searching for element with locator %s", locator)
            return None

    # Метод для получения свойства элемента
    def get_element_property(self, mode, locator, property):
        # Ищем элемент
        element = self.find_element(mode, locator)
        if element:
            # Возвращаем значение свойства, если элемент найден
            return element.value_of_css_property(property)
        else:
            # Записываем ошибку в лог, если элемент не найден
            logging.error("Can't get property %s from non-existing element with locator %s", property, locator)
            return None

    # Метод для перехода на сайт по базовому URL
    def go_to_site(self):
        try:
            self.driver.get(self.base_url)
        except Exception as e:
            # Записываем исключение в лог, если возникла ошибка при открытии сайта
            logging.exception("Exception occurred while opening site: %s", e)

    # Метод для получения уведомления (alert)
    def get_alert(self, time=10):
        try:
            # Возвращаем уведомление, если оно появляется в течение заданного времени ожидания
            return WebDriverWait(self.driver, time).until(EC.alert_is_present(),
                                                          message="Alert not found")
        except TimeoutException:
            # Записываем исключение в лог, если время ожидания истекло и уведомление не появилось
            logging.exception("Timeout exception while waiting for alert")
            return None
