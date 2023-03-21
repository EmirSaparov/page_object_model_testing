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
