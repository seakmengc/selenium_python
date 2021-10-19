import unittest

from src.pages.scratch_pad_page import ScratchPadPage
from src.test.smoking.base_test import BaseTest


def _go_to_tab(driver):
    page = ScratchPadPage(driver)
    page.view_tab()

    return page


class ScratchPadTest(BaseTest):
    def test_go_to_view(self):
        _go_to_tab(self.driver)

    def test_input(self):
        page = _go_to_tab(self.driver)

        txt = 'Hello'
        page.input(txt)

        self.assertEqual(txt, page.get_editor().text.lstrip())

    def test_persist(self):
        page = _go_to_tab(self.driver)

        txt = 'Hello'
        page.input(txt)

        page.save_changes()
        self.driver.refresh()

        new_page = _go_to_tab(self.driver)

        self.assertEqual(txt, new_page.get_editor().text.lstrip())



