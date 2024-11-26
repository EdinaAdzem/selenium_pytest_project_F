from pages.payment_pom import PaymentPage


class TestPayment:
    def test_payment(self):
        self.login_page.login("colamityjane@test.com", "jane1234")
        self.driver.get("https://grocerymate.masterschool.com/checkout")
        payment_page = PaymentPage(self.driver)
        payment_page.complete_payment(
            address="addressColamity",
            city="cityColamity",
            postcode="72160",
            card_number="4111111111111111",
            name_on_card="Colamity Jane",
            expiration_date="12/25",
            cvv="123"
        )

        payment_page.wait_for_payment_confirmation()
        print("Payment successful!")
