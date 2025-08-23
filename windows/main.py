from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
import time
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def open_chirpstack():
    # Configurações do Chrome (opcional: pode abrir maximizado, sem logs, etc.)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Inicializa o Chrome com o WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("http://localhost:8080")
    time.sleep(2)

    # Login
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.CSS_SELECTOR, ".ant-btn-primary")

    email_input.send_keys("admin")
    password_input.send_keys("admin")
    submit_button.click()
    time.sleep(2)

    # Ir para Applications
    applications_button = driver.find_element(By.XPATH, "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications']")
    applications_button.click()
    time.sleep(5)

    # Selecionar aplicação
    cell = driver.find_element(By.XPATH, "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877']")
    cell.click()
    time.sleep(5)

    # Selecionar Device específico
    devEUI_button = driver.find_element(By.XPATH, "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877/devices/08a60f4954ee1820']")
    devEUI_button.click()
    time.sleep(5)

    # Selecionar Events
    event_button = driver.find_element(By.XPATH, "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877/devices/08a60f4954ee1820/events']")
    event_button.click()
    time.sleep(5)

    # Mantém o navegador aberto (ou fecha se preferir)
    # driver.quit()

def main():
    open_chirpstack()

if __name__ == "__main__":
    main()