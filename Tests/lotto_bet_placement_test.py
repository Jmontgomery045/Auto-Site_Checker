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

class test_04LottoBetPlacement():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_04LottoBetPlacement(self):
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
                (By.CSS_SELECTOR, "a[data-actionable=\"Sportsbook.HomePage.SportsCarousel.lotto\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "a[data-actionable=\"Sportsbook.HomePage.SportsCarousel.lotto\"]").click()

            # Navigate to specific url
            self.driver.get("https://www.betfred.com/lotto/nifty-50")


            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "a[data-actionable=\"Lotto.SelectLotto.UseLuckyDip\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "a[data-actionable=\"Lotto.SelectLotto.UseLuckyDip\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "button[data-actionable=\"Lotto.DrawsPage.Continue\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "button[data-actionable=\"Lotto.DrawsPage.Continue\"]").click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, "button[data-actionable=\"Lotto.DrawsPage.Continue\"]").click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, "button[data-actionable=\"Lotto.DrawsPage.Continue\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "a[data-actionable=\"Lotto.YourNumbers.GoToDraws\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "a[data-actionable=\"Lotto.YourNumbers.GoToDraws\"]").click()

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "label[data-actionable=\"LottoApp.Toggle\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "label[data-actionable=\"LottoApp.Toggle\"]").click()
            
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "a[data-actionable=\"Lotto.DrawsPage.Continue\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "a[data-actionable=\"Lotto.DrawsPage.Continue\"]").click()
            
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "input[data-actionable=\"Lotto.BetslipStake.Input.Single\"]")))
            self.driver.find_element(By.CSS_SELECTOR, "input[data-actionable=\"Lotto.BetslipStake.Input.Single\"]").send_keys("0.1")

            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, "button[data-actionable=\"Lotto.BetslipFooter.PlaceBet\"]").click()

            time.sleep(1)

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-actionable=\"BetConfirmationPage.BetConfirmation.FloatingMessage\"]")))
            elements = self.driver.find_elements(By.CSS_SELECTOR, "div[data-actionable=\"BetConfirmationPage.BetConfirmation.FloatingMessage\"]")
            assert len(elements) > 0
            return True
        except Exception as e:
            test_failure('Lotto', e)
            return False

