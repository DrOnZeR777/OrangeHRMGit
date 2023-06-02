import time

import pytest

from PageObjects.Add_Emp_Page import AddEmp
from PageObjects.LoginPage import loginpage
from PageObjects.empserach import EmpSearch
from utilites.Logger import LogGenrator
from utilites.readproperties import ReadConfig


class Test_Search_Emp:
    url = ReadConfig.geturl()
    username = ReadConfig.username()
    password = ReadConfig.password()
    log = LogGenrator.logGen()

    @pytest.mark.sanity
    def test_SerachEmp_005(self, setup):

        self.log.info("test_SerachEmp_005 is started....")
        self.site = setup  # Fetching site from web browser
        self.log.info("Fetching site from web browser....")
        self.site.get(self.url)  # Calling Class variable
        self.log.info("Calling class variable....")

        self.lp = loginpage(self.site)  # object created for loginpage

        self.lp.Enter_Username(self.username)  # passing argument for username
        self.log.info("Entering USERNAME---->" + self.username)

        self.lp.Enter_Password(self.password)  # passing argument for password
        self.log.info("Entering PASSWORD---->" + self.password)

        self.lp.Click_Login()  # Click on login
        self.log.info("Clicking on Login..")

        self.ae = AddEmp(self.site)  # object created for AddEmp
        self.ae.Click_PIM()  # function call for PIM
        self.log.info("Clicking on PIM..")

        self.es = EmpSearch(self.site)  # Object created for empserach page object

        time.sleep(5)
        self.es.Enter_EmpName("Paul")
        self.log.info("Entering employee Name...")

        time.sleep(2)
        self.es.Click_SerachButton()
        self.log.info("Clickin on Search Button...")

        time.sleep(5)
        print(self.es.Serach_Result())
        if self.es.Serach_Result() == True:

            self.log.info("Serach Found.......")
            self.lp.Click_MenuButton()
            self.log.info("Clicked on Menu Button....")
            time.sleep(3)
            self.lp.Click_Logout()
            self.log.info("Clicked on Log Out Button....")
            assert True
            self.log.info("test_SerachEmp_005 is passed....")
        else:
            self.log.info("Serach not Found.......")
            self.log.info("test_SerachEmp_005 is falied....")
            assert False
