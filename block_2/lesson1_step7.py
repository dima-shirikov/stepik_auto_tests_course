from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/get_attribute.html')

x = browser.find_element(By.CSS_SELECTOR, '#treasure').get_attribute('valuex')

browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
time.sleep(5)
browser.quit()

