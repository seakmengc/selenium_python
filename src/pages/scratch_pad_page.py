from dataclasses import dataclass
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.pages.base_page import BasePage


@dataclass
class ScratchPadPage(BasePage):
    page_btn = By.CSS_SELECTOR, 'section.app-sidebar-main > button:nth-child(1)'
    save_btn = By.CSS_SELECTOR, "[data-testid='topbar-action-sync-notes']"

    editor_ele = By.CSS_SELECTOR, 'div.react-codemirror2.editor.mousetrap'

    def __init__(self, driver):
        super().__init__(driver)

    def get_editor(self):
        return self.find_element_by_tuple(self.editor_ele)

    def view_tab(self):
        self.driver.get('https://takenote.dev/app')
        self.driver.maximize_window()

        self.find_element_by_tuple(self.page_btn).click()

    def input(self, text: str):
        self.view_tab()

        self.get_editor().click()

        # clear text
        ActionChains(self.driver)\
            .key_down(Keys.COMMAND)\
            .send_keys('a')\
            .key_up(Keys.COMMAND) \
            .send_keys(Keys.BACKSPACE) \
            .perform()

        ActionChains(self.driver)\
            .send_keys(text)\
            .perform()

    def save_changes(self):
        self.find_element_by_tuple(self.save_btn).click()