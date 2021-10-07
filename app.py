import os
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
load_dotenv()

# op = webdriver.ChromeOptions()
# op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
# # op.add_argument('--headless')
# op.add_argument('--no-sandbox')
# op.add_argument('--disable-dev-sh-usage')
print('THIS IS THE PATH', os.environ.get('CHROME_DRIVER_PATH'))
driver = webdriver.Chrome(executable_path=os.environ.get('CHROME_DRIVER_PATH'))

driver.get('https://www.facebook.com/')
email = driver.find_element_by_name('email')
email.send_keys(os.environ.get('EMAIL'))
password = driver.find_element_by_name('pass')
password.send_keys(os.environ.get('PASSWORD'))

password.send_keys(Keys.RETURN)
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'oajrlxb2 rq0escxv'))
#     )
# finally:
#     driver.get('https://www.facebook.com/pibelcalvario/')
driver.implicitly_wait(10)
driver.get('https://www.facebook.com/pibelcalvario/')
print('ARE WE REACHING THIS?')
# try:
#     element = WebDriverWait(driver, 15).until(
#         EC.presence_of_all_elements_located((By.CLASS_NAME, 'bi6gxh9e aov4n071'))
#     )
# finally:
#     print('HIT THIS LINE')
#     try:
#         driver.find_elements_by_xpath("//*[contains(text(), ' was live.')]")
#         print('FOUND ELEMENT')
#     except NoSuchElementException:
#         print('ELEMENT DOES NOT EXISTS')

# child = driver.find_element_by_xpath("//*[contains(text(), ' was live.')]")
try:
    driver.find_elements_by_xpath("//*[contains(text(), ' was live.')]")
except NoSuchElementException:
    print('ELEMENT DOES NOT EXISTS')
finally:
    print('FOUND ELEMENT')

# ON HEROKU
