from src.test.smoking.base_test import BaseTest
from src.pages.notes_page import NotesPage
import pytest


def _go_to_tab(driver):
    page = NotesPage(driver)
    page.view_tab()

    return page


class NotesTest(BaseTest):
    def test_go_to_view(self):
        _go_to_tab(self.driver)

    def test_add_new_note(self):
        page = _go_to_tab(self.driver)

        page.add_new_note()

        self.assertEqual(
            'New note',
            page.get_title().text.lstrip()
        )

    def test_input(self):
        page = _go_to_tab(self.driver)

        txt = 'Hello'
        page.input(txt)

        self.assertEqual(txt, page.get_editor().text.lstrip())
        self.assertEqual(txt, page.get_title().text.lstrip())

    def test_persist(self):
        page = _go_to_tab(self.driver)

        txt = 'Hello'
        page.input(txt)

        page.save_changes()
        self.driver.refresh()

        new_page = _go_to_tab(self.driver)

        self.assertEqual(txt, new_page.get_editor().text.lstrip())
