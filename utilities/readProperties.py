import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\config.ini")

class ReadConfig():
    @staticmethod
    def getURL():
        URL = config.get('Common info', 'URL')
        return URL

    @staticmethod
    def getemail():
        email = config.get('Common info', 'email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('Common info', 'password')
        return password