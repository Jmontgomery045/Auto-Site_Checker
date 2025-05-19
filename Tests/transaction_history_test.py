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

class test_04TransactionHistory():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_04TransactionHistory(self):
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

            time.sleep(1)
            elements = self.driver.find_elements(By.CSS_SELECTOR,"div[data-actionable=\"PromptToUpdate.MarketingPreferencesSplitByProduct.Button.OptInToAll.Button\"]")
            if len(elements) > 0:
                self.driver.find_element(By.CSS_SELECTOR,"button[data-actionable=\"PromptToUpdate.MarketingPreferencesSplitByProduct.Button.OptInToAll.Button\"]").click()
                self.driver.find_element(By.CSS_SELECTOR,"button[data-actionable=\"Core.MarketingPreferencesSplitByProduct.Button.Confirm\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "button[data-actionable=\"Header.LoggedIn.buttonMyAccount\"]")))
            self.driver.find_element(By.CSS_SELECTOR,"button[data-actionable=\"Header.LoggedIn.buttonMyAccount\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-actionable=\"MyAccount.MenuItem.TransactionHistory\"]")))
            self.driver.find_element(By.CSS_SELECTOR,"div[data-actionable=\"MyAccount.MenuItem.TransactionHistory\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-actionable=\"MyAccount.MenuItem.period_last_30_days\"]")))
            self.driver.find_element(By.CSS_SELECTOR,"div[data-actionable=\"MyAccount.MenuItem.period_last_30_days\"]").click()
            
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-actionable=\"MyAccount.TransactionResultsItem.toggleTransaction\"]")))
            elements = self.driver.find_elements(By.CSS_SELECTOR, "div[data-actionable=\"MyAccount.TransactionResultsItem.toggleTransaction\"]")

            assert len(elements) > 0
            return True
        except Exception as e:
            test_failure('Transaction History', e)
            return False

