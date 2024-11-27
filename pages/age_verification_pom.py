from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AgeVerificationPage:
    def __init__(self, driver):
        self.driver = driver

    def handle_age_confirmation(self, dob):
        date_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/input'))
        )
        date_input.clear()
        date_input.send_keys(dob)

        confirm_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/button')
        confirm_button.click()

    def is_age_validation_triggered(self):
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Age verification failed")]'))
            )
            return error_message.is_displayed()
        except:
            return False
