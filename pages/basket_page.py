from .base_page import BasePage
from .locators import BasketPageLocators
class BasketPage(BasePage):
    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            "Message about empty basket is not present"

    def should_be_not_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), \
            "Products are present although not required"
