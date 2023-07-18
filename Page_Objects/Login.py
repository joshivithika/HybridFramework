from selenium import webdriver
class AdminLogin:

    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class = 'button-1 login-button']"
    link_logout_xpath = "//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self, driver):
        self.driver = driver

    def set_email_id(self, email_id):
        self.driver.find_element("id", self.textbox_email_id).clear()
        self.driver.find_element("id", self.textbox_email_id).send_keys(email_id)

    def set_password(self, password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath", self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element("xpath", self.link_logout_xpath).click()




