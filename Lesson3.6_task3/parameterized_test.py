import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

links = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']

alien_message = []


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
    print("\nAnswer:")
    print("".join(alien_message))


@pytest.mark.parametrize('link', links)
def test_links_for_alien_messages(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    result_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    assert result_text == "Correct!", (f"Aliens left a message: {result_text}", alien_message.append(result_text))[0]
