from dataclasses import dataclass
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

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
        self._view_tab()

    def input(self, text: str):
        self.view_tab()

        self.get_editor().click()

        self._clear_text()

        ActionChains(self.driver)\
            .send_keys(text)\
            .perform()

    def save_changes(self):
        self.find_element_by_tuple(self.save_btn).click()
