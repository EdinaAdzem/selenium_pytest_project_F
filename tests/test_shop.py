import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page_pom import LoginPage
from pages.common import CommonPage

url = 'https://grocerymate.masterschool.com'

class TestShop(unittest.TestCase):
    def setUp(self):
        # Initialize WebDriver and open the application
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)

        # Create instances of the LoginPage and CommonPage
        self.login_page = LoginPage(self.driver)
        self.common_page = CommonPage(self.driver)

    def tearDown(self):
        # Close the browser window after test execution
        self.driver.quit()

    def test_shop_cart(self):
        print("Logging in with existing user...colamity jane ")
        self.login_page.login("colamityjane@test.com", "jane1234")

        # Navigate to the shop link
        print("Navigating to the shop page...")
        shop_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/ul/li[2]/a'))
        )
        shop_button.click()

        # age confirm
        print("Handling age confirmation popup...")
        date_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/input'))
        )
        date_input.send_keys("01-01-1981")  # Hardcoded date of birth
        confirm_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/button')
        confirm_button.click()

        #add product
        print("Adding product to cart...")
        add_to_cart_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/button'))
        )
        add_to_cart_button.click()

        print("Navigating to the checkout page - masterschool.com/checkout")
        self.driver.get("https://grocerymate.masterschool.com/checkout")
        print("Verifying the product in the cart...")
        product_name = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Oranges")]'))
        )
        assert product_name.is_displayed(), "Product not found in the cart!"
        print("Product successfully found in the cart!")

if __name__ == "__main__":
    unittest.main()
