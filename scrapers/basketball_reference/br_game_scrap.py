import requests
import re
import numpy as np
import pandas as pd
import config
import time

from selenium import webdriver
from bs4 import BeautifulSoup, Comment
from requests_html import HTMLSession
#from ghost import Ghost
#from robobrowser import browser

class BasketballReferenceGameScrap:
    def __init__(self):
     pass

    def check(self, link):
        pageBS = self.callPage(config.baseURL + link)
        df1 = self.extractTable(pageBS)
        return

    def callPage(self, url):
        #s = HTMLSession()
        #response = s.get(url)
        #response.html.render()
        #url = "http://legendas.tv/busca/walking%20dead%20s03e02"
        driver = webdriver.Chrome()# ChromeOptions()# PhantomJS()
        #driver = webdriver.Firefox()
        driver.get(url)
        #a = driver.find_element("id", 'wrap')
        string1 = str("javascript:document.getElementById('wrap').click();")
        driver.execute_script(string1)
        driver.execute_script("//cdn.confiant-integrations.net/gptprebidnative/202212211045/wrap.js")
        a = driver.find_element("id", 'wrap'). click()
        html = driver.page_source
        driver.quit()
        tt= BeautifulSoup(html, 'html.parser')

        #print(html)
        #soup = BeautifulSoup(html, 'lxml')
        #req = browser.get(url) #requests.get(url)
        #teste = requests()
        #teste.html.render(sleep=5, keep_page=True)
        req = requests.get("https://www.basketball-reference.com/boxscores/201912010BRK.html", time.sleep(10))
        content = ''
        if req.status_code == 200:
            print('Requisição bem sucedida! Game ')
            content = req.content

        #html = browser.page_source
        return BeautifulSoup(content, 'html.parser')
    
    def extractTable(self, pageBS):
        
        #table = soup.find_all('table', attrs={'class':'teams'})
        #pageBS = BeautifulSoup(page, 'html.parser')
        lineScoreBS = pageBS.find_all('table', attrs={'id':'line_score'})
        lineScoreStringTable = str(lineScoreBS)
        
        lineScoreBSParser = BeautifulSoup(lineScoreStringTable, 'html.parser')
        bodyLineScoreBody = lineScoreBSParser.find_all('tbody')
        bodyLineScoreStringBody = str(bodyLineScoreBody)
        
        firstColumnLineScoreBS = BeautifulSoup(bodyLineScoreStringBody, 'html.parser')
        firstColumnLineScore = firstColumnLineScoreBS.find_all('th')
        
        
        
        visitorBS = pageBS.find_all('table', attrs={'id':'box-PHI-game-basic'})
        visitorString = str(visitorBS)
        
        homeBS = pageBS.find_all('table', attrs={'id':'box-BOS-game-basic'})
        homeString = str(homeBS)
        

        #scheduleTableBS = BeautifulSoup(scheduleStringTable, 'html.parser')
        bodySchedule = scheduleTableBS.find_all('tbody')
        bodyStringSchedule = str(bodySchedule)
        
        bodyScheduleBS = BeautifulSoup(bodyStringSchedule, 'html.parser')
        lineTableData = bodyScheduleBS.find_all('tr')
        lineStringTableData = str(lineTableData)
        lineTableDataBS = BeautifulSoup(lineStringTableData, 'html.parser')

        lineFirstColumnTable = lineTableDataBS.find_all('th')
        
        lineDataTable = lineTableDataBS.find_all('td')
        return None