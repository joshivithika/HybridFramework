import pytest
from selenium import webdriver
from Page_Objects.Login import AdminLogin
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class  Test_02_DDT_LoginPage:
    URL = ReadConfig.getURL()
    path = ".//Test_data/LoginData.xlsx"
    logger = LogGen.log()

    def test_title_home_page(self, setup):

        self.logger.info("*************Test_02_DDT_Login**************")
        self.logger.info("************* Verifying Home Page Title **************")
        self.driver = setup
        self.driver.get(self.URL)
        page_title = self.driver.title
        if page_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Home Page Title Test is passed **************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_title_home_page.png")
            self.driver.close()
            self.logger.info("************* Home Page Title Test is failed **************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************* Verifying DDT Login Test **************")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.lp = AdminLogin(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in the excel are: ", self.rows)

        lst_status = []    # Empty list variable

        for r in range(2,self.rows+1):
            self.Email = XLUtils.readData(self.path,'Sheet1',r,1)
            self.Password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.Expected = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.set_email_id(self.Email)
            self.lp.set_password(self.Password)
            self.lp.clickLogin()

            time.sleep(5)

            page_title = self.driver.title

            Expected_title = "Dashboard / nopCommerce administration"

            if page_title == Expected_title:
                if self.Expected == 'Pass':
                    self.logger.info("********************Passed*******************")
                    time.sleep(5)
                    self.lp.clickLogout()
                    lst_status.append('Pass')
                elif self.Expected == 'Fail':
                     self.logger.info("*******************Failed*******************")
                     lst_status.append('Fail')
            elif  page_title != Expected_title:
                if self.Expected == 'Fail':
                     self.logger.info("********************Passed*********************")
                     lst_status.append('Pass')
                elif self.Expected == 'Pass':
                    self.logger.info("*********************Failed********************")
                    self.lp.clickLogout()
                    lst_status.append('Fail')

        if 'Fail' not in lst_status:
            self.logger.info("*************DDT Test Case is Passed **************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*************DDT Test Case is Failed **************")
            self.driver.close()
            assert False

        self.logger.info("************* End of DDT Test Case **************")















