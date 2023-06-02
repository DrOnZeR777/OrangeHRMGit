import configparser

configuration = configparser.RawConfigParser()

configuration.read("C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\Configurations\\config.ini")



class ReadConfig():

    @staticmethod
    def geturl():
        url = configuration.get("common info", "url")
        return url

    @staticmethod
    def username():
        username = configuration.get("common info", "username")
        return username

    @staticmethod
    def password():
        password = configuration.get("common info", "password")
        return password
