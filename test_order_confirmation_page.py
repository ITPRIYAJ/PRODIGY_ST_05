import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_product_to_cart_xpath(driver):
    driver.get("https://demowebshop.tricentis.com/")

     # Wait for the login link to be clickable
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))).click()
    except TimeoutException:
        print("Login link not found")

    # Enter username and password
    username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Email")))
    username_input.send_keys("nilaj08@gmail.com")
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Password")))
    password_input.send_keys("Nila123")

    # Submit the login form
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "RememberMe"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='button-1 login-button']"))).click()


    # Search for 'Health Book'
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='q']"))
    )
    search_box.send_keys("Health Book")
    search_box.submit()

    # Click the product link from search results using XPath
    product_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h2[@class='product-title']/a[contains(text(),'Health Book')]"))
    )
    product_link.click()

    # Click Add to Cart button on product page using XPath
    add_to_cart_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Add to cart' and contains(@class,'add-to-cart-button')]"))
    )
    add_to_cart_btn.click()

    # Verify confirmation message using XPath
    confirmation = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='content']"))
    )
    assert "The product has been added to your shopping cart" in confirmation.text
    
    # Open Cart
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Shopping cart"))).click()

    # Proceed to Checkout
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "termsofservice"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Billing Address Step (Assumes pre-filled address)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@title='Continue']"))).click()

    def fill_billing_address(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Nila")
        self.driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("J")
        self.driver.find_element(By.ID, "BillingNewAddress_Email").clear()
        self.driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("nilaj08@gmail.com")
        self.driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("India")
        self.driver.find_element(By.ID, "BillingNewAddress_StateProvinceId").send_keys("Other (Non US)")
        self.driver.find_element(By.ID, "BillingNewAddress_City").send_keys("chennai")
        self.driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("porur")
        self.driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("600116")
        self.driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("9876543210")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='Billing.save()']"))).click()

    def continue_shipping(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='Shipping.save()']"))).click()

    def continue_shipping_method(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='ShippingMethod.save()']"))).click()

    def continue_payment_method(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='PaymentMethod.save()']"))).click()

    def continue_payment_info(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='PaymentInfo.save()']"))).click()

    def confirm_order(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@onclick='ConfirmOrder.save()']"))).click()

    def verify_order_success(self):
        message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
        assert "Your order has been successfully processed!" in message.text
    

   



   
