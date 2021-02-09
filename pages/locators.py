from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    VIEW_BASKET = (By.CSS_SELECTOR, '.btn-group>.btn.btn-default:nth-child(1)')


class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, '.basket_summary')
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages >.fade.in:nth-child(1)>.alertinner')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages >.fade.in:nth-child(1)>.alertinner>strong')
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alertinner > p > strong')
    ALERT_PRICE_MESSAGES = (By.CSS_SELECTOR, '.alert-info.fade.in> .alertinner')