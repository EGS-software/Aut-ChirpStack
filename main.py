from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_chirpstack():
    driver = webdriver.Safari()

    driver.get("http://localhost:8080")
    time.sleep(2)

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary")


    email_input.send_keys("admin")
    password_input.send_keys("admin")
    submit_button.click()
    time.sleep(2)

    applications_button = driver.find_element(By.XPATH, "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications']")    
    applications_button.click()
    time.sleep(5)

    cell = driver.find_element(By.XPATH, "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877']")
    cell.click()
    time.sleep(5)

    devEUI_button = driver.find_element(By.XPATH, "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877/devices/08a60f4954ee1820']")



def main():
    open_chirpstack()
    # Additional logic can be added here if needed

if __name__ == "__main__":
    main()