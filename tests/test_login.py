import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page_pom import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://grocerymate.masterschool.com")
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        self.login_page.login("colamityjane@test.com", "jane1234")
        time.sleep(2)
        self.login_page.click_login()
        self.assertEqual(self.driver.current_url, "https://grocerymate.masterschool.com/auth",
                         "Did not navigate to the auth page after clicking login.")

        # Verify that the Logout button is present
        try:
            logout_button = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/button")
            self.assertTrue(logout_button.is_displayed(), "Logout button is not displayed.")
        except:
            self.fail("Logout button not found.")



if __name__ == "__main__":
    unittest.main()
