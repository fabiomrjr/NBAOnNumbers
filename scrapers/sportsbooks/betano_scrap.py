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



url = "https://br.betano.com/sport/hoquei-no-gelo/ligas/10118r/"
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

a = driver.find_elements(By.CLASS_NAME, "events-list__grid")[0].get_attribute("outerHTML")
#b = driver.find_elements(By.CLASS_NAME, "prebet-match__odds__container")
#b = driver.find_elements(By.CLASS_NAME, "grid-six-pack-wrapper ng-star-inserted")
dfbase=pd.DataFrame()
df=pd.read_html(str(a))[0]
print("---------------------")
print(a[0].text)
print("---------------------")
print(b[0].text)
print("---------------------")
driver.quit()

#'Jogos', '1  X  2', 'MAIS/MENOS', 'HANDICAP', 'Unnamed: 4'
#df.iloc[0][0]
# '20/02  15:00  Boston Bruins  Ottawa Senators'
#df.iloc[0][1]
#'Resultado no Final do Tempo Regulamentar  273 1.42  5.30  6.00'
#df.iloc[0][2]
#'Total de gols (Tempo regular)  273 + 6.5 2.25  - 6.5 1.65'
#df.iloc[0][3]
#'Handicap  273 -1.5 1.65  +1.5 2.25'
#df.iloc[0][4]
#273