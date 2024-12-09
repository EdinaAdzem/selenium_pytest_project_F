from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShippingCostPage:
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[1]')
    EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/form/input[1]")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/form/input[2]")
    SIGNIN_BUTTON = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/form/button")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/form/div[2]")
    STORE_LINK = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div/ul/li[2]/a')
    CART_ICON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/div[3]/svg/path')
    SHIPPING_COST = (By.XPATH, '//*[@id="root"]/div/section/div/div[1]/div/div[2]/h5[2]')
    TOTAL_COST = (By.XPATH, '//*[@id="root"]/div/section/div/div[1]/div/div[4]')
    #//*[@id="root"]/div/section/div/div[1]/div/div[4] - total
    #//*[@id="root"]/div/section/div/div[1]/div/div[2] - shipping
    #//*[@id="root"]/div/section/div/div[1]/div/div[1]/div/div/div[1]/a


    # Add product-related XPaths for parameterization in tests
    ITEM = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[3]/div')
    PRODUCT_XPATH = (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[3]/div/img')
    QUANTITY_INPUT_XPATH = (
        By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/input')
    ADD_TO_CART_XPATH = (
        By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/div/div[2]/button')

    def __init__(self, driver):
        self.driver = driver

    def handle_age_confirmation(self, dob):
        try:
            # Wait for the date input field to be visible
            date_input = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/input'))
            )
            # Clear the input field and enter the date of birth
            date_input.clear()
            date_input.send_keys(dob)
            print(f"Entered date of birth: {dob}")

            # Wait for and click the confirm button
            confirm_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div/button'))
            )
            confirm_button.click()
            print("Clicked on the confirm button to bypass age verification.")

        except Exception as e:
            print(f"Error occurred during age verification handling: {e}")

    def login(self, username, password):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.EMAIL_FIELD)).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.SIGNIN_BUTTON).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.STORE_LINK))

    def navigate_to_store(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.STORE_LINK)).click()

    def search_and_add_items(self, product_xpath, quantity_input_xpath, add_to_cart_xpath, quantity):
        # Wait for the product element to be clickable and click it
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(product_xpath))

        # Wait for the quantity input field to be visible and send keys (quantity)
        quantity_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(quantity_input_xpath)
        )
        quantity_input.clear()  # Clear any pre-filled values (optional but can be helpful)
        quantity_input.send_keys(str(quantity))

        # Wait for the 'Add to Cart' button to be clickable and click it
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(add_to_cart_xpath)).click()

    def navigate_to_cart(self):
        print("Navigating to the cart page directly...")
        self.driver.get("https://grocerymate.masterschool.com/checkout")
        print("Successfully navigated to the cart page.")

    def get_shipping_and_total_cost(self):
        shipping_cost = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SHIPPING_COST)
        ).text
        total_cost = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TOTAL_COST)
        ).text

        # Clean the shipping cost text and convert to float
        shipping_cost = float(shipping_cost.replace('€', '').replace('\n', '').strip())

        # Clean the total cost text (remove 'Total:' and convert to float)
        total_cost = float(total_cost.replace('€', '').replace('Total:', '').replace('\n', '').strip())

        try:
            total_cost = float(total_cost)
        except ValueError:
            print(f"Error converting total cost to float: {total_cost}")
            total_cost = float('nan')  # Set to NaN if conversion fails

        return shipping_cost, total_cost
