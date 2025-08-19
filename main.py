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




def main():
    open_chirpstack()
    # Additional logic can be added here if needed

if __name__ == "__main__":
    main()