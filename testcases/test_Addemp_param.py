# Framework Design
# Sesion Automation
# Opeining the OrangeHRM Site:: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
import time
from selenium import webdriver
from selenium.common import NoSuchElementException as EC
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import loginpage
from utilites.readproperties import ReadConfig
from utilites.Logger import LogGenrator


class Test_login_Params:
    url = ReadConfig.geturl()
    username = ReadConfig.username()
    password = ReadConfig.password()
    log = LogGenrator.logGen()


    def test_login_params_004(self, setup, getDataforLogin):

        self.log.info("test_login_params_004 is Started....")
        self.site = setup
        self.log.info("Opening Browser.....")
        self.site.get(self.url)
        self.log.info("Go to this url--->" + self.url)
        # self.site = webdriver.Chrome()  # Object created for browser

        # self.site.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Fetching site
        time.sleep(5)  # sleep for 2 seconds

        # object creted and calling the login page
        self.lp = loginpage(self.site)
        self.lp.Enter_Username(getDataforLogin[0])
        self.log.info("Entering the USERNAME---->" + getDataforLogin[0])

        # object creted and calling the login page
        self.lp.Enter_Password(getDataforLogin[1])
        self.log.info("Entering the PASSWORD---->" + getDataforLogin[1])

        # object creted and calling the login page
        self.lp.Click_Login()  ## Calling  login button method
        self.log.info("Clicked on Log In...")
        time.sleep(5)

        # Exception Handling Blcok :::
        time.sleep(5)
        if self.lp.login_status() == True:
            if getDataforLogin[2] == "Pass":

                self.site.save_screenshot(
                "C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\ScreenShots\\Test_Login_pass_002.png")
                self.lp.Click_MenuButton()
                self.log.info("Clicked on Menu Button....")
                time.sleep(3)
                self.lp.Click_Logout()
                self.log.info("Clicked on Log Out Button....")
                assert True
                self.log.info("test_login_params_004 is passed")
            else:
                self.log.info("test_login_param failed")
                self.site.save_screenshot(
                "C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\ScreenShots\\Test_Login_failed_002.png")
                assert False
        else:
            if getDataforLogin[2] == "Fail":
                assert True
            else:
                self.log.info("test_login_params_004 failed")
                self.site.save_screenshot(
                    "C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\ScreenShots\\Test_Login_failed_002.png")
                assert False

        self.site.close()
        self.log.info("test_login_params_004 is completed.....")

