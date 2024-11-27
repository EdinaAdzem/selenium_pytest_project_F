import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page_pom import LoginPage
from pages.common import CommonPage
from pages.age_verification_pom import AgeVerificationPage

url = 'https://grocerymate.masterschool.com'

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    yield driver
    driver.quit()

@pytest.mark.parametrize(
    "username, password, dob, expected_error",
    [
        ("colamityjane@test.com", "jane1234", "01-01-1981", None),
        ("younguser@test.com", "young123", "01-01-2010", "Age verification failed")
    ]
)
def test_shop_cart(setup, username, password, dob, expected_error):
    driver = setup
    login_page = LoginPage(driver)
    common = CommonPage(driver)
    age_verification_page = AgeVerificationPage(driver)

    print(f"Logging in with user: {username}")
    login_page.login(username, password)

    print("Navigating to the shop page...")
    shop_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/ul/li[2]/a'))
    )
    shop_button.click()

    # Handle age confirmation
    print(f"Handling age confirmation for DOB: {dob}")
    age_verification_page.handle_age_confirmation(dob)

    if expected_error:
        assert age_verification_page.is_age_validation_triggered(), f"Expected error but none was found."
        print(f"Error correctly displayed for underage user: {dob}")
    else:
        print("Adding product to cart...")
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/button'))
        )
        add_to_cart_button.click()

        print("Navigating to the checkout page...")
        driver.get("https://grocerymate.masterschool.com/checkout")
        print("Verifying the product in the cart...")
        product_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Celery")]'))
        )
        assert product_name.is_displayed(), "Product not found in the cart!"
        print("Product successfully found in the cart!")
