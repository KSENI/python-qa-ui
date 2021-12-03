from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        book_title = self.browser.find_element(*ProductPageLocators.BOOK).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        book = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_product.click()
        return book_title, price

    def should_be_book_in_success_message(self, book_title):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"
        success_message_elt = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        success_message = success_message_elt.text
        assert book_title == success_message, f"Book title is not in success message, expected: {book_title}, but was {success_message}"

    def should_be_book_price_in_message(self, price):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_PRICE), "Message with price is not presented"
        basket_elt = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE)
        basket_text = basket_elt.text
        assert price == basket_text , f"Book price is not in message, expected: {price}, but was {basket_text}"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should disappeared"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
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