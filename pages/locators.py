from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.XPATH, '//p')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL_REGISTER_INPUT = (By.NAME, 'registration-email')
    PASSWORD_REGISTER_INPUT = (By.NAME, 'registration-password1')
    CONFIRM_PASSWORD_REGISTER_INPUT = (By.NAME, 'registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators():
    PRODUCT_ADD_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.XPATH, '//h1')
    BASKET_PRODUCT_NAME = (By.XPATH, "//div[1]/strong")
    PRODUCT_PRICE = (By.CLASS_NAME, 'price_color')
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages'] //div[@class='alertinner ']")
