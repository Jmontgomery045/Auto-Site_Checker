import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_failure(test, error):
    print(test + ": Failure")
    print(error)

class test_05GamesSpinSpribe():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_05GamesSpinSpribe(self):
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
                (By.CSS_SELECTOR, "a[data-actionable=\"core.navigation.ProductSwitcher.ProductLink.link.games\"]")))
            self.driver.find_element(By.CSS_SELECTOR,"a[data-actionable=\"core.navigation.ProductSwitcher.ProductLink.link.games\"]").click()

            self.driver.get("https://www.betfred.com/games/play/aviator")

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.ID,"game_iframe")))
            iframe1 = self.driver.find_element(By.ID,"game_iframe")
            self.driver.switch_to.frame(iframe1)

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.ID,"gameIFrame")))
            iframe2 = self.driver.find_element(By.ID,"gameIFrame")
            self.driver.switch_to.frame(iframe2)

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.ID,"spribe-game")))
            iframe3 = self.driver.find_element(By.ID,"spribe-game")
            self.driver.switch_to.frame(iframe3)

            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR,"button.btn.btn-success.bet.ng-star-inserted")))
            button = self.driver.find_element(By.CSS_SELECTOR,"button.btn.btn-success.bet.ng-star-inserted")
            button.click()
            time.sleep(5)

            return True
        except Exception as e:
            test_failure('Games Spin', e)
            return False

