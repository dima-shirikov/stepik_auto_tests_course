from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

with open("file.txt", "w") as file:
  content = file.write("automationbypython")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Dmitriy')
browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Shirikov')
browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('Shirikov@mail.ya')
browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)
browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

time.sleep(5)
browser.quit()