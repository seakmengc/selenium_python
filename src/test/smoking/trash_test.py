from src.test.smoking.base_test import BaseTest
from src.pages.trash_page import TrashPage


class TrashTest(BaseTest):
    def test_move_to_trash(self):
        page = TrashPage(self.driver)

        page.move_to_trash()

        self.assertEqual(1, page.get_notes_len())
