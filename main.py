from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_chirpstack():
    driver = webdriver.Safari()

    driver.get("http://localhost:8080")
    time.sleep(2)