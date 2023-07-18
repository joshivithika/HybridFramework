import pytest
from selenium import webdriver
from Page_Objects.Login import AdminLogin
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class  Test_01_LoginPage:
    URL = ReadConfig.getURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()

    logger = LogGen.log()

    @pytest.mark.sanity
    def test_title_home_page(self, setup):

        self.logger.info("*************Test_001_Login**************")
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
        self.logger.info("************* Verifying Login Test **************")
        self.driver = setup
        self.driver.get(self.URL)
        self.lp = AdminLogin(self.driver)
        self.lp.set_email_id(self.email)
        self.lp.set_password(self.password)
        self.lp.clickLogin()
        page_title = self.driver.title
        if page_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************* Login Test is passed **************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info("************* Login Test is failed **************")
            assert False



