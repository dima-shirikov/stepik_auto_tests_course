import time
from selenium.webdriver.common.by import By


def test_different_languages(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    button = browser.find_elements(By.XPATH, '//button[contains(@class, "btn-add-to-basket")]')

    assert button, 'Кнопка добавления товара в корзину - отсутствует'
