import time
import unittest
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page_pom import LoginPage
from pages.payment_pom import PaymentPage


class TestPayment(unittest.TestCase):
    def setUp(self):
        # Initialize the WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Open the website
        self.driver.get("https://grocerymate.masterschool.com")

        # Initialize LoginPage and PaymentPage
        self.login_page = LoginPage(self.driver)
        self.payment_page = PaymentPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_payment(self):
        self.login_page.login("colamityjane@test.com", "jane1234")
        time.sleep(2)
        self.driver.get("https://grocerymate.masterschool.com/checkout")
        self.payment_page.fill_payment_form(
            address="addressColamity",
            city="cityColamity",
            postcode="72160",
            card_number="4111111111111111",
            card_name="Colamity Jane",
            expiration="12/25",
            cvv="123"
        )

        self.payment_page.submit_payment()
        self.driver.get("https://grocerymate.masterschool.com/checkout")
        print("navigating back to checkout, to verify the cart has been emptied after the payment process...")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/section/div/div/img"))
        )
        empty_cart_image = self.driver.find_element(By.XPATH, "//*[@id='root']/div/section/div/div/img")
        print("empty cart image is present...")
        self.assertTrue(empty_cart_image.is_displayed(), "Empty cart image is not displayed.")


if __name__ == "__main__":
    unittest.main()
