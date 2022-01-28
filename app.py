import os
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv
from lxml import html
import requests
load_dotenv()
message_request = os.environ.get('PYTHON_SCRIPT_KEY')
hidden_route = os.environ.get('HIDDEN_ROUTE')
embed_iframe = ''

option = webdriver.ChromeOptions()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})
# GOOGLE CHROME BIN IS ONLY NEEDED FOR HEROKU
option.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')

print('THIS IS THE PATH', os.environ.get('CHROME_DRIVER_PATH'))
driver = webdriver.Chrome(chrome_options=option, executable_path=os.environ.get('CHROME_DRIVER_PATH'))

driver.get('https://www.facebook.com/')
try:
    myElemWait1 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID,'email')))
    print('DONE LOADING')
except TimeoutException:
    print('LOADING IS TAKING TOO LONG')

email = driver.find_element(By.NAME, 'email')
email.send_keys(os.environ.get('EMAIL'))
password = driver.find_element(By.NAME, 'pass')
password.send_keys(os.environ.get('PASSWORD'))

password.send_keys(Keys.RETURN)
try:
    element = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'RANDOM STUFF'))
    )
except:
    print('NOPE DIDNT FIND IT')
finally:
    driver.get('https://www.facebook.com/pibelcalvario/')


try:
    element = WebDriverWait(driver, 8).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'RANDOM STUFF'))
    )
except TimeoutException:
    print('WORKING ON FINDING LIVE POST')
    html_selenium = driver.page_source
    doc = html.fromstring(html_selenium)
    all_lives = doc.xpath("//*[text()=' is live now.']" )
    # NEED TO CREATE FUNCTION THAT DETECTS THE TIME OF DAY AND SENDS THE "WAS LIVE"

    # all_lives = doc.xpath("//*[text()=' was live.']" )
    first_live = all_lives[0]
    first_live_path = first_live.getroottree().getpath(first_live)
    print('FIRST LIVE PATH:', first_live_path)
    sibling_number = str(int(first_live_path[-26]) + 1)

    new_path = first_live_path[:-26] + sibling_number + ']/div'
    print(new_path)
    three_dots = driver.find_element(By.XPATH, new_path)
    three_dots.click()




finally:
    print('DONE WITH SECOND WAIT')


try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'RANDOM STUFF'))
    )
except TimeoutException:
    print('CLICKING ON EMBED MENU')
    embed = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[4]')
    embed.click()
finally:
    print('done with 3rd wait')


try:
    element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'RANDOM STUFF'))
    )
except TimeoutException:
    print('OBTAINING iFRAME VALUE TO SEND TO BACKEND SERVER')
    iframe = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div[1]/label/input')
    print(iframe.get_attribute('value'))
    embed_iframe = str(iframe.get_attribute('value'))
finally:
    print('done with 4th wait')

driver.quit()

############# FOR PRODUCTION ##############

post_value = requests.post(f'https://pibec-website.herokuapp.com{hidden_route}/update', json={'message_request': message_request, 'iframe': embed_iframe})

############# FOR DEV TESTING ##############
# post_value = requests.post(f'http://localhost:3000{hidden_route}/update', json={'message_request': message_request, 'iframe': embed_iframe})

print(post_value.text)

# Next step:
# Need to make sure it gets tried multiple times. once it is succesful, then it will stop the loop.
# otherwise it will try a number of times
# this is to fix the issue of not finding a live postat 11:30 and then just failing without trying again.

# this will need to run every 2 minutes.
