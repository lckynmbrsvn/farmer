# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
# Comment the line below out
import secret_config as config
# Uncomment the line below and fill with your login information
#import config

# Config
USERNAME = config.USER_NAME
PASSWORD = config.USER_PASS
FARM_ID = config.FARM_ID
GAME_URL = "https://farmrpg.com/"
LOGIN_URL = GAME_URL + "#!/login.php"
LOGOUT_URL = "logout.php"
MENU_URL = GAME_URL + "#!/index.php"
FARM_URL = GAME_URL + "index.php#!/" + FARM_ID
GAME_TITLE = "Farm RPG"

# Selenium Setup
driver = webdriver.Chrome("C:/chromedriver.exe")
driver.set_window_size(800, 800)
driver.set_window_position(100, 100)
driver.get(GAME_URL)
sleep(3)

# Quit Web Driver
def tearDown():
    driver.quit()

# Get Tab Title
def getTitle():
    return driver.title

# Check if game is already logged in
def checkLogin():
    try:
        logoutBTN = '//a[@href="' + LOGOUT_URL + '"]'
        driver.find_element(By.XPATH, logoutBTN)
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

        driver.find_element(By.NAME, "username").send_keys(USERNAME)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        sleep(.5)

        driver.find_element(By.ID, "login_sub").click()
        sleep(1)
        if checkLogin() == False: print("!!! Failed to log in !!!")

# Go to user's home menu
def goToMenu():
    try:
        driver.get(MENU_URL)
        print("Going to Home Menu...")
        sleep(1)
    except:
        print("!!! Failed to go to Main Menu !!!")
        return False

# Go to user's farm
def goToFarm():
    try:
        driver.get(FARM_URL)
        driver.refresh()
        print("Going to Farm...")
        sleep(1)
    except:
        print("!!! Failed to go to Farm !!!")
        return False

# Harvest all user's crops
def harvestCrops():
    #if getTitle() != FARM_URL: return False
    print("Harvesting All Available Crops...")
    try:
        driver.find_element(By.CLASS_NAME, "harvestallbtn").click()
        print("... ... ... ... ... Success!")
        sleep(2)
        return True
    except:
        print("!!! Failed to Harvest Crops !!!")
        return False

# Plant all 
def plantCrops():
    #if getTitle() != FARM_URL: return False
    print("Planting All Available Crops...")
    try:
        driver.find_element(By.CLASS_NAME, "plantallbtn").click()
        sleep(.5)
        elements = driver.find_elements(By.TAG_NAME, 'div')

        for e in elements:
            if e.text == "Yes": e.click()
        
        print("... ... ... ... ... Success!")
        sleep(2)
        return True
    except:
        print("!!! Failed to Plant Crops !!!")
        return False




### TEST ###
login()
goToFarm()
harvestCrops()
plantCrops()
goToMenu()

### End ###
sleep(5)
tearDown()