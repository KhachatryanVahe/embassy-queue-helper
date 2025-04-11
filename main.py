from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Config
url = os.getenv('URL')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

#selectors
LOGIN='login'
USERNAME_FIELD_NAME = 'email'
PASSWORD_FIELD_NAME = 'pwd'
SUBMIT_BUTTON_SELECTOR = 'login_button'

# Setup WebDriver
service = Service('/usr/bin/chromedriver')  # update path to your chromedriver
options = Options()
options.debugger_address = "localhost:9222"

driver = webdriver.Chrome(service=service, options=options)

# Open the page
driver.get(url)


# driver.find_element(By.XPATH, "//*[text()='Accept All']").click()

# # Click the login link
# try:
#     login_link = driver.find_element(By.CLASS_NAME, LOGIN)
#     print(f'✅ Found login link: "{LOGIN}"')
#     login_link.click()
# except Exception as e:
#     print(f'❌ Could not find or click login link: {e}')

# time.sleep(2)

# # Fill in username and password
# try:
#     driver.find_element(By.NAME, USERNAME_FIELD_NAME).send_keys(username)
#     # password_filed = driver.find_element(By.NAME, PASSWORD_FIELD_NAME).send_keys(password)
#     password_filed = driver.find_element(By.NAME, PASSWORD_FIELD_NAME)
#     driver.execute_script("arguments[0].scrollIntoView(true);", password_filed)
#     password_filed.send_keys(password)
#     print('✅ Filled in username and password')
# except Exception as e:
#     print(f'❌ Failed to find input fields: {e}')
#     driver.quit()
#     exit()

# # Click submit/login button
# try:
#     login_button = driver.find_element(By.ID, "login_button")
#     # driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
#     # time.sleep(0.5)  # let it scroll
#     login_button.click()
#     print('✅ Clicked login/submit button')
# except Exception as e:
#     print(f'❌ Failed to submit login form: {e}')

# time.sleep(30)
