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

class test_04ToteBetPlacement():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_04ToteBetPlacement(self):
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
            
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "a[data-actionable=\"core.navigation.ProductSwitcher.ProductLink.link.tote\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "a[data-actionable=\"core.navigation.ProductSwitcher.ProductLink.link.tote\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.ID,"totepool-iframe")))
            iframe1 = self.driver.find_element(By.ID,"totepool-iframe")
            self.driver.switch_to.frame(iframe1)

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "button[data-testid=\"race-item\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "button[data-testid=\"race-item\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-testid=\"checkbox-container\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "div[data-testid=\"checkbox-container\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "input[data-actionable=\"StakeInput\"]")))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(By.CSS_SELECTOR, "input[data-actionable=\"StakeInput\"]"))


            print("Adding Stake...")
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "input[data-actionable=\"StakeInput\"]")))
            self.driver.execute_script("""
                var betamount = document.querySelector('[data-testid="submit-button"]');
                betamount.focus();
            """)
            elem = self.driver.switch_to.active_element
            elem.send_keys('1.00')


            print("Submitting bet...")
            WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid=\"submit-button\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "button[data-testid=\"submit-button\"]").click()

            print("End Time")
            time.sleep(100)
            return True
        except Exception as e:
            test_failure('Bet Placement', e)
            return False

