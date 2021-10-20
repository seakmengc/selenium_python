from dataclasses import dataclass

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


@dataclass
class NotesPage(BasePage):
    page_btn = By.CSS_SELECTOR, '[data-testid="notes"]'
    save_btn = By.CSS_SELECTOR, "[data-testid='topbar-action-sync-notes']"

    editor_ele = By.CSS_SELECTOR, 'div.react-codemirror2.editor.mousetrap'

    favorite_btn = By.CSS_SELECTOR, 'nav:nth-child(1) > button:nth-child(2)'
    new_note_btn = By.CSS_SELECTOR, '[data-testid="sidebar-action-create-new-note"]'

    note_title_ele = By.CSS_SELECTOR, '[data-testid="note-title-0"]'

    def __init__(self, driver):
        super().__init__(driver)

    def view_tab(self):
        self._view_tab()

    def get_editor(self):
        return self.find_element_by_tuple(self.editor_ele)

    def get_title(self):
        return self.find_element_by_tuple(self.note_title_ele)

    def add_new_note(self):
        self.find_element_by_tuple(self.new_note_btn).click()

    def input(self, text: str):
        self.find_element_by_tuple(self.editor_ele).click()

        self._clear_text()

        ActionChains(self.driver)\
            .send_keys(text)\
            .perform()

    def save_changes(self):
        self.find_element_by_tuple(self.save_btn).click()
