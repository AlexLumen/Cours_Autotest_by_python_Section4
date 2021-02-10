import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
@pytest.mark.need_review
@pytest.mark.parametrize('link', ["coders-at-work_207/?promo=offer0",
                                  "coders-at-work_207/?promo=offer1",
                                  "coders-at-work_207/?promo=offer2",
                                  "coders-at-work_207/?promo=offer3",
                                  "coders-at-work_207/?promo=offer4",
                                  "coders-at-work_207/?promo=offer5",
                                  "coders-at-work_207/?promo=offer6",
                                  "coders-at-work_207/?promo=offer8",
                                  "coders-at-work_207/?promo=offer9",
                                  pytest.param("coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

@pytest.mark.xfail(reason="Won't fix")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Won't fix")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_should_be_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_not_product_in_basket()
    page.should_be_message_about_empty_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "124345"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, link)
        page.register_new_user(email, password)
        page = BasePage(browser, link)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()