import pytest
from selenium import webdriver
from pages.shipping_cost_pom import ShippingCostPage
from pages.age_verification_pom import AgeVerificationPage

url = "https://grocerymate.masterschool.com"
"""seperating out the unittest and pytest tests, to practice and try and solve both approaches."""
@pytest.fixture(scope="class")
def setup_driver():
    # Setup: Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    driver.delete_all_cookies()
    print(f"Opened website: {url}")
    yield driver
    print("Test completed, quitting the driver.")
    driver.quit()

@pytest.mark.parametrize("dob, quantity, expected_total_cost, expected_shipping_cost", [
    ("18.01.1981", 5, 15.00, 5),  # (total < 20) shipping cost 5
])
def test_shipping_costs_for_total_less_than_20(setup_driver, dob, quantity, expected_total_cost, expected_shipping_cost):
    driver = setup_driver
    shipping_cost_page = ShippingCostPage(driver)

    print("Logging in...")
    shipping_cost_page.login("colamityjane@test.com", "jane1234")
    print("Login successful.")

    print("Navigating to the store...")
    shipping_cost_page.navigate_to_store()

    print("Handling age verification...")
    shipping_cost_page.handle_age_confirmation(dob)
    print("Age verification completed.")

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
    assert shipping_cost == expected_shipping_cost, \
        f"Expected shipping cost {expected_shipping_cost}, but got {shipping_cost}"

    print("Assertions passed.")
