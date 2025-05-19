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

class test_04HorseRacingBetPlacement():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_04HorseRacingBetPlacement(self):
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
            self.driver.find_element(By.CSS_SELECTOR,
                                     "a[data-actionable=\"core.navigation.ProductSwitcher.ProductLink.link.sports\"]").click()
            
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "a[data-actionable=\"Sportsbook.HomePage.SportsCarousel.horseRacing\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "a[data-actionable=\"Sportsbook.HomePage.SportsCarousel.horseRacing\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "a[data-actionable=\"RaceGrid.eventLink\"]")))
            events = self.driver.find_elements(By.CSS_SELECTOR, "a[data-actionable=\"RaceGrid.eventLink\"]")
            if len(events) > 2:
                events[2].click()
            else:
                print("Not enough events found.")
                return False
            
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-actionable=\"Price\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "div[data-actionable=\"Price\"]").click()

            self.driver.find_element(By.ID, "stake-1").click()
            self.driver.find_element(By.ID, "stake-1").send_keys("0.2")
            self.driver.find_element(By.CSS_SELECTOR, "button[data-actionable=\"Betslip.Footer.placeBet\"]").click()
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "span[data-actionable=\"BetConfirmation.success\"]")))
            elements = self.driver.find_elements(By.CSS_SELECTOR, "span[data-actionable=\"BetConfirmation.success\"]")
            assert len(elements) > 0
            return True
        except Exception as e:
            test_failure('Horse', e)
            return False

