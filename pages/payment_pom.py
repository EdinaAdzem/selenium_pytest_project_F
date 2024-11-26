from selenium.webdriver.common.by import By
from pages.common import CommonPage

class PaymentPage(CommonPage):
    # Payment form elements
    STREET_ADDRESS = (By.XPATH, '//*[@id="root"]/div/section/div/div[2]/div/form/input[1]')
    CITY = (By.XPATH, '//*[@id="root"]/div/section/div/div[2]/div/form/input[2]')
    POSTCODE = (By.XPATH, '//*[@id="root"]/div/section/div/div[2]/div/form/input[3]')
    CARD_NUMBER = (By.XPATH, '//*[@id="root"]/div/section/div/div[2]/div/form/input[4]')
    CARD_NAME = (By.XPATH, '//*[@id="root"]/div/section/div/div[2]/div/form/input[5]')
    EXPIRATION = (By.XPATH, '//*[@id="root"]/div/section/div/div[2]/div/form/div/div[1]/input')
    CVV = (By.XPATH, '//*[@id="root"]/div/section/div/div[2]/div/form/div/div[2]/input')
    BUY_NOW_BUTTON = (By.XPATH, '//*[@id="root"]/div/section/div/div[2]/div/form/button')

    def __init__(self, driver):
        super().__init__(driver)

    def enter_street_address(self, address):
        self.enter_text(*self.STREET_ADDRESS, address)

    def enter_city(self, city):
        self.enter_text(*self.CITY, city)

    def enter_postcode(self, postcode):
        self.enter_text(*self.POSTCODE, postcode)

    def enter_card_number(self, card_number):
        self.enter_text(*self.CARD_NUMBER, card_number)

    def enter_card_name(self, card_name):
        self.enter_text(*self.CARD_NAME, card_name)

    def enter_expiration(self, expiration):
        self.enter_text(*self.EXPIRATION, expiration)

    def enter_cvv(self, cvv):
        self.enter_text(*self.CVV, cvv)

    def click_buy_now(self):
        self.click(*self.BUY_NOW_BUTTON)

    def fill_payment_form(self, address, city, postcode, card_number, card_name, expiration, cvv):
        self.enter_street_address(address)
        self.enter_city(city)
        self.enter_postcode(postcode)
        self.enter_card_number(card_number)
        self.enter_card_name(card_name)
        self.enter_expiration(expiration)
        self.enter_cvv(cvv)

    def submit_payment(self):
        self.click_buy_now()
