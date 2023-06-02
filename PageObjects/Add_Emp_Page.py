import time

import self as self
from selenium.webdriver.common.by import By


# Class Created for AddEmp
class AddEmp:
    # Object created for each element event
    Click_PIM_XPATH = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name']["
                                 "normalize-space()='PIM']")
    Click_Add_XPATH = (By.XPATH, "//button[normalize-space()='Add']")
    Text_FirstName_Xpath = (By.XPATH, "//input[@placeholder='First Name']")
    Text_MiddleName_Xpath = (By.XPATH, "//input[@placeholder='Middle Name']")
    Text_LastName_Xpath = (By.XPATH, "//input[@placeholder='Last Name']")
    Click_Save_Xpath = (By.XPATH, "//button[normalize-space()='Save']")
    Personal_Details_Tab_Xpath = (By.XPATH, "//a[normalize-space()='Personal Details']")
    Add_Emp_Xpath = (By.XPATH,"//a[normalize-space()='Add Employee']")

    # Default Constructor
    def __init__(self, site):
        self.site = site

    # Method for Click On PIM
    def Click_PIM(self):
        self.site.find_element(*AddEmp.Click_PIM_XPATH).click()

    # Method for Adding
    def Click_Add(self):
        self.site.find_element(*AddEmp.Click_Add_XPATH).click()

    # Method For First Name
    def Add_FirstName(self, firstname):
        time.sleep(2)
        self.site.find_element(*AddEmp.Text_FirstName_Xpath).send_keys(firstname)

    # Method For Middle Name
    def Add_MiddleName(self, middlename):
        time.sleep(2)
        self.site.find_element(*AddEmp.Text_MiddleName_Xpath).send_keys(middlename)

    # Method For Last Name
    def Add_LastName(self, lastname):
        time.sleep(2)
        self.site.find_element(*AddEmp.Text_LastName_Xpath).send_keys(lastname)

    # Method for save
    def Click_Save(self):
        self.site.find_element(*AddEmp.Click_Save_Xpath).click()


    #If agin wants to add Employtee then
    def Click_Add_Emp(self):
        self.site.find_element(*AddEmp.Add_Emp_Xpath).click()


    # Exception Handling with page element validation
    def Add_Emp_Status(self):
        self.site.implicitly_wait(5)
        try:
            self.site.find_element(*AddEmp.Personal_Details_Tab_Xpath).click()
            return True

        except:
            return False
