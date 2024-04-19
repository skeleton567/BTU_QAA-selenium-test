from Locators.login_locators import LoginLocators

class LoginActions:
    
    def check_login_page():
        return 'Login to your account' in LoginLocators.login_title().text
    
    def enter_email(email):
        LoginLocators.email_login_input().send_keys(email)
        
    def enter_password(password):
        LoginLocators.password_login_input().send_keys(password)
        
    def submit():
        LoginLocators.login_button().click()
        
    def check_error_message():
        return 'Your email or password is incorrect!' in LoginLocators.error_message()
    
    def check_logged_in(name):
        return f"Logged in as {name}" in LoginLocators.logged_in_text()
    
    def delete_account():
       return LoginLocators.delete_account_button().click()
   
    def check_account_deleted():
        return 'ACCOUNT DELETED!' in LoginLocators.account_deleted_text()
    
    def logout():
        return LoginLocators.logout_button().click()
