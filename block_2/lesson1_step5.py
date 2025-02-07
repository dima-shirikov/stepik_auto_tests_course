from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/math.html')

x = browser.find_element(By.CSS_SELECTOR, '#input_value').text

browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()

browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
browser.quit()

