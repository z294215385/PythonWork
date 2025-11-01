from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Edge()
browser.get('https://play2048.co/')

html_element = browser.find_element(By.TAG_NAME, 'html')

while True:
    html_element.send_keys(Keys.UP)
    html_element.send_keys(Keys.RIGHT)
    html_element.send_keys(Keys.DOWN)
    html_element.send_keys(Keys.LEFT)
