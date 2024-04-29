from Locators.shared_locators import SharedLocators


class SharedActions:
    def check_page_is_right():
        return 'Automation Exercise' == SharedLocators.page_title()
        
    def go_to_sign_up():
        SharedLocators.sign_in_url().click()