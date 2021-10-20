from src.pages.favorite_page import FavoritePage
from src.test.smoking.base_test import BaseTest


class FavoriteTest(BaseTest):
    def test_add_to_favorite(self):
        page = FavoritePage(self.driver)

        page.add_to_favorite()

        self.assertEqual(1, page.get_notes_len())
