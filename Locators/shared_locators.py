from selenium.webdriver.common.by import By
from conftest import DriverSetUp

driver = DriverSetUp.driver

class SharedLocators:
    
    def page_title():
        return driver.title

    def sign_in_url():
        return driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
    
