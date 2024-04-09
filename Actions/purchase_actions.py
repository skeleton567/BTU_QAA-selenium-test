from Locators.purchase_locators import PurchaseLocators

PurchaseLocators()

class PurchaseActions:
    def click_add_to_card_button():
        PurchaseLocators.add_to_card_button().click()
        
    def go_to_item():
        PurchaseLocators.men_link.click()
        PurchaseLocators.pants_link().click()
        PurchaseLocators.pants_items_link().click()