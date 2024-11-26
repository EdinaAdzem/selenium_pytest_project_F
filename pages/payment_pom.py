from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    STREET_ADDRESS_INPUT = '//*[@id="root"]/div/section/div/div[2]/div/form/input[1]'
    CITY_INPUT = '//*[@id="root"]/div/section/div/div[2]/div/form/input[2]'
    POSTCODE_INPUT = '//*[@id="root"]/div/section/div/div[2]/div/form/input[3]'
    CARD_NUMBER_INPUT = '//*[@id="root"]/div/section/div/div[2]/div/form/input[4]'
    NAME_ON_CARD_INPUT = '//*[@id="root"]/div/section/div/div[2]/div/form/input[5]'
    EXPIRATION_INPUT = '//*[@id="root"]/div/section/div/div[2]/div/form/div/div[1]/input'
    CVV_INPUT = '//*[@id="root"]/div/section/div/div[2]/div/form/div/div[2]/input'
    BUY_NOW_BUTTON = '//*[@id="root"]/div/section/div/div[2]/div/form/button'

    def fill_street_address(self, address):
        street_address_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.STREET_ADDRESS_INPUT))
        )
        street_address_input.send_keys(address)

    def fill_city(self, city):
        city_input = self.driver.find_element(By.XPATH, self.CITY_INPUT)
        city_input.send_keys(city)

    def fill_postcode(self, postcode):
        postcode_input = self.driver.find_element(By.XPATH, self.POSTCODE_INPUT)
        postcode_input.send_keys(postcode)

    def fill_card_number(self, card_number):
        card_number_input = self.driver.find_element(By.XPATH, self.CARD_NUMBER_INPUT)
        card_number_input.send_keys(card_number)

    def fill_name_on_card(self, name):
        name_on_card_input = self.driver.find_element(By.XPATH, self.NAME_ON_CARD_INPUT)
        name_on_card_input.send_keys(name)

    def fill_expiration(self, expiration_date):
        expiration_input = self.driver.find_element(By.XPATH, self.EXPIRATION_INPUT)
        expiration_input.send_keys(expiration_date)

    def fill_cvv(self, cvv):
        cvv_input = self.driver.find_element(By.XPATH, self.CVV_INPUT)
        cvv_input.send_keys(cvv)

    def submit_payment(self):
        buy_now_button = self.driver.find_element(By.XPATH, self.BUY_NOW_BUTTON)
        buy_now_button.click()

    def complete_payment(self, address, city, postcode, card_number, name_on_card, expiration_date, cvv):
        self.fill_street_address(address)
        self.fill_city(city)
        self.fill_postcode(postcode)
        self.fill_card_number(card_number)
        self.fill_name_on_card(name_on_card)
        self.fill_expiration(expiration_date)
        self.fill_cvv(cvv)
        self.submit_payment()


