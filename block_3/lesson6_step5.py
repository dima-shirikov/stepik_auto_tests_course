import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_login_link(browser, link):
    # link = 'https://stepik.org/lesson/236905/step/1'
    answer = (str(math.log(int(time.time()))))
    browser.get(link)
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ember471"))
    )
    browser.find_element(By.XPATH, ".navbar__divider+a").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys('*****')
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys('*****')
    browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
    # time.sleep(5)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']"))
    )
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']").send_keys(answer)

    submit_button = browser.find_element(By.XPATH, "//button[text()='Отправить']")
    time.sleep(2)
    submit_button.click()

    time.sleep(2)
    opt_hint = browser.find_element_by_class_name("smart-hints__hint")
    opt_hint_text = opt_hint.text
    assert opt_hint_text == "Correct!", opt_hint_text
