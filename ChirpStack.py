from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

class ChirpStack:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file

        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("PASSWORD")
        self.applications_button_xpath = "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications']"
        self.cell_xpath = "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877']"
        self.devEUI_button_xpath = "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877/devices/08a60f4954ee1820']"
        self.event_button_xpath = "//a[@href='#/tenants/cde402c9-1549-4de5-b37c-b32755f5a70c/applications/e38b1e6a-599e-4a2d-9de3-695ea5b57877/devices/08a60f4954ee1820/events']"
        self.driver = None