from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    start_button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    start_button.click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    x_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(x_value)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(result)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
