import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.driver = webdriver.Chrome()

    def tearDown(self):
        print("tearDown")
        self.driver.quit()
