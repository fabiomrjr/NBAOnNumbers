import config
import math
import requests
import re
import numpy as np
import pandas as pd

from datetime import datetime as dt

from selenium import webdriver
from datetime import datetime as dt
from bs4 import BeautifulSoup, Comment
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from model.game import Game as game
from dao.team_dao import TeamDAO
from dao.odd_dao import OddDAO
from dao import dao

class OddsDBCreatorService():
    def __init__(self):
        pass
        #DAO.__init__(self)
        
    def getAndSaveOdds():

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
            
        dfbase=pd.DataFrame()
        df=pd.read_html(str(a))[0]


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
        
        for index, row in df.iterrows():
            teamsName = row['Jogos'][14:len(row['Jogos'])]
            
            dateHour = row['Jogos'][0:12].split(" ")
            date = dateHour[0]
            hour = dateHour[2]
            
            odds = row['1  X  2'][len(row['1  X  2'])-16:len(row['1  X  2'])].split(" ")
            visitor = float(odds[0])
            home = float(odds[2])
            
            total = row['MAIS/MENOS'][35:len(row['MAIS/MENOS'])]
            total_visitor_splitted = total[0:int((len(total)/2)-1)].split(" ")
            total_home_splitted = total[int((len(total)/2)+1):len(total)].split(" ")
            
            total = float(total_visitor_splitted[1])
            total_upper = float(total_visitor_splitted[2])
            total_under = float(total_home_splitted[2])
            
            handicap = row['HANDICAP'][14:len(row['HANDICAP'])].split(" ")
            handicap_visitor = float(handicap[0])
            odd_handicap_visitor = float(handicap[1])
            handicap_home = float(handicap[3])
            odd_handicap_home = float(handicap[4])
            
            #id_game, game_date, date, visitor_team_name, home_team_name, visitor_win_odd,
            #home_win_odd, visitor_spread, home_spread, visitor_win_spread, home_win_spread, total, total_under, total_upper
            OddDAO.createOdd(0, dt(2023, int(date.split("/")[1]), int(date.split("/")[0]), int(hour.split(":")[0]), int(hour.split(":")[1]), 0, 0),
                             dt.now(), teamsName, "", visitor, home, handicap_visitor, handicap_home, odd_handicap_visitor,
                             odd_handicap_home, total, total_under, total_upper)
        return df