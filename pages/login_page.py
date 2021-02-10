from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.url
        assert 'login' in current_url, 'Invalid login URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        email_el = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_el.send_keys(email)

        password_el = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_el.send_keys(password)

        password_repeat_el = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT)
        password_repeat_el.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
