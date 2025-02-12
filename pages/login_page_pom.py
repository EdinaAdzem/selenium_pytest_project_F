from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.common import CommonPage


class LoginPage(CommonPage):
    #updated the paths to relative instead of absolute for robustness
    LOGIN = (By.XPATH, "//div[@class='headerIcon']")
    EMAIL = (By.XPATH, "//form//input[@type='email']")
    PASSWORD = (By.XPATH, "//form//input[@type='password']")
    SIGNIN = (By.XPATH, "//button[@type='submit' and contains(@class, 'submit-btn')]")
    ERROR_MESSAGE = (By.XPATH, "//form//div[contains(@class, 'error')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login(self):
        print(f"Clicking on element with XPath: {self.LOGIN}")
        self.click(*self.LOGIN)

    def enter_email(self, email):
        self.enter_text(*self.EMAIL, email)

    def enter_password(self, password):
        self.enter_text(*self.PASSWORD, password)

    def click_login_button(self):
        self.click(*self.SIGNIN)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)

    def login(self, email, password):
        self.click_login()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://grocerymate.masterschool.com/auth")
        )

        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()