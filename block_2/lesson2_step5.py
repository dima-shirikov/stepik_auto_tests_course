from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) #Проскролит страницу чтобы элемент стал видимым
button.click()

# browser.execute_script("window.scrollBy(0, 100);") #Проскроллит страницу на 100 пикселей вниз