#DDT ===> Data Driven Testing

import time

import pytest

from PageObjects.Add_Emp_Page import AddEmp
from PageObjects.LoginPage import loginpage
from utilites import XLutils
from utilites.Logger import LogGenrator
from utilites.readproperties import ReadConfig


class Test_Add_Emp_DDT:

    url = ReadConfig.geturl()
    username = ReadConfig.username()
    password = ReadConfig.password()
    log = LogGenrator.logGen()
    path = "C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\testcases\\TestData\\EmpList.xlsx"

    @pytest.mark.sanity
    def test_addEmp_DDT_005(self, setup):

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

        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        self.log.info("Reading Data from Excel File......")
        print("Number of ROWs are ---->", self.rows)

        self.ae = AddEmp(self.site)  # object created for AddEmp
        self.ae.Click_PIM()  # function call for PIM
        self.log.info("Clicking on PIM..")

        self.ae.Click_Add()  # function call for Add
        self.log.info("Clicking on Add button..")
        time.sleep(5)  # Wait for 5 seconds


        status_list = []
        for r in range(2,self.rows+1):
            self.FirstName = XLutils.readData(self.path,'Sheet1',r,2)
            self.MiddleName = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.LastName = XLutils.readData(self.path, 'Sheet1', r, 4)

            self.ae.Add_FirstName(self.FirstName)  # passing argument for FirstName
            self.log.info("Entering first Name.."+self.FirstName)

            self.ae.Add_MiddleName(self.MiddleName)  # passing argument for MiddleName
            self.log.info("Entering Middle Name.."+self.MiddleName)

            self.ae.Add_LastName(self.LastName)  # passing argument for LastName
            self.log.info("Entering Last Name.."+self.LastName)

            #time.sleep(2)  # wait for 2 seconds
            self.ae.Click_Save()  # function call for save
            self.log.info("Clicking On Save..")

            if self.ae.Add_Emp_Status() == True:  # conditional menu element check
                self.ae.Click_Add_Emp()
                time.sleep(2)
                status_list.append("Pass")      #List to check status of task
                XLutils.writeData(self.path,'Sheet1',r,5,"Pass")    #Writing data into file on condition if Passed
                self.site.save_screenshot("C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\ScreenShots\\Add_Emp_Passed.png")
                self.log.info("Taking Screenshots on LogIn Passed..")
                self.log.info("test_addEmp_003 is Passed....")
            else:
                status_list.append("Fail")          #List to check status of task
                XLutils.writeData(self.path, 'Sheet1', r, 5, "Failed")  #Writing data into file on condition if failed
                self.site.save_screenshot("C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\ScreenShots\\Add_Emp_Failed.png")
                self.log.info("Taking Screenshots on LogIn Failed..")

        print(status_list)              #Printing status list


        self.lp.Click_MenuButton()  # function call for Menubutton
        self.log.info("Clicking on Menu Button..")
        time.sleep(2)

        self.lp.Click_Logout()  # function call for Logout
        self.log.info("Clicking on Log Out Button...")

        self.site.close()  # closing the browser page

        if "Fail" not in status_list:
            self.log.info("test_addEmp_005 is Passed....")
            assert True
        else:
            self.log.info("test_addEmp_005 is Failed....")
            assert False

        self.log.info("test_addEmp_003 is Completed Successfully....")
