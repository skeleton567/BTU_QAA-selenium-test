from selenium.webdriver.common.by import By
from conftest import DriverSetUp

driver = DriverSetUp.driver

class PurchaseLocators:
    men_link = driver.find_element(By.CSS_SELECTOR, "#ui-id-5")
    
    def pants_link():
        return driver.find_element(By.XPATH, "//*[@id='maincontent']/div[4]/div[2]/div[2]/div/ul[2]/li[1]/a")
    
    def pants_items_link():
     return driver.find_element(By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[4]/ol/li[1]/div/a")
    
    def add_to_card_button():
     return driver.find_element(By.CSS_SELECTOR, "#product-addtocart-button")

    def error_message():
        return driver.find_element(By.CSS_SELECTOR, "#super_attribute\[143\]-error").text