from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
applications_button_xpath = "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications']"
cell_xpath = "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877']"
devEUI_button_xpath = "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877/devices/08a60f4954ee1820']"
event_button_xpath = "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877/devices/08a60f4954ee1820/events']"

def open_chirpstack():
    driver = webdriver.Safari()

    driver.get("http://localhost:8080")
    time.sleep(2)

    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))   
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-btn-primary")))


    email_input.send_keys(EMAIL) # pyright: ignore[reportArgumentType]
    password_input.send_keys(PASSWORD) # pyright: ignore[reportArgumentType]
    submit_button.click()
    time.sleep(2)

    applications_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, applications_button_xpath)))    
    applications_button.click()
    time.sleep(5)

    cell = driver.find_element(By.XPATH, cell_xpath)
    cell.click()
    time.sleep(5)

    devEUI_button = driver.find_element(By.XPATH, devEUI_button_xpath)
    devEUI_button.click()
    time.sleep(5)

    event_button = driver.find_element(By.XPATH, event_button_xpath)
    event_button.click()
    time.sleep(5)



def main():
    open_chirpstack()
    # Additional logic can be added here if needed

if __name__ == "__main__":
    main()