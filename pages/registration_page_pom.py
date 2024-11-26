from selenium.webdriver.common.by import By

class RegistrationPage:
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]')
    CREATE_NEW_ACCOUNT_LINK = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/a[1]')
    FULLNAME = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/input[1]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/input[2]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/input[3]')
    SIGNUP_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[1]/div/form/button')

    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_create_new_account(self):
        self.driver.find_element(*self.CREATE_NEW_ACCOUNT_LINK).click()

    def create_new_account(self, fullname, email, password):
        # Fill in the registration form
        self.driver.find_element(*self.FULLNAME).send_keys(fullname)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.SIGNUP_BUTTON).click()
