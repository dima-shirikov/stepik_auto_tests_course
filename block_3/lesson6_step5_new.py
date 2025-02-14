from selenium import webdriver
import pytest
import time
import math
from selenium.webdriver.common.by import By

final = ''


@pytest.fixture(scope="session")
def browser():
    br = webdriver.Chrome()
    yield br
    br.quit()
    print(final)  # напечатать ответ про Сов в конце всей сессии


@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_find_hidden_text(browser, lesson):
    global final
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".navbar__divider+a").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys('dima.shirikov@mail.ru')
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys('49Dima80Shir12')
    browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector('textarea').send_keys(str(answer))
    browser.find_element_by_css_selector('.submit-submission ').click()
    check_text = browser.find_element_by_css_selector('.smart-hints__hint').text
    try:
        assert 'Correct!' == check_text
    except AssertionError:
        final += check_text  # собираем ответ про Сов с каждой ошибкой