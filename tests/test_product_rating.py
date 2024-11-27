import pytest
from selenium import webdriver
from pages.product_rating_pom import ProductRatingPage

@pytest.fixture(scope="function")
def setup():
    # Initialize the WebDriver and set up the environment
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://grocerymate.masterschool.com")
    yield driver
    driver.quit()

def test_product_rating(setup):
    driver = setup
    product_rating_page = ProductRatingPage(driver)

    # Log in as an existing user
    print("Logging in with existing user... colamity jane")
    product_rating_page.login("colamityjane@test.com", "jane1234")

    # Navigate to the shop page
    print("Navigating to the shop page...")
    product_rating_page.navigate_to_shop()

    # Handle age confirmation popup
    print("Handling age confirmation popup...")
    product_rating_page.handle_age_confirmation("01-01-1981")

    # rate any product also hardcoded for now
    print("Selecting a product to rate...")
    product_rating_page.select_product("Oranges")

    # Submit a rating - hardcoded for now
    print("Submitting a 3-star rating...")
    product_rating_page.rate_product(3)

    # check the user has rated
    username = "colamity jane"
    print("Verifying rating")
    assert product_rating_page.verify_rating_submission(
        username), f"Rating submission verification failed for user {username}."
    print("Product rating successfully verified!")
