from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_product.click()

    def should_be_success_message(self):
        book_title = "The shellcoder's handbook"
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
        success_message_elt = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        success_message = success_message_elt.text
        assert book_title in success_message, "Book title is not in success message"

    def should_be_book_price_in_basket(self):
        price = "9,99"
        assert self.is_element_present(*ProductPageLocators.BASKET), "Basket is not presented"
        basket_elt = self.browser.find_element(*ProductPageLocators.BASKET)
        basket_text = basket_elt.text
        assert price in basket_text , "Book price is not in basket"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")