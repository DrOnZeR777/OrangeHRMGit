from selenium.webdriver.common.by import By


class EmpSearch:
    Text_EmpName_Xpath = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
    Click_Search_Xpath = (By.XPATH, "//button[normalize-space()='Search']")
    Search_Result_CSS = (By.CSS_SELECTOR,"div[class='oxd-table-card'] div:nth-child(3) div:nth-child(1)")

    def __init__(self, site):
        self.site = site

    def Enter_EmpName(self, empname):
        self.site.find_element(*EmpSearch.Text_EmpName_Xpath).send_keys(empname)

    def Click_SerachButton(self):
        self.site.find_element(*EmpSearch.Click_Search_Xpath).click()

    def Serach_Result(self):
        search = self.site.find_elements(*EmpSearch.Search_Result_CSS)
        LEN = len(search)
        if LEN == 0:
            return False
        elif LEN == 1:
            print("self.site.find_element(*EmpSearch.Search_Result_CSS).text")
            return True
