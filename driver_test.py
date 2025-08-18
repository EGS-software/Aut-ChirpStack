from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
driver.get("https://www.google.com")

time.sleep(5)
print(driver.title)

driver.quit()