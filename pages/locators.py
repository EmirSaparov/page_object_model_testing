from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    PRODUCT_ADD_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, '//h1')
    BASKET_PRODUCT_NAME = (By.XPATH, "//div[1]/strong")
    PRODUCT_PRICE = (By.CLASS_NAME, 'price_color')
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages'] //div[@class='alertinner ']")
