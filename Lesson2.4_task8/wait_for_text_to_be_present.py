from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    expected_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_button = browser.find_element(By.CSS_SELECTOR, "#book")
    book_button.click()

    x_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(x_value)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(result)
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
