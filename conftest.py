from selenium import webdriver


class DriverSetUp:
    driver = webdriver.Chrome()
    driver.get("http://automationexercise.com")