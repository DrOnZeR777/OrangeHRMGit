import time

import pytest

from PageObjects.Add_Emp_Page import AddEmp
from PageObjects.LoginPage import loginpage
from utilites.Logger import LogGenrator
from utilites.readproperties import ReadConfig


class Test_Add_Emp:

    url = ReadConfig.geturl()
    username = ReadConfig.username()
    password = ReadConfig.password()
    log = LogGenrator.logGen()

    @pytest.mark.sanity
    def test_addEmp_003(self, setup):

        self.log.info("test_addEmp_003 is started....")
        self.site = setup  # Fetching site from web browser
        self.log.info("Fetching site from web browser....")
        self.site.get(self.url)         #Calling Class variable
        self.log.info("Calling class variable....")

        self.lp = loginpage(self.site)  # object created for loginpage

        self.lp.Enter_Username(self.username)  # passing argument for username
        self.log.info("Entering USERNAME---->"+self.username)

        self.lp.Enter_Password(self.password)  # passing argument for password
        self.log.info("Entering PASSWORD---->"+self.password)

        self.lp.Click_Login()  # Click on login
        self.log.info("Clicking on Login..")

        self.ae = AddEmp(self.site)  # object created for AddEmp
        self.ae.Click_PIM()  # function call for PIM
        self.log.info("Clicking on PIM..")

        self.ae.Click_Add()  # function call for Add
        self.log.info("Clicking on Add button..")
        time.sleep(5)  # Wait for 5 seconds

        self.ae.Add_FirstName("TestBot1")  # passing argument for FirstName
        self.log.info("Entering first Name..")

        self.ae.Add_MiddleName("TestBot1")  # passing argument for MiddleName
        self.log.info("Entering Middle Name..")

        self.ae.Add_LastName("TestBot1")  # passing argument for LastName
        self.log.info("Entering Last Name..")

        time.sleep(2)  # wait for 2 seconds
        self.ae.Click_Save()  # function call for save
        self.log.info("Clicking On Save..")

        if self.ae.Add_Emp_Status():  # conditional menu element check
            time.sleep(5)
            self.site.save_screenshot("C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\ScreenShots\\Add_Emp_Passed.png")
            self.log.info("Taking Screenshots on LogIn Passed..")

            self.lp.Click_MenuButton()  # function call for Menubutton
            self.log.info("Clicking on Menu Button..")

            self.lp.Click_Logout()  # function call for Logout
            self.log.info("Clicking on Log Out Button...")
            assert True
            self.log.info("test_addEmp_003 is Passed....")
        else:
            self.site.save_screenshot("C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\ScreenShots\\Add_Emp_Failed.png")
            self.log.info("Taking Screenshots on LogIn Failed..")
            self.log.info("test_addEmp_003 is Failed....")
            assert False


        self.site.close()  # closing the browser page
        self.log.info("test_addEmp_003 is Completed Successfully....")
