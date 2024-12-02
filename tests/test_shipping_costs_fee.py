import unittest
from selenium import webdriver
from pages.shipping_cost_pom import ShippingCostPage
from pages.age_verification_pom import AgeVerificationPage

url = "https://grocerymate.masterschool.com"
class TestShippingCost(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(url)
        print(f"Opened website: {url}")
        cls.driver.delete_all_cookies()
        print("Deleted all cookies to start fresh session.")

    @classmethod
    def tearDownClass(cls):
        print("Test completed, quitting the driver.")
        cls.driver.quit()

    def test_shipping_costs_for_total_less_than_20(self):
        shipping_cost_page = ShippingCostPage(self.driver)

        # Login first
        print("Logging in...")
        shipping_cost_page.login("colamityjane@test.com", "jane1234")
        print("Login successful.")

        # Navigate to the shop after logging in
        print("Navigating to the store...")
        shipping_cost_page.navigate_to_store()

        # Handle age verification if it pops up
        dob = "01/01/1990"
        print("Handling age verification...")
        shipping_cost_page.handle_age_confirmation(dob)
        print("Age verification completed.")
        test_data = [
            ("18.01.1981", 5, 15.00, 5),  # (total < 20) shipping cost 5
        ]

        for dob, quantity, expected_total_cost, expected_shipping_cost in test_data:
            print(f"Adding {quantity} items to the cart...")
            shipping_cost_page.search_and_add_items(
                ShippingCostPage.PRODUCT_XPATH,
                ShippingCostPage.QUANTITY_INPUT_XPATH,
                ShippingCostPage.ADD_TO_CART_XPATH,
                quantity
            )
            print(f"{quantity} items added to the cart.")
            print("Navigating to the cart to check items and total cost...")
            shipping_cost_page.navigate_to_cart()
            print("Fetching updated shipping and total cost...")
            shipping_cost, total_cost = shipping_cost_page.get_shipping_and_total_cost()
            print(f"Shipping cost: {shipping_cost}, Total cost: {total_cost}")
            # total is less than 20
            self.assertEqual(shipping_cost, expected_shipping_cost,
                             f"Expected shipping cost {expected_shipping_cost}, but got {shipping_cost}")

            print("Assertions passed.")


if __name__ == "__main__":
    unittest.main()
