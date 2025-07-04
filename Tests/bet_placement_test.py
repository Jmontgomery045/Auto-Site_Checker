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

class test_03BetPlacement():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_03BetPlacement(self):
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

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "button[data-actionable=\"Header.LoggedIn.buttonMyAccount\"]")))
            self.driver.get("https://www.betfred.com/sports/football")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "span[data-actionable=\"Price.name\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "span[data-actionable=\"Price.name\"]").click()
            self.driver.find_element(By.ID, "stake-1").click()
            self.driver.find_element(By.ID, "stake-1").send_keys("0.5")
            self.driver.find_element(By.CSS_SELECTOR, "button[data-actionable=\"Betslip.Footer.placeBet\"]").click()
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "span[data-actionable=\"BetConfirmation.success\"]")))
            elements = self.driver.find_elements(By.CSS_SELECTOR, "span[data-actionable=\"BetConfirmation.success\"]")
            assert len(elements) > 0
            return True
        except Exception as e:
            test_failure('Bet Placement', e)
            return False

