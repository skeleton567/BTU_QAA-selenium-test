from selenium import webdriver


class DriverSetUp:
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")