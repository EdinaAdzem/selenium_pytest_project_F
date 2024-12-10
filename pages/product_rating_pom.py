from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.common import CommonPage
from pages.login_page_pom import LoginPage


class ProductRatingPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(driver)

    def login(self, username, password):
        self.login_page.login(username, password)

    def navigate_to_shop(self):
        shop_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/ul/li[2]/a'))
        )
        shop_button.click()

    def handle_age_confirmation(self, dob):
        date_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/input'))
        )
        date_input.send_keys(dob)
        confirm_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/button')
        confirm_button.click()

    def select_product(self, product_name):
        product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//*[contains(text(), "{product_name}")]'))
        )
        product.click()

    def rate_product(self, rating):
        try:
            rating_xpath = f'//*[@id="root"]/div/section/section[1]/div[2]/div/div/div/div/div[1]/div/span[{rating}]'
            rating_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, rating_xpath))
            )
            rating_element.click()
            print(f"Successfully clicked on {rating}-star rating.")
        except Exception as e:
            print(f"Failed to rate the product with {rating} stars: {e}")

    def is_product_already_rated(self):
        """:raise the product radted???
        """
        try:
            review_message = self.driver.find_element_by_xpath(
                "//*[contains(text(), 'You have already reviewed this product.')]")
            if review_message.is_displayed():
                return True
        except:
            return False

    def verify_rating_submission(self, username):
        try:
            # Wait for the comments section to load
            comments = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@id="root"]/div/section/section/div/div[1]/div/div[1]/h5'))
            )

            # Check if any comment contains the username
            for comment in comments:
                if username in comment.text:
                    print(f"Username '{username}' found in product comments.")
                    return True

            print(f"Username '{username}' not found in product comments.")
            return False
        except Exception as e:
            print(f"Verification failed: {e}")
            return False

