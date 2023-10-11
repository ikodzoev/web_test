import logging
import yaml
from selenium.common.exceptions import NoSuchElementException
from BaseApp import BasePage
from selenium.webdriver.common.by import By


# Класс для определения локаторов
class TestSearchLocators:
    ids = dict()
    # Загрузка локаторов из файла
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)

    # Определение XPATH-локаторов
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])


# Класс для выполнения операций на странице
class OperationsHelper(BasePage):

    # Метод для ввода текста в поле информации
    def enter_text_info_field(self, locator, word, description=None):
        element_name = description if description else locator
        logging.debug(f"Send {word} to element {element_name}")
        try:
            field = self.find_element(locator)
            field.clear()
            field.send_keys(word)
        except NoSuchElementException:
            logging.exception(f"Element {locator} not found")
            return False

    # Метод для нажатия на кнопку
    def click_button(self, locator, description=None):
        element_name = description if description else locator
        try:
            button = self.find_element(locator)
            button.click()
        except NoSuchElementException:
            logging.exception(f"Button {element_name} not found")
            return False
