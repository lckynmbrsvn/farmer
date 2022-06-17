# Imports
from selenium import webdriver
import time
import config

# Config
USERNAME = config.USER_NAME
PASSWORD = config.USER_PASS
URL = 'https://farmrpg.com/#!/login.php'

# Selenium Config
driver = webdriver.Chrome('C:/browser_drivers/chromedriver.exe')

# Login
driver.set_window_size(800, 800)
time.sleep(1)

driver.get(URL)
time.sleep(1)

driver.find_element_by_name('username').send_keys(USERNAME)
driver.find_element_by_name('password').send_keys(PASSWORD)
time.sleep(1)

driver.find_element_by_id('login_sub').click()



# For testing
time.sleep(5)
driver.close()