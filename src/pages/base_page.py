from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_by_tuple(self, by: tuple[str, str]) -> WebElement:
        return self.driver.find_element(*by)

    def _view_tab(self):
        self.driver.get('https://takenote.dev/app')
        self.driver.maximize_window()

        self.find_element_by_tuple(self.page_btn).click()

    def _clear_text(self):
        # clear text
        ActionChains(self.driver)\
            .key_down(Keys.COMMAND)\
            .send_keys('a')\
            .key_up(Keys.COMMAND) \
            .send_keys(Keys.BACKSPACE) \
            .perform()
