import datetime
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

def test_failure(test, error):
    print(test + ": Failure")
    print(error)

class test_04Register():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_04Register(self):
        try:
            date = datetime.datetime.now()
            splitDate = str(date).split(' ')[0].split('-')
            newDate = splitDate[2] + splitDate[1] + splitDate[0][2] + splitDate[0][3]
            three_digit_number = random.randint(100, 999)
            username = f'AUTOTEST{newDate}{three_digit_number}'
            password = 'Angjfuhe756!'
            print(username)
            print(password)
            self.driver.get("https://www.betfred.com/")
            self.driver.find_element(By.CSS_SELECTOR, ".wscrBannerContentInner .wscrOk").click()
            self.driver.find_element(By.CSS_SELECTOR,"a[data-actionable=\"Header.LoggedOut.buttonJoin\"]").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "RegistrationPage.AccountSection.email").send_keys(f'{username}@betfred.com')
            self.driver.find_element(By.ID, "RegistrationPage.AccountSection.username").send_keys(username)
            self.driver.find_element(By.ID, "RegistrationPage.AccountSection.password").send_keys(password)
            self.driver.find_element(By.CSS_SELECTOR, "div[data-actionable=\"RegistrationPage.TermsAndConditions.agree_terms\"]").click()
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, "button[data-actionable=\"RegistrationPage.NavigationButtonsPage1.Continue\"]").click()
            time.sleep(1)
            self.driver.find_element(By.ID, "RegistrationPage.PersonalSection.first_name").send_keys('John')
            self.driver.find_element(By.ID, "RegistrationPage.PersonalSection.last_name").send_keys('Testerson')
            self.driver.find_element(By.CSS_SELECTOR, "input[data-actionable=\"RegistrationPage.DateOfBirthInput.day\"]").send_keys('02')
            self.driver.find_element(By.CSS_SELECTOR, "input[data-actionable=\"RegistrationPage.DateOfBirthInput.month\"]").send_keys('02')
            self.driver.find_element(By.CSS_SELECTOR, "input[data-actionable=\"RegistrationPage.DateOfBirthInput.year\"]").send_keys('1990')
            self.driver.find_element(By.CSS_SELECTOR,"button[data-actionable=\"RegistrationPage.NavigationButtonsPage2.Continue\"]").click()
            self.driver.find_element(By.CSS_SELECTOR,"button[data-actionable=\"RegistrationPage.NavigationButtonsPage2.Continue\"]").click()
            elem = self.driver.switch_to.active_element
            elem.send_keys('9876543210')
            self.driver.execute_script("""
                    var select = document.getElementById('RegistrationPage.Dropdown.desktop-securityQuestion');
                    select.value = 'Name of a favourite family member?';
                    var event = new Event('change', { bubbles: true });
                    select.dispatchEvent(event);
                    """)
            self.driver.execute_script("""
                var answer = document.getElementById('RegistrationPage.ContactSection.mobile_security_answer');
                answer.value = 'Test';
                answer.focus();
                answer.dispatchEvent(new Event('input', { bubbles: true }));
                answer.dispatchEvent(new Event('change', { bubbles: true }));
            """)
            elem = self.driver.switch_to.active_element
            elem.send_keys('bigtest')
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR,"button[data-actionable=\"RegistrationPage.NavigationButtonsPage3.Continue\"]").click()
            time.sleep(10)
            self.driver.execute_script("""
                var postcode = document.getElementById('search');
                postcode.focus();
            """)
            elem = self.driver.switch_to.active_element
            elem.send_keys('SK6 3JP')

            # time.sleep(2)
            # options = dropdown.find_elements(By.CSS_SELECTOR, "option")
            # options[2].click()
            # self.driver.find_element(By.ID, "RegistrationPage.ContactSection.desktop_security_answer").send_keys('testy')
            time.sleep(50)
            print("Successfully registered")
            return True
        except Exception as e:
            test_failure('Register', e)
            print("Failed to register")
            return False

