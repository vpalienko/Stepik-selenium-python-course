from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    valuex = browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")
    result = calc(valuex)

    input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_field.send_keys(result)
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()
    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robot_radiobutton.click()
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
