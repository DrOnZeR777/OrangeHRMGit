# Framework Design
# Sesion Automation
# Opeining the OrangeHRM Site:: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
import time
from selenium import webdriver
from selenium.common import NoSuchElementException as EC
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import loginpage
from utilites import XLutils
from utilites.readproperties import ReadConfig
from utilites.Logger import LogGenrator


class Test_login_DDT:
    url = ReadConfig.geturl()
    # username = ReadConfig.username()
    # password = ReadConfig.password()
    log = LogGenrator.logGen()
    path = "C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\testcases\\TestData\\LoginData.xlsx"

    def test_pagetitle_001(self, setup):
        self.log.info("Test page title case started...")
        self.site = setup
        self.log.info("Opening Browser.....")
        self.site.get(self.url)
        self.log.info("Go to this url--->" + self.url)

        time.sleep(2)  # sleep for 2 seconds
        if self.site.title == "OrangeHRM":
            assert True
            self.log.info("test_page_title_001 is passed")
            self.log.info("Page title is--->" + self.site.title)
        else:
            assert False
            self.log.info("test_page_title_001 is failed")

        self.site.close()
        self.log.info("test_page_title_001 is Completed...")
        self.log.debug("debug")
        self.log.info("info")
        self.log.warning("warning")
        self.log.error("error")
        self.log.critical("critical")

    def test_login_DDT_006(self, setup):

        self.log.info("test_login_DDT_006 is Started....")
        self.site = setup
        self.log.info("Opening Browser.....")
        self.site.get(self.url)
        self.log.info("Go to this url--->" + self.url)
        # self.site = webdriver.Chrome()  # Object created for browser

        # self.site.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Fetching site
        time.sleep(5)  # sleep for 2 seconds

        # Checking count data from login data file
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        self.log.info("Reading Data from Excel File......")
        print("Number of ROWs are ---->", self.rows)
        login_status = []
        for r in range(2, self.rows + 1):

            self.username = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 3)

            # object creted and calling the login page
            self.lp = loginpage(self.site)
            self.lp.Enter_Username(self.username)
            self.log.info("Entering the USERNAME---->" + self.username)

            # object creted and calling the login page
            self.lp.Enter_Password(self.password)
            self.log.info("Entering the PASSWORD---->" + self.password)

            # object creted and calling the login page
            self.lp.Click_Login()  ## Calling  login button method
            self.log.info("Clicked on Log In...")
            time.sleep(5)

            # Exception Handling Blcok :::
            time.sleep(5)
            if self.lp.login_status() == True:
                self.site.save_screenshot(
                    "C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\ScreenShots\\" + self.username + self.password + "Test_Login_pass_002.png")
                self.lp.Click_MenuButton()
                self.log.info("Clicked on Menu Button....")
                time.sleep(3)
                self.lp.Click_Logout()
                self.log.info("Clicked on Log Out Button....")
                login_status.append("Pass")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Pass")
                self.log.info("test_login_DDT_006 is passed")
            else:
                self.site.save_screenshot(
                    "C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\ScreenShots\\" + self.username + self.password + "Test_Login_Failed_006.png")
                login_status.append("Failed")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Failed")
            self.log.info("test_login_DDT_006 is failed")

        if "Fail" not in login_status:
            self.log.info("test_login_DDT_006 is Passed....")
            assert True
        else:
            self.log.info("test_login_DDT_006 is Failed....")
            assert False

        self.log.info("test_login_DDT_006 is Completed Successfully....")
        self.site.close()

        self.log.info("test_login_DDT_006 is completed.....")

    def test_addemp_003(self, setup):

        self.site = setup
        self.site.get(self.url)
        # site = webdriver.Chrome()  # Object created for browser

        # site.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Fetching site
        self.site.maximize_window()
        self.site.implicitly_wait(5)
        time.sleep(2)  # sleep for 2 seconds

        # Entering the username
        username = self.username
        self.site.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)

        # Entering the Password
        passwords = self.password
        self.site.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(passwords)

        # Click on login button
        self.site.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)

        # Click on PIM...
        self.site.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']["
                                         "normalize-space()='PIM']").click()
        time.sleep(2)

        # click on add button
        self.site.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        time.sleep(2)

        # Click on first name
        self.site.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("TestBot1")
        time.sleep(1)

        # Click on  Middle name
        self.site.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("TestBot1")
        time.sleep(1)

        # Click on first name
        self.site.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("TestBot1")
        time.sleep(1)

        # Click on Save button
        self.site.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
        time.sleep(5)
        # Exception Handling Blcok :::
        try:

            # site.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
            print("Login passed........")

            # Clicking on menu for employee list availability option
            # site.find_element(By.XPATH, "//a[normalize-space()='Employee List']").click()
            # time.sleep(4)

            # Clicking on personal Details
            self.site.find_element(By.XPATH, "//a[normalize-space()='Personal Details']").click()
            print("Login passed........")
            time.sleep(4)

            # Clicking on menu for logout option
            self.site.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
            time.sleep(2)

            # Clicking on logout option
            self.site.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            time.sleep(5)
            addemp = True
            # assert True
        except EC:  # NoSuchElementException Added
            print("TestCase Addemp003 Failed........")
            print("TestCase Addemp003 is completed......")
            addemp = False
            # assert False

        if addemp == True:
            assert True
        else:
            assert False
        self.site.close()
#
# # site.close()  # site object closed
