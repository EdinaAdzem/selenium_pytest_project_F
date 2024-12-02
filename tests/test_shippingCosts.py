import unittest
from selenium import webdriver
from pages.shipping_cost_pom import ShippingCostPage
from pages.age_verification_pom import AgeVerificationPage


# URL for the website
url = "https://grocerymate.masterschool.com"
dob = "18.01.1981"  # Ensure this format matches what the site expects

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

    def test_shipping_costs(self):
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

        # Test data for shopping and shipping costs
        test_data = [
            ("18.01.1981", 15, 22.50, 0),  # (total > 20) free shipping
        ]

        for dob, quantity, expected_total_cost, expected_shipping_cost in test_data:
            print(f"Adding {quantity} items to the cart...")

            # Adding items to the cart
            shipping_cost_page.search_and_add_items(
                ShippingCostPage.PRODUCT_XPATH,
                ShippingCostPage.QUANTITY_INPUT_XPATH,
                ShippingCostPage.ADD_TO_CART_XPATH,
                quantity
            )
            print(f"{quantity} items added to the cart.")
            print("Navigating to the cart to check items and total cost...")
            shipping_cost_page.navigate_to_cart()

            # Fetch the latest shipping and total cost values this will always be incremented with the set user
            print("Fetching updated shipping and total cost...")
            shipping_cost, total_cost = shipping_cost_page.get_shipping_and_total_cost()
            print(f"Shipping cost: {shipping_cost}, Total cost: {total_cost}")
            print(f"Verifying that shipping cost is {expected_shipping_cost} when total cost is greater than 20...")

            # Verifying that shipping cost is 0 if total cost is >= 20
            if total_cost >= 20:
                self.assertEqual(shipping_cost, 0,
                                 f"Expected shipping cost to be 0 for total >= 20, but got {shipping_cost}")
            else:
                # If total < 20, shipping free
                self.assertEqual(shipping_cost, expected_shipping_cost,
                                 f"Expected shipping {expected_shipping_cost}, shipping_ {shipping_cost}")

            print("Assertions passed.")
if __name__ == "__main__":
    unittest.main()
