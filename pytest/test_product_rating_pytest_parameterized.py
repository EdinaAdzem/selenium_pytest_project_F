import pytest
from selenium import webdriver
from pages.product_rating_pom import ProductRatingPage

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://grocerymate.masterschool.com")
    yield driver
    driver.quit()

# Parameterized to add more test case options here
@pytest.mark.parametrize(
    "username, password, product_name, rating",
    [
        ("colamityjane@test.com", "jane1234", "Oranges", 3),
        ("johnsmith@test.com", "smith1234", "Apples", 4),
        ("test@test.com", "678", "Bananas", 5),
    ],
)
def test_product_rating(setup, username, password, product_name, rating):
    driver = setup
    product_rating_page = ProductRatingPage(driver)

    # Log in as an existing user
    print(f"Logging in with user: {username}")
    product_rating_page.login(username, password)

    # Navigate to the shop page
    print("Navigating to the shop page...")
    product_rating_page.navigate_to_shop()

    # Handle age confirmation popup
    print("Handling age confirmation popup...")
    product_rating_page.handle_age_confirmation("01-01-1981")

    # Select a product to rate
    print(f"Selecting product: {product_name} to rate...")
    product_rating_page.select_product(product_name)

    # Submit a rating
    print(f"Submitting a {rating}-star rating...")
    product_rating_page.rate_product(rating)

    # Verify the rating submission
    user_display_name = username.split("@")[0]
    print(f"Verifying rating for user: {user_display_name}")
    assert product_rating_page.verify_rating_submission(
        user_display_name
    ), f"Rating submission verification failed for user {user_display_name}."
    print("Product rating successfully verified!")