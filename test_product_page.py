import pytest
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

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
