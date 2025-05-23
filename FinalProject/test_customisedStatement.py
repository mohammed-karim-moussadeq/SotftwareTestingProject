# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestCustomisedStatement():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testCS1Valid(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 695)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2023-07-04")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2025-01-20")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("40")
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""


    def test_testCS2negativeNum(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 695)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("-5")
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(1) > tr:nth-child(1) > td").click()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2006-12-12")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2007-12-12")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(2)").click()
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == "Negative numbers are not allowed"
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""


    def test_testCS3alphabets(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 695)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("abc")
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2007-12-12")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2007-12-12")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == "Characters are not allowed"
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

    def test_testCS4blank(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 695)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(1) > tr:nth-child(1) > td").click()
        self.driver.find_element(By.NAME, "accountno").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == "Account Number must not be blank"
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == "From Date Field must not be blank"
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == "To Date Field mus tnot be blank"
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == "Characters are not allowed"
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == "Characters are not allowed"

    def test_testCS5specialCharacter(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 629)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("@#$")
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2007-12-12")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2008-12-12")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == "Special Characters are not allowed"
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

    def test_testCS6leadingZeros(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 629)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(2)").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("001")
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2001-12-12")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2002-12-12")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == "Invalid number"
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

    def test_testCS7longNumber(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 629)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("9999999999")
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2001-02-12")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2020-12-12")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("500")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

    def test_testCS8invalidDate(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 637)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("0010-01-01")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("0001-01-31")
        self.driver.find_element(By.NAME, "tdate").send_keys("0001-01-11")
        self.driver.find_element(By.NAME, "tdate").send_keys("0001-01-01")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == "Invalid date"
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == "Invalid date"
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

    def test_testCS9backwardsDate(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 637)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td").click()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2025-12-12")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2020-12-12")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == "From Date cannot be greater than To Date"
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

    def test_testCS10negativeAmount(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 637)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td").click()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2000-02-02")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2002-02-02")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("-500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == "Negative Transaction Amount is invalid"
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

    def test_testCS11specialCharacterAmount(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 637)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "tbody:nth-child(2) > tr > td").click()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2001-02-02")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2002-02-02")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("@#$")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == "Special characters are not allowed"
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

    def test_testCS12alphabetsAmount(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 637)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2001-02-02")
        self.driver.find_element(By.NAME, "tdate").send_keys("2002-02-02")
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("abc")
        self.driver.find_element(By.NAME, "numtransaction").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == "Characters are not allowed"
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

    def test_testCS13largeAmount(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 637)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(1)").click()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2001-02-02")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2002-02-02")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("9999999999")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

    def test_testCS14alphabetsTransactions(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 632)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2001-02-02")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2002-02-02")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(2)").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("abs")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == "Characters are not allowed"

    def test_testCS15specialCharactersTransactions(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 632)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(1)").click()
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2002-02-02")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2022-02-02")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("!@#")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == "Special Characters are not allowed"

    def test_testCS16negativeNumberTransaction(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 632)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2002-02-02")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2003-02-02")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("-50")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(13) > td:nth-child(1)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == "Negative numbers are not allowed"

    def test_testCS17largeNumbersTransaction(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(919, 632)
        self.driver.execute_script("""
                               let footer = document.querySelector('p.barone');
                               if (footer) {
                                   footer.style.display = 'none';
                               }

                               let ad = document.querySelector('img[alt="Try Xero for free"]');
                               if (ad && ad.parentElement) {
                                   ad.parentElement.style.display = 'none';
                               }
                           """)
        self.driver.find_element(By.LINK_TEXT, "Customised Statement").click()
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1")
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys("2002-02-02")
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys("2003-02-02")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("500")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("9999999999")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) > td:nth-child(2)").click()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        assert error_message == ""
        error_message2 = self.driver.find_element(By.XPATH, '//*[@id="message26"]').text
        assert error_message2 == ""
        error_message3 = self.driver.find_element(By.XPATH, '//*[@id="message27"]').text
        assert error_message3 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message12"]').text
        assert error_message4 == ""
        error_message4 = self.driver.find_element(By.XPATH, '//*[@id="message13"]').text
        assert error_message4 == ""

