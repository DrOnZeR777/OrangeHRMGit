# Framework Design
# Sesion Automation
# Opeining the OrangeHRM Site:: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_login:

    @pytest.mark.sanity
    def test_login_001(self):

        site = webdriver.Chrome()  # Object created for browser

        site.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Fetching site
        time.sleep(5)  # sleep for 2 seconds

        # Entering the username
        username = "Admin"
        site.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)

        # Entering the Password
        passwords = "admin123"
        site.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(passwords)

        # Click on login button
        site.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(5)

        # Exception Handling Blcok :::
        try:
            site.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
            print("Login passed........")
            # Clickin on menu for logout option
            site.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
            # Clicking on logout option
            site.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            time.sleep(5)
            assert True
        except:
            print("Login failed........")
            assert False

        site.close()  # site object closed
