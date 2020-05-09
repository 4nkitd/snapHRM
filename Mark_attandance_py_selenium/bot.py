from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#install selenium "pip install selenium"
#install browser driver https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.138/

snap_email = 'example@webinfexampleomart.com' #email goes here
snap_pass = 'example@19!' #password goes here
url = "https://example.snaphrm.com/login" #domain goes here
driver_location='chromedriver.exe'

browser = webdriver.Chrome(driver_location)

#function
def snapLogin(url,browser,uname,pwrd):
    
    browser.get(str(url))

    time.sleep(10)

    # emailinput =  browser.find_elements_by_xpath("//input[@name='email']")
    elem1 = browser.find_element_by_name("email")
    elem1.send_keys(uname)

    elem2 = browser.find_element_by_name("password")
    elem2.send_keys(pwrd)

    browser.find_element_by_class_name('palette-Light-Blue-800').click()

    time.sleep(5)

    browser.find_element_by_class_name('btn-primary').click()

snapLogin(url,browser,snap_email,snap_pass)