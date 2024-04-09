from Locators.registration_locators import RegistrationLocators

RegistrationLocators()

class RegistrationActions:
    def click_sumbit_button(self):
        RegistrationLocators.submit_button.click()
        
    def set_field(locator, value):
        locator.send_keys(value)

    def set_registration_fields(self):
        RegistrationActions.set_field( RegistrationLocators.first_name_input, "John")
        RegistrationActions.set_field( RegistrationLocators.last_name_input, "Doe")
        RegistrationActions.set_field( RegistrationLocators.email_input, "john.doe233@example.com")
        RegistrationActions.set_field( RegistrationLocators.password_input, "Password123@")
        RegistrationActions.set_field( RegistrationLocators.password_confirmation_input, "Password123@")