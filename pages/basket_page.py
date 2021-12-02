from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.SAMETHING_IN_BASKET), "Samething is basket, but should not be"
    def should_be_text_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "Message empty basket is not presented" 