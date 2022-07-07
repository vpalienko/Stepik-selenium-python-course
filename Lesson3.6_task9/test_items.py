from selenium.webdriver.common.by import By
# import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_is_displayed(browser):
    browser.get(link)
    # time.sleep(30)
    basket_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert basket_button, "Button 'Add to basket' is absent on the page"
