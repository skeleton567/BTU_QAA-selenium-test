from selenium.webdriver.common.by import By
from conftest import DriverSetUp

driver = DriverSetUp.driver

class LoginLocators:

    def email_login_input():
        return driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[2]")
        
    def password_login_input():
        return driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/input[3]")
        
    def login_title():  
        return driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/h2")
        
    def login_button(): 
        return driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/button")
    
    def error_message():
        return driver.find_element(By.XPATH, "//*[@id='form']/div/div/div[1]/div/form/p").text
    
    def logged_in_text():
        return driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[10]").text
    
    def delete_account_button():
        return driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")  
    
    def account_deleted_text():
       return driver.find_element(By.XPATH, "//*[@id='form']/div/div/div/h2").text
   
    def logout_button():
       return driver.find_element(By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")
        


