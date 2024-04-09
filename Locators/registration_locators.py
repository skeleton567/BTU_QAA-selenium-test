from selenium.webdriver.common.by import By
from conftest import DriverSetUp

driver = DriverSetUp.driver

class RegistrationLocators:
    first_name_input = driver.find_element(By.CSS_SELECTOR, "#firstname")
    last_name_input = driver.find_element(By.CSS_SELECTOR, "#lastname")
    email_input = driver.find_element(By.CSS_SELECTOR, "#email_address")
    password_input = driver.find_element(By.CSS_SELECTOR, "#password")
    password_confirmation_input = driver.find_element(By.CSS_SELECTOR, "#password-confirmation")
    submit_button = driver.find_element(By.XPATH, "//*[@id='form-validate']/div/div[1]/button")
    
    def success_message():
        return driver.find_element(By.XPATH, "//*[@id='maincontent']/div[1]/div[2]/div/div/div").text


