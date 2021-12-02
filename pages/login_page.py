from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.page_source

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTRATION_EMAIL), "Registration email is not presented"
        assert self.is_element_present(*MainPageLocators.REGISTRATION_PASSWORD), "Registration password is not presented"
        assert self.is_element_present(*MainPageLocators.REGISTRATION_PASSWORD_REPEAT), "Registration password repeat is not presented"
        assert self.is_element_present(*MainPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"
