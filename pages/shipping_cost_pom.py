from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShippingCostPage:
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]')
    EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/form/input[1]")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/form/input[2]")
    SIGNIN_BUTTON = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/form/button")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/form/div[2]")
    AGE_INPUT = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/input')
    AGE_CONFIRM_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/button')
    AGE_ERROR_MESSAGE = (By.XPATH, '//*[contains(text(), "Age verification failed")]')
    STORE_LINK = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/ul/li[2]/a')
    CART_ICON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/svg/path')
    SHIPPING_COST = (By.XPATH, '//*[@id="root"]/div/section/div/div[1]/div/div[2]/h5[2]')
    TOTAL_COST = (By.XPATH, '//*[@id="root"]/div/section/div/div[1]/div/div[4]')

    # Add product-related XPaths for parameterization in tests
    #
    PRODUCT_XPATH = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[3]/div/img')
    QUANTITY_INPUT_XPATH = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/input')  # Example XPath
    ADD_TO_CART_XPATH = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/button')

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.EMAIL_FIELD)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.SIGNIN_BUTTON).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.STORE_LINK))

    def handle_age_confirmation(self, dob):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.AGE_INPUT)).send_keys(dob)
        self.driver.find_element(*self.AGE_CONFIRM_BUTTON).click()

    def is_age_validation_triggered(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.AGE_ERROR_MESSAGE)
            ).is_displayed()
        except:
            return False

    def navigate_to_store(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.STORE_LINK)).click()

    def search_and_add_items(self, product_xpath, quantity_input_xpath, add_to_cart_xpath, quantity):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(product_xpath)).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(quantity_input_xpath)
        ).send_keys(str(quantity))
        self.driver.find_element(*add_to_cart_xpath).click()

    def navigate_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CART_ICON)).click()

    def get_shipping_and_total_cost(self):
        shipping_cost = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SHIPPING_COST)
        ).text
        total_cost = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TOTAL_COST)
        ).text
        return float(shipping_cost.replace('€', '').strip()), float(total_cost.replace('€', '').strip())
