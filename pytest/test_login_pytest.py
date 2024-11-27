import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page_pom import LoginPage


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://grocerymate.masterschool.com")
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "email,password",
    [
        ("colamityjane@test.com", "jane1234"),
    ]
)
def test_login(setup, email, password):
    driver = setup
    login_page = LoginPage(driver)

    login_page.login(email, password)
    login_page.click_login()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://grocerymate.masterschool.com/auth")
    )
    assert driver.current_url == "https://grocerymate.masterschool.com/auth"

    logout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/div/button"))
    )
    assert logout_button.is_displayed()
