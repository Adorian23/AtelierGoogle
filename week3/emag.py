import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import selenium.common.exceptions as exceptions

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.emag.ro/#opensearch')
get_element=browser.find_element(by=By.ID,value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()
date = browser.find_elements(by=By.CLASS_NAME,value='card-v2')
for i in date:
    try:
        title_of_products =  i.find_element(by=By.CLASS_NAME,value='card-v2-title')
        print(i.text)
    except exceptions.StaleElementReferenceException:
        pass
time.sleep(10)