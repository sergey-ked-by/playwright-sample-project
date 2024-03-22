from pages.base import Base
from Locators.market_page import Market
from Locators.basket_page import Basket
from data.assertions import Assertion
from playwright.sync_api import Page


class MarketPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertions = Assertion(page)

    def add_to_cart(self):
        self.click_element_by_index(Market.ADD_TO_CART, 0)

    def checkout(self):
        self.click(Basket.CHECKOUT_BTN)
        self.input(Basket.FIRST_NAME, "Sergey")
        self.input(Basket.LAST_NAME, "Ked")
        self.input(Basket.ZIP, "220033")
        self.click(Basket.CNT_BTN)
        self.click(Basket.FINISH_BTN)
        self.assertions.have_text(Basket.FINAL_TEXT, "Checkout: Complete!", "no")