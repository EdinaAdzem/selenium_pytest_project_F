import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page_pom import LoginPage
from pages.registration_page_pom import RegistrationPage
import random
import string


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://grocerymate.masterschool.com")
        self.login_page = LoginPage(self.driver)
        self.registration_page = RegistrationPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def generate_random_email(self):
        """Generate a unique email address."""
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"testuser_{random_string}@example.com"

    def generate_random_password(self):
        """Generate a random password."""
        random_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        return random_password
    def test_registration(self):
        email = self.generate_random_email()
        password = self.generate_random_password()
        fullname = "Test User"
        self.registration_page.click_login()
        self.registration_page.click_create_new_account()
        self.registration_page.create_new_account(
            fullname=fullname,
            email=email,
            password=password
        )

        print(f"Registered new user with email: {email} and password: {password}")



if __name__ == "__main__":
    unittest.main()
