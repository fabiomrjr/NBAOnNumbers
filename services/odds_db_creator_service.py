import config
import math
import requests
import re
import numpy as np
import pandas as pd

from datetime import datetime as dt

from selenium import webdriver
from datetime import datetime as dt
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from dao.odd_dao import OddDAO
from dao import dao

class OddsDBCreatorService():
    def __init__(self):
        pass
        #DAO.__init__(self)
        
    def getAndSaveNHLOdds():

        url = "https://br.betano.com/sport/hoquei-no-gelo/ligas/10118r/"
        a = ""
        element = ""
        driver = webdriver.Chrome()
        driver.implicitly_wait(15) # seconds
        driver.get(url)
        try:
            a = driver.find_elements(By.CLASS_NAME, "events-list__grid")[0].get_attribute("outerHTML")
        finally:
            driver.quit()
            
        df=pd.read_html(str(a))[0]
        
        for index, row in df.iterrows():
            teamsName = row['Jogos'][14:len(row['Jogos'])]
            splited = teamsName.split("  ")
            visitorName = splited[1]
            homeName = splited[0]
            
            dateHour = row['Jogos'][0:12].split(" ")
            date = dateHour[0]
            hour = dateHour[2]
            
            odds = row['1  X  2'][len(row['1  X  2'])-16:len(row['1  X  2'])].split(" ")
            home = float(odds[0])
            visitor = float(odds[4])
            
            position = row['MAIS/MENOS'].index("+")
            total = row['MAIS/MENOS'][position:len(row['MAIS/MENOS'])]
            total_visitor_splitted = total[0:int((len(total)/2)-1)].split(" ")
            total_home_splitted = total[int((len(total)/2)+1):len(total)].split(" ")
            
            total = float(total_visitor_splitted[1])
            total_upper = float(total_visitor_splitted[2])
            total_under = float(total_home_splitted[2])
            
            plusposition = row['HANDICAP'].index("+")
            minosposition = row['HANDICAP'].index("-")
            position = plusposition if plusposition < minosposition else minosposition
            
            handicap = row['HANDICAP'][position:len(row['HANDICAP'])].split(" ")
            handicap_home = float(handicap[0])
            odd_handicap_home = float(handicap[1])
            handicap_visitor = float(handicap[3])
            odd_handicap_visitor = float(handicap[4])
            
            OddDAO.createOdd(0, dt(2023, int(date.split("/")[1]), int(date.split("/")[0]), int(hour.split(":")[0]), int(hour.split(":")[1]), 0, 0),
                             dt.now(), visitorName, homeName, visitor, home, handicap_visitor, handicap_home, odd_handicap_visitor,
                             odd_handicap_home, total, total_under, total_upper, "NHL")
        return df
    
    def getAndSaveNBAOdds():
    
        url = "https://br.betano.com/sport/basquete/eua/nba/17106/"
        a = ""
        element = ""
        driver = webdriver.Chrome()
        driver.implicitly_wait(15) # seconds
        driver.get(url)
        try:
            a = driver.find_elements(By.CLASS_NAME, "events-list__grid")[0].get_attribute("outerHTML")
        finally:
            driver.quit()
            
        df=pd.read_html(str(a))[0]
        
        for index, row in df.iterrows():
            teamsName = row['Jogos'][14:len(row['Jogos'])]
            splited = teamsName.split("  ")
            visitorName = splited[1]
            homeName = splited[0]
            
            dateHour = row['Jogos'][0:12].split(" ")
            date = dateHour[0]
            hour = dateHour[2]
            
            odds = row['VENCEDOR'][len(row['VENCEDOR'])-10:len(row['VENCEDOR'])].split(" ")
            home = float(odds[0])
            visitor = float(odds[2])
            
            position = row['MAIS/MENOS'].index("+")
            total = row['MAIS/MENOS'][position:len(row['MAIS/MENOS'])]
            total_visitor_splitted = total[0:int((len(total)/2)-1)].split(" ")
            total_home_splitted = total[int((len(total)/2)+1):len(total)].split(" ")
            
            total_value = float(total_visitor_splitted[1])
            total_upper = float(total_visitor_splitted[2])
            total_under = float(total_home_splitted[2])
            
            plusposition = row['HANDICAP'].index("+")
            minosposition = row['HANDICAP'].index("-")
            position = plusposition if plusposition < minosposition else minosposition
            
            handicap = row['HANDICAP'][position:len(row['HANDICAP'])].split(" ")
            handicap_home = float(handicap[0])
            odd_handicap_home = float(handicap[1])
            handicap_visitor = float(handicap[3])
            odd_handicap_visitor = float(handicap[4])
            
            OddDAO.createOdd(0, dt(2023, int(date.split("/")[1]), int(date.split("/")[0]), int(hour.split(":")[0]), int(hour.split(":")[1]), 0, 0),
                             dt.now(), visitorName, homeName, visitor, home, handicap_visitor, handicap_home, odd_handicap_visitor,
                             odd_handicap_home, total_value, total_under, total_upper, "NBA")
        return df