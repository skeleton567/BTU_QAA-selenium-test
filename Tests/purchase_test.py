
from Locators.purchase_locators import PurchaseLocators
from Actions.purchase_actions import PurchaseActions


def test_purchase():
    PurchaseActions.go_to_item()
    PurchaseActions.click_add_to_card_button()
    
    assert PurchaseLocators.error_message() == "This is a required field."