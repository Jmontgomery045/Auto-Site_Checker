import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_failure(test, error):
    print(test + ": Failure")
    print(error)

class test_02Deposit():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_02Deposit(self):
        try:
            print("Loading environment variables...")
            load_dotenv()
            print("Environment variables loaded.")

            self.driver.get("https://www.betfred.com/")
            self.driver.find_element(By.CSS_SELECTOR, ".wscrBannerContentInner .wscrOk").click()
            self.driver.find_element(By.CSS_SELECTOR,
                                     "button[data-actionable=\"Header.LoggedOut.buttonLogin\"]").click()
            self.driver.find_element(By.ID, "Login.username").send_keys(os.getenv("USER"))
            self.driver.find_element(By.ID, "Login.password").send_keys(os.getenv("PASS"))
            self.driver.find_element(By.CSS_SELECTOR, "button[data-actionable=\"Login.login\"]").click()

            time.sleep(2)
            elements = self.driver.find_elements(By.CSS_SELECTOR,"div[data-actionable=\"PromptToUpdate.MarketingPreferencesSplitByProduct.Button.OptInToAll.Button\"]")
            if len(elements) > 0:
                self.driver.find_element(By.CSS_SELECTOR,"button[data-actionable=\"PromptToUpdate.MarketingPreferencesSplitByProduct.Button.OptInToAll.Button\"]").click()
                self.driver.find_element(By.CSS_SELECTOR,"button[data-actionable=\"Core.MarketingPreferencesSplitByProduct.Button.Confirm\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "button[data-actionable=\"Header.LoggedIn.buttonMyAccount\"]")))
            self.driver.find_element(By.ID, "quick-deposit-button").click()
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div[data-actionable=\"MyAccount.MenuItem.ChoosePaymentMethod.CardPayments\"]")))
            checkbox_el = self.driver.find_elements(By.CSS_SELECTOR,"[data-actionable=\"MyAccount.PaymentSolutions.fundsPolicyConfirm.unchecked\"]")
            if len(checkbox_el) > 0:
                self.driver.find_element(By.CSS_SELECTOR,"[data-actionable=\"MyAccount.PaymentSolutions.fundsPolicyConfirm.unchecked\"]").click()
            self.driver.find_element(By.CSS_SELECTOR,"div[data-actionable=\"MyAccount.MenuItem.ChoosePaymentMethod.CardPayments\"]").click()
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "iframe[ID=\"paymentsIFrame\"]")))
            iframe_el = self.driver.find_elements(By.ID, "paymentsIFrame")
            assert len(iframe_el) > 0
            return True
        except Exception as e:
            test_failure('Deposit', e)
            return False
