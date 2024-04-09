from Actions.registration_actions import RegistrationActions
from Locators.registration_locators import RegistrationLocators
import time

registration_actions = RegistrationActions()


def test_registration():
    registration_actions.set_registration_fields()
    registration_actions.click_sumbit_button()
    
    assert RegistrationLocators.success_message() == "Thank you for registering with Main Website Store."
