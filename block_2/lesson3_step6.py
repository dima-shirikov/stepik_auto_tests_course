from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/redirect_accept.html')

browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))

browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

time.sleep(5)
browser.quit()