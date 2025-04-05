from pages.base_page import BasePage

class LoginPage(BasePage):
    PAGE_URL = "https://www.freeconferencecall.com/ru/ru/login"

    lOGIN_FIELD_LOCATOR= ("xpath", "//input[@name='email']")
    PASSWORD_FIELD_LOCATOR =("xpath", "//input[@name='password']")


    def enter_login(self, login):
        login_field = self.driver.find_element(*self.lOGIN_FIELD_LOCATOR)
        login_field.send_keys(login)


    def enter_password(self, password):
        password_field = self.driver.find_element(*self.PASSWORD_FIELD_LOCATOR)
        password_field.send_keys(password)