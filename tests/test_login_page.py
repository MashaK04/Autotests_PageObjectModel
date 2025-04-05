import time

from pages.login_page import LoginPage
class TestLoginPage:
    def setup_method(self):
        self.login_page = LoginPage(self.driver)

    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.enter_login("qwerty")
        self.login_page.enter_password("password")
        time.sleep(3)