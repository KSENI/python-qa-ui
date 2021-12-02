from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.page_source

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Registration password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), "Registration password repeat is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"
