# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# Comment this out
import secret_config as config
# Uncomment this out and fill with your login information
#import config

# Config
USERNAME = config.USER_NAME
PASSWORD = config.USER_PASS
GAME_URL = "https://farmrpg.com/"
LOGIN_URL = "https://farmrpg.com/#!/login.php"
LOGOUT_URL = "logout.php"
GAME_TITLE = "Farm RPG"

# Selenium Setup
driver = webdriver.Chrome("C:/browser_drivers/chromedriver.exe")
driver.set_window_size(800, 800)
driver.get(GAME_URL)
sleep(.5)

# Quit Web Driver
def tearDown():
    driver.quit()

# Get Tab Title
def getTitle():
    return driver.title

# Check if game is already logged in
def checkLogin():
    try:
        driver.find_element(by=By.XPATH, value='//a[@href="'+LOGOUT_URL+'"]')
        print("User is logged in!")
        return True
    except:
        print("User is NOT logged in!")
        return False

# Log the user in
def login():
    if checkLogin():
        pass
    else:
        driver.get(LOGIN_URL)
        sleep(.5)
        driver.refresh()
        sleep(.5)

        assert getTitle() == GAME_TITLE

        driver.find_element_by_name("username").send_keys(USERNAME)
        driver.find_element_by_name("password").send_keys(PASSWORD)
        sleep(.5)

        driver.find_element_by_id("login_sub").click()
        sleep(.5)
        if checkLogin() == False:
            print("!!! Failed to log in !!!")
            tearDown()




login()
# End
sleep(5)
tearDown()