from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.get_product_name()
        self.get_product_price()
        self.should_be_button_add_product_to_basket()
        self.click_add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_success_message()
        self.product_name_should_be_matches()
        self.should_be_message_with_price()
        self.product_price_should_be_matches()

    # Метод получения названия товара
    def get_product_name(self):
        get_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        self.product_name = get_product_name.text

    # Метод получения цены товара
    def get_product_price(self):
        get_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        self.product_price = get_product_price.text

    # Метод проверки наличия кнопки добавления товара в корзину
    def should_be_button_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON), 'Button for add product' \
                                                                                           ' to basket not found'
    # Метод клика по кнопке добавления в корзину
    def click_add_product_to_basket(self):
        button_add_product_to_basket = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON)
        button_add_product_to_basket.click()

    # Метод проверки наличия сообщения о том, что товар добавлен в корзину.
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADDED_PRODUCT), 'No message that the product' \
                                                                                  ' has been added to the basket'
    # Метод проверки совпадения названия товара в сообщении с тем товаром, который добавляли в корзину
    def product_name_should_be_matches(self):
        get_product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        self.product_name_in_message = get_product_name_in_message.text
        assert self.product_name_in_message == self.product_name, 'The name of the added product does' \
                                                                  ' not match the name in the shopping cart'
    # Метод проверки наличия сообщения со стоимостью корзины
    def should_be_message_with_price(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRICE_MESSAGES), 'No price message'

    # Метод проверки совпадения цены товара в сообщении с тем товаром, который добавляли в корзину
    def product_price_should_be_matches(self):
        get_product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        self.product_price_in_basket = get_product_price_in_basket.text
        assert self.product_price_in_basket == self.product_price, 'The price of the added product does ' \
                                                                   'not match the name in the shopping cart'


