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
# op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')

print('THIS IS THE PATH', os.environ.get('CHROME_DRIVER_PATH'))
driver = webdriver.Chrome(chrome_options=option, executable_path=os.environ.get('CHROME_DRIVER_PATH'))

driver.get('https://www.facebook.com/')
email = driver.find_element(By.NAME, 'email')
email.send_keys(os.environ.get('EMAIL'))
password = driver.find_element(By.NAME, 'pass')
password.send_keys(os.environ.get('PASSWORD'))

password.send_keys(Keys.RETURN)
try:
    element = WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'RANDOM STUFF'))
    )
except:
    print('NOPE DIDNT FIND IT')
finally:
    driver.get('https://www.facebook.com/pibelcalvario/')


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
# try:
try:
    element = WebDriverWait(driver, 6).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'RANDOM STUFF'))
    )
except TimeoutException:
    html_selenium = driver.page_source
    doc = html.fromstring(html_selenium)
    all_lives = doc.xpath("//*[text()=' was live.']" )
    first_live = all_lives[0]
    first_live_path = first_live.getroottree().getpath(first_live)
    print(first_live_path)
    sibling_number = str(int(first_live_path[-21]) + 1)
    new_path = first_live_path[:-21] + sibling_number + ']/div'
    print(new_path)
    three_dots = driver.find_element(By.XPATH, new_path)
    three_dots.click()




finally:
    print('DONE WITH SECOND WAIT')


try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'RANDOM STUFF'))
    )
except TimeoutException:
    embed = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[4]')
    embed.click()
finally:
    print('done with 3rd wait')


try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'RANDOM STUFF'))
    )
except TimeoutException:
    iframe = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div[1]/label/input')
    print(iframe.get_attribute('value'))
    embed_iframe = str(iframe.get_attribute('value'))
finally:
    print('done with 4th wait')

driver.quit()

requests.post(f'http://localhost:5000{hidden_route}/update', json={'message_request': message_request, 'iframe': embed_iframe})
# html_selenium = driver.page_source
# doc = html.fromstring(html_selenium)
# all_lives = doc.xpath("//strong[text()=' was live.']" )
# print(all_lives)
# first_live = all_lives[0]
# print(first_live.getroottree().getpath(first_live))

# was_live = driver.find_element(By.XPATH, "//h2[text()=' was live.']" )
# print(was_live)
# h2_live = was_live.find_element_by_xpath('..')
# h2_live_path = h2_live.get_attribute('d')
# print(h2_live_path)

# span_live = h2_live.find_element_by_xpath('..')
# div1_live = span_live.find_element_by_xpath('..')
# div2_live = div1_live.find_element_by_xpath('..')
# div3_live = div2_live.find_element_by_xpath('..')
# div3_live_path = div3_live.getroottree().getpath(div3_live)
# print(div3_live_path)
    # sibling_div = div3_live.find_element_by_xpath('..')
    # sibling_div.click()
    # tag_value = was_live.text
    # print(tag_value)
    # print(was_live)
# except NoSuchElementException:
# except :
#     print('ELEMENT DOES NOT EXISTS')
# finally:
#     print('FOUND ELEMENT')

# ON HEROKU
