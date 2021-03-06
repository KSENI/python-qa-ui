from selenium.webdriver.common.by import By
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK= (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    SAMETHING_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, ".content #content_inner > p > a")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[name='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-of-type(1) div strong")
    BASKET = (By.CSS_SELECTOR, ".basket-mini")
    BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    