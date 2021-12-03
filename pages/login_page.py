from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    def register_new_user(self, email, password):
        email_elt = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_elt.send_keys(email)
        password_elt = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_elt.send_keys(password)
        password2_elt = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        password2_elt.send_keys(password)
        button_elt = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button_elt.click()

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
