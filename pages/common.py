from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class CommonPage:
    def __init__(self, driver, default_timeout=15):
        self.driver = driver
        self.default_timeout = default_timeout

    def wait_for_element(self, by, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
        except TimeoutException:
            print(f"Timeout while waiting for element: {locator}")
            raise

    def wait_for_clickable(self, by, locator, timeout=None):
        timeout = timeout or self.default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
        except TimeoutException:
            print(f"Timeout while waiting for clickable element: {locator}")
            raise

    def click(self, by, locator, timeout=None):
        print(f"Attempting to click: {locator}")  # Debugging line
        element = self.wait_for_clickable(by, locator, timeout)
        try:
            element.click()
        except Exception as e:
            print(f"Error clicking element: {locator}, error: {e}")
            raise

    def find_element(self, by, locator):
        try:
            return self.driver.find_element(by, locator)
        except Exception as e:
            print(f"Error finding element: {locator}, error: {e}")
            raise

    def enter_text(self, by, locator, text, timeout=None):
        element = self.wait_for_element(by, locator, timeout)
        try:
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Error entering text in element: {locator}, error: {e}")
            raise

    def get_text(self, by, locator, timeout=None):
        element = self.wait_for_element(by, locator, timeout)
        try:
            return element.text
        except Exception as e:
            print(f"Error getting text from element: {locator}, error: {e}")
            raise