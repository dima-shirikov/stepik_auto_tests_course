from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/execute_script.html')

x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)

browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", check)
check.click()
browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

time.sleep(5)
browser.quit()