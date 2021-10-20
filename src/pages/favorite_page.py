from dataclasses import dataclass
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.pages.notes_page import NotesPage


@dataclass
class FavoritePage(BasePage):
    page_btn = By.CSS_SELECTOR, '[data-testid="favorites"]'

    favorite_btn = By.CSS_SELECTOR,  'main > section > nav:nth-child(1) > button:nth-child(2)'

    favorite_title = 'Welcome to Takenote!'

    notes_list_ele = By.CSS_SELECTOR, '[data-testid="note-list"]'

    def __init__(self, driver):
        super().__init__(driver)

        self.notes_page = NotesPage(driver)

    def get_notes_len(self) -> int:
        return int(self.find_element_by_tuple(self.notes_list_ele).get_attribute('childElementCount'))

    def view_tab(self):
        self.find_element_by_tuple(self.page_btn).click()

    def add_to_favorite(self):
        self.notes_page.view_tab()
        self.notes_page.get_editor().click()

        self.find_element_by_tuple(self.favorite_btn).click()

        self.view_tab()
