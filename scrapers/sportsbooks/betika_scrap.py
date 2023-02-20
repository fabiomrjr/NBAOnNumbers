import requests
import re
import numpy as np
import pandas as pd

from selenium import webdriver
from datetime import datetime as dt
from bs4 import BeautifulSoup, Comment
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = "https://www.betika.com/en-ke/s/basketball/usa-nba"
b = ""
element = ""
driver = webdriver.Chrome()# ChromeOptions()# PhantomJS()
#driver = webdriver.Firefox()
driver.implicitly_wait(15) # seconds
driver.get(url)
#try:
#    element = WebDriverWait(driver, 15).until(
#        EC.presence_of_element_located((By.CLASS_NAME, "StatsTableBody_tbody__uvj_P"))
#    )
#    b=(element.text)
#finally:
#    driver.quit()

a = driver.find_elements(By.CLASS_NAME, "prebet-match__teams")
b = driver.find_elements(By.CLASS_NAME, "prebet-match__odds__container")
#b = driver.find_elements(By.CLASS_NAME, "grid-six-pack-wrapper ng-star-inserted")

print("---------------------")
print(a[0].text)
print("---------------------")
print(b[0].text)
print("---------------------")
driver.quit()

#req = requests.get("https://www.basketball-reference.com/boxscores/201912010BRK.html", time.sleep(10))
content = ''
if req.status_code == 200:
    print('Requisição bem sucedida! Game ')
    content = req.content

#html = browser.page_source
#return BeautifulSoup(content, 'html.parser')

#startDate = dt.now()
#df = check()
#endDate = dt.now()
#print("Finish Game Builder. Seconds " + str((endDate - startDate).total_seconds()))