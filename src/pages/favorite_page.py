# from dataclasses import dataclass
# from selenium import webdriver

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By

# from src.pages.base_page import BasePage
# from src.pages.notes_page import NotesPage


# @dataclass
# class FavoritePage(BasePage):
#     page_btn = By.CSS_SELECTOR, 'section.app-sidebar-main > button:nth-child(1)'
#     save_btn = By.CSS_SELECTOR, "[data-testid='topbar-action-sync-notes']"

#     editor_ele = By.CSS_SELECTOR, 'div.react-codemirror2.editor.mousetrap'

#     def __init__(self, driver: webdriver):
#         super().__init__(driver)

#         self.notes_page = NotesPage(driver)

#     def view_tab(self):
#         self._view_tab()

#     def input(self, text: str):
#         self.notes_page.view_tab()

#         self.find_element_by_tuple(self.editor_ele).click()

#         self._clear_text()

#         ActionChains(self.driver)\
#             .send_keys(text)\
#             .perform()

#     def save_changes(self):
#         self.find_element_by_tuple(self.save_btn).click()
