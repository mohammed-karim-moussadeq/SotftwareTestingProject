import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Justin Wheeler (100982020)

class TestNewAccount():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_emptyID(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        element = self.driver.find_element(By.XPATH, "//label[@id='message14']")
        assert element.is_displayed()
        assert element.text == "Customer ID is required"

    def test_nonCharID(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        element = self.driver.find_element(By.XPATH, "//label[@id='message14']")
        assert element.is_displayed()
        assert element.text == "Characters are not allowed"
        self.driver.find_element(By.NAME, "cusid").clear()
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        element = self.driver.find_element(By.XPATH, "//label[@id='message14']")
        assert element.is_displayed()
        assert element.text == "Characters are not allowed"

    def test_specialCharID(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        element = self.driver.find_element(By.XPATH, "//label[@id='message14']")
        assert element.is_displayed()
        assert element.text == "Special characters are not allowed"
        self.driver.find_element(By.NAME, "cusid").clear()
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#")
        element = self.driver.find_element(By.XPATH, "//label[@id='message14']")
        assert element.is_displayed()
        assert element.text == "Special characters are not allowed"

    def test_blankCharID(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        element = self.driver.find_element(By.XPATH, "//label[@id='message14']")
        assert element.is_displayed()
        assert element.text == "Characters are not allowed"

    def test_spaceCharID(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(" ")
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        element = self.driver.find_element(By.XPATH, "//label[@id='message14']")
        assert element.is_displayed()
        assert element.text == "First character cannot have space"

    def test_emptyDeposit(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys(Keys.TAB)
        element = self.driver.find_element(By.XPATH, "//label[@id='message19']")
        assert element.is_displayed()
        assert element.text == "Initial Deposit must not be blank"

    def test_charDeposit(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("1234Acc")
        element = self.driver.find_element(By.XPATH, "//label[@id='message19']")
        assert element.is_displayed()
        assert element.text == "Characters are not allowed"
        self.driver.find_element(By.NAME, "inideposit").clear()
        self.driver.find_element(By.NAME, "inideposit").send_keys("Acc123")
        element = self.driver.find_element(By.XPATH, "//label[@id='message19']")
        assert element.is_displayed()
        assert element.text == "Characters are not allowed"

    def test_specialCharDeposit(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123!@#")
        element = self.driver.find_element(By.XPATH, "//label[@id='message19']")
        assert element.is_displayed()
        assert element.text == "Special characters are not allowed"
        self.driver.find_element(By.NAME, "inideposit").clear()
        self.driver.find_element(By.NAME, "inideposit").send_keys("!@#")
        element = self.driver.find_element(By.XPATH, "//label[@id='message19']")
        assert element.is_displayed()
        assert element.text == "Special characters are not allowed"

    def test_spaceCharDeposit(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123 12")
        element = self.driver.find_element(By.XPATH, "//label[@id='message19']")
        assert element.is_displayed()
        assert element.text == "Special characters are not allowed"

    def test_spaceDeposit(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys(" ")
        self.driver.find_element(By.NAME, "inideposit").send_keys(Keys.TAB)
        element = self.driver.find_element(By.XPATH, "//label[@id='message19']")
        assert element.is_displayed()
        assert element.text == "First character cannot have space"

    def test_savingsAccount(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        element = self.driver.find_element(By.NAME, "selaccount")
        element.click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(1)").click()
        dropdown = Select(element)
        selected_option = dropdown.first_selected_option
        assert selected_option.text == "Savings"

    def test_currentAccount(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        element = self.driver.find_element(By.NAME, "selaccount")
        element.click()
        self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        dropdown = Select(element)
        selected_option = dropdown.first_selected_option
        assert selected_option.text == "Current"

    def test_resetForm(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("qwer")
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123456")
        self.driver.find_element(By.NAME, "reset").click()
        element = self.driver.find_element(By.NAME, "cusid")
        assert element.get_attribute("value") == ""
        element = self.driver.find_element(By.NAME, "inideposit")
        assert element.get_attribute("value") == ""

    def test_submitIncorrectForm(self):
        self.driver.get("https://demo.guru99.com/V4")
        self.driver.set_window_size(1597, 1009)

        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618468")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("rYsapan")
        self.driver.find_element(By.NAME, "btnLogin").click()
        time.sleep(1)

        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("1234567")
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("9999")
        self.driver.find_element(By.NAME, "button2").click()
        time.sleep(1)
        assert self.driver.switch_to.alert.text == "Customer does not exist!!"

    def test_submitCorrectForm(self):
        self.driver.get("https://demo.guru99.com/V4")
        self.driver.set_window_size(1597, 1009)

        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618468")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("rYsapan")
        self.driver.find_element(By.NAME, "btnLogin").click()
        time.sleep(1)

        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("34967")
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("9999")
        self.driver.find_element(By.NAME, "button2").click()
        time.sleep(1)

        element = self.driver.find_element(By.XPATH, "//p[@class='heading3']")
        assert element.is_displayed()
        assert element.text == "Account generated succussfully"

    def test_continueSubmittedForm(self):
        self.driver.get("https://demo.guru99.com/V4")
        self.driver.set_window_size(1597, 1009)

        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618468")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("rYsapan")
        self.driver.find_element(By.NAME, "btnLogin").click()
        time.sleep(1)

        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys("34967")
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("9999")
        self.driver.find_element(By.NAME, "button2").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//a[normalize-space()='Continue']").click()
        time.sleep(1)

        element = self.driver.find_element(By.XPATH, "//td[normalize-space()='Manger Id : mngr618468']")
        assert element.is_displayed()















