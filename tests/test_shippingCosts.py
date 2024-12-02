import unittest
from selenium import webdriver
from pages.shipping_cost_pom import ShippingCostPage

class TestShippingCosts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://grocerymate.masterschool.com")

    def tearDown(self):
        self.driver.quit()

    def test_shipping_costs_free_shipping(self):
        shipping_cost_page = ShippingCostPage(self.driver)
        shipping_cost_page.login("colamityjane@test.com", "jane1234")
        shipping_cost_page.handle_age_confirmation("01-01-1981")
        self.assertFalse(shipping_cost_page.is_age_validation_triggered(), "Age verification failed.")

        #go the the store to pick an item
        shipping_cost_page.navigate_to_store()
        shipping_cost_page.search_and_add_items(
            ShippingCostPage.PRODUCT_XPATH,
            ShippingCostPage.QUANTITY_INPUT_XPATH,
            ShippingCostPage.ADD_TO_CART_XPATH,
            15
        )

        #go to cart
        shipping_cost_page.navigate_to_cart()
        shipping_cost, total_cost = shipping_cost_page.get_shipping_and_total_cost()

        self.assertEqual(total_cost, 22.50, f"Expected total 22.50, but got {total_cost}")
        self.assertEqual(shipping_cost, 0, f"Expected shipping 0, but got {shipping_cost}")

    def test_shipping_costs_with_shipping(self):
        shipping_cost_page = ShippingCostPage(self.driver)

        shipping_cost_page.login("colamityjane@test.com", "jane1234")
        shipping_cost_page.handle_age_confirmation("01-01-1981")
        self.assertFalse(shipping_cost_page.is_age_validation_triggered(), "Age verification failed.")

        shipping_cost_page.navigate_to_store()
        shipping_cost_page.search_and_add_items(
            ShippingCostPage.PRODUCT_XPATH,
            ShippingCostPage.QUANTITY_INPUT_XPATH,
            ShippingCostPage.ADD_TO_CART_XPATH,
            12
        )

        shipping_cost_page.navigate_to_cart()
        shipping_cost, total_cost = shipping_cost_page.get_shipping_and_total_cost()

        self.assertEqual(total_cost, 18.00, f"Expected total 18.00, but got {total_cost}")
        self.assertEqual(shipping_cost, 5, f"Expected shipping 5, but got {shipping_cost}")

if __name__ == "__main__":
    unittest.main()
