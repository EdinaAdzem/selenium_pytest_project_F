import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page_pom import LoginPage
from pages.common import CommonPage

url = 'https://grocerymate.masterschool.com'


class TestSearchProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.login_page = LoginPage(self.driver)
        self.common_page = CommonPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_product_search(self):
        # log in with jane for the purposes of this validation
        print("Logging in...")
        self.login_page.login("colamityjane@test.com", "jane1234")

        # Navigate to the shopping page after successful login
        print("Navigating to shop page...")
        shop_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/ul/li[2]/a'))
        )
        shop_button.click()

        # Bypass age confirmation popup
        print("Bypassing age confirmation popup...")
        date_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/input'))
        )
        date_input.send_keys("01-01-1981")  # Hardcoded date of birth
        confirm_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/button')
        confirm_button.click()

        # Perform product search
        print("Searching for product 'Ginger'...")
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/input'))
        )
        search_input.send_keys("Ginger")  # hardcoded product name, will need to create a dictionary of existing to alternate at some point

        # Select the Ginger items list displayed
        print("Selecting the Ginger item from the search results...")
        ginger_item = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[1]/div/div/div/div[1]'))
        )
        ginger_item.click()

        product_image = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//img[@src="https://seleniumwebsites.fra1.digitaloceanspaces.com/grocery/Ginger.jpg"]'))
        )

        assert product_image is not None, "Ginger product image not found."
        print("Product search successful. Ginger is displayed.")


if __name__ == "__main__":
    unittest.main()
