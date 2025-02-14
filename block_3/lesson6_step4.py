import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_guest_should_see_login_link(browser):
    link = 'https://stepik.org/lesson/236895/step/1'
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#ember471").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys('dima.shirikov@mail.ru')
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys('49Dima80Shir12')
    browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
