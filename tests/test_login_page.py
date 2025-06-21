import time
from selenium import webdriver
from pages.login_page import LoginPage

# тестовый класс
class TestLoginPage:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login_page = LoginPage(self.driver)

    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.enter_login("qwerty")
        self.login_page.enter_password("password")
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()