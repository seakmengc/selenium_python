from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_by_tuple(self, by: tuple[str, str]) -> WebElement:
        return self.driver.find_element(*by)
