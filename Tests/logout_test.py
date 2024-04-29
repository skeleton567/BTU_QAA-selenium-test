from Actions.shared_actions import SharedActions
from Actions.login_actions import LoginActions

def test_incorrect_pasword():
    assert SharedActions.check_page_is_right() == True
    
    SharedActions.go_to_sign_up()
    
    assert LoginActions.check_login_page() == True
    
    LoginActions.enter_email('guram@gh.ge')
    
    LoginActions.enter_password('1234')
    
    LoginActions.submit()
    
    assert LoginActions.check_logged_in('guram') == True
    
    LoginActions.logout()
    
    assert LoginActions.check_login_page() == True