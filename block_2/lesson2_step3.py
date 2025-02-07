from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/selects1.html')

x = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)

select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
select.select_by_value(str(x))

browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

time.sleep(5)
browser.quit()