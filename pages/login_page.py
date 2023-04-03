from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_page_url = self.browser.current_url
        assert "login" in login_page_url, 'This is not login page url'

    def should_be_login_form(self):
        assert self.element_is_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.element_is_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email: str, password: str):
        email_register = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_INPUT)
        password_register = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_INPUT)
        confirm_password_register = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_REGISTER_INPUT)
        email_register.send_keys(email)
        password_register.send_keys(password)
        confirm_password_register.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
