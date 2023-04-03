from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_on_add_product_button(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BUTTON)
        button.click()

    def find_product_name_and_price(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_name, product_price

    def find_basket_product_name_and_price(self):
        basket_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        basket_product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text
        return basket_product_name, basket_product_price

