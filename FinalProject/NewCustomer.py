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


class TestTestCase1():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testCase1(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.ID, "dob").send_keys("2001-06-22")
        self.driver.find_element(By.NAME, "addr").send_keys("76")
        self.driver.find_element(By.NAME, "city").send_keys("OSHAWA")
        self.driver.find_element(By.NAME, "state").send_keys("ONTARIO")
        self.driver.find_element(By.NAME, "pinno").send_keys("123456")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("123456789")
        self.driver.find_element(By.NAME, "emailid").send_keys("exampleEmail@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase2(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("1234")
        self.driver.find_element(By.ID, "dob").click()
        self.driver.find_element(By.ID, "dob").send_keys("2003-05-22")
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("66 workmen")
        self.driver.find_element(By.NAME, "city").send_keys("Ajax")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("Ontario")
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("125698")
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6479856324")
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("exampleEmail2@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase3(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Karim!@3")
        self.driver.find_element(By.ID, "dob").click()
        self.driver.find_element(By.ID, "dob").send_keys("2000-12-31")
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("76 church")
        self.driver.find_element(By.NAME, "city").send_keys("Ajax")
        self.driver.find_element(By.NAME, "state").send_keys("Ontario")
        self.driver.find_element(By.NAME, "pinno").send_keys("569874")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6479856423")
        self.driver.find_element(By.NAME, "emailid").send_keys("exampleEmail3@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase4(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("    Karim")
        self.driver.find_element(By.ID, "dob").send_keys("2003-10-15")
        self.driver.find_element(By.NAME, "addr").send_keys("96")
        self.driver.find_element(By.NAME, "city").send_keys("Hamilton")
        self.driver.find_element(By.NAME, "state").send_keys("Ontario")
        self.driver.find_element(By.NAME, "pinno").send_keys("546987")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6472365148")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail4@gmail.com")
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()

    def test_testCase5(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Karim")
        self.driver.find_element(By.ID, "dob").send_keys("2001-07-22")
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "city").send_keys("Ajax")
        self.driver.find_element(By.NAME, "state").send_keys("Ontario")
        self.driver.find_element(By.NAME, "pinno").send_keys("365897")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("4682541256")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail5@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase6(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Karim")
        self.driver.find_element(By.ID, "dob").send_keys("2009-12-05")
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("  WorkMen")
        self.driver.find_element(By.NAME, "city").send_keys("Ajax")
        self.driver.find_element(By.NAME, "state").send_keys("Ontario")
        self.driver.find_element(By.NAME, "pinno").send_keys("457813")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6547895412")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail6@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase7(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Name")
        self.driver.find_element(By.ID, "dob").send_keys("2011-11-11")
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("address1")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "state").send_keys("Ontario")
        self.driver.find_element(By.NAME, "pinno").send_keys("459576")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("647589125")
        self.driver.find_element(By.NAME, "emailid").send_keys("exampleEmail7@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase8(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Kaarim")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address8")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("1234")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("Ontario")
        self.driver.find_element(By.NAME, "pinno").send_keys("156894")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6478593215")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail8@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("112345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase9(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Karim")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address9")
        self.driver.find_element(By.NAME, "city").send_keys("Ajax@!#")
        self.driver.find_element(By.NAME, "state").send_keys("Ontario")
        self.driver.find_element(By.NAME, "pinno").send_keys("124568")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("64587859865")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail9@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase10(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("karim")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("address10")
        self.driver.find_element(By.NAME, "city").send_keys(" Ajax")
        self.driver.find_element(By.NAME, "state").send_keys("Ontario")
        self.driver.find_element(By.NAME, "pinno").send_keys("123568")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("1254879865")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase11(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address11")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("126589")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("1256487596")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail11@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase12(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("Address12")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("State1234")
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("126589")
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6475895421")
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail12@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase13(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("address")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("city")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("State@!#")
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("259874")
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("64785932564")
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("Emailexample@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase14(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("karim")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("address14")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("city")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys(" State")
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("569848")
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6589874586")
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase15(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("namee")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("address15")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("Ciity")
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys("Statee")
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys("1235AB")
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("3659847852")
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail15@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase16(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys("address16")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("1234569875")
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail16@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase17(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("address17")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("city")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("123")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("12366548789")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail17@")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(9) > td:nth-child(2)").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail17@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase18(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address18")
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("123@!#")
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("3656987458")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail18@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase19(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address19")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys(" 12568")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6478954561")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail19@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("123455")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase20(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Karim")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address20")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("125 35")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("4658974565")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail20@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase21(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address21")
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("123654")
        self.driver.find_element(By.NAME, "telephoneno").click()
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail21@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase22(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Name")
        self.driver.find_element(By.ID, "dob").send_keys("2000-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address22")
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("123654")
        self.driver.find_element(By.NAME, "telephoneno").send_keys(" 6476589842")
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail22@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase23(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address23")
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("123654")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("645 478954")
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail23@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase24(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address24")
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("123456")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("64578945@!#")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail24@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase25(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Karim")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address25")
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td:nth-child(2)").click()
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("123456")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6475689754")
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase26(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address")
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("123456")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6547896587")
        self.driver.find_element(By.NAME, "emailid").send_keys("Guru99")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"

    def test_testCase27(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 1009)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Name")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address27")
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("123456")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("6547896547")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleE mail@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "sub").click()

    def test_testCase28(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1597, 974)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("Karim")
        self.driver.find_element(By.ID, "dob").send_keys("2001-01-01")
        self.driver.find_element(By.NAME, "addr").send_keys("Address28")
        self.driver.find_element(By.NAME, "city").send_keys("City")
        self.driver.find_element(By.NAME, "state").send_keys("State")
        self.driver.find_element(By.NAME, "pinno").send_keys("123654")
        self.driver.find_element(By.NAME, "telephoneno").send_keys("641589756")
        self.driver.find_element(By.NAME, "emailid").send_keys("ExampleEmail28@gmail.com")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "sub").click()
        assert self.driver.switch_to.alert.text == "please fill all fields"