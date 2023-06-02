import time

from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as EC



class loginpage:
    Text_Username_Xpath = (By.XPATH, "//input[@placeholder='Username']")
    Text_Password_Xpath = (By.XPATH, "//input[@placeholder='Password']")
    Click_on_Login_Xpath = (By.XPATH, "//button[normalize-space()='Login']")
    Click_on_Menu_Xpath = (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    Click_on_Logout_Xpath = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, site):
        self.site = site

    def Enter_Username(self,username):
        self.site.find_element(*loginpage.Text_Username_Xpath).send_keys(username)

    def Enter_Password(self,password):
        self.site.find_element(*loginpage.Text_Password_Xpath).send_keys(password)

    def Click_Login(self):
        self.site.find_element(*loginpage.Click_on_Login_Xpath).click()

    def Click_MenuButton(self):
        self.site.find_element(*loginpage.Click_on_Menu_Xpath).click()

    def Click_Logout(self):
        self.site.find_element(*loginpage.Click_on_Logout_Xpath).click()

    def login_status(self):
        # Exception Handling Block
        try:
            self.site.find_element(*loginpage.Click_on_Menu_Xpath).click()
            return True

        except EC:  # NoSuchElementException Added
            return False





