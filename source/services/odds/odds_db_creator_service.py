import resources.config as config
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
from source.dao.odd_dao import OddDAO
from bs4 import BeautifulSoup, Comment
from source.scrapers.sportsbooks.betano_scrap import BetanoScrap

class OddsDBCreatorService():
    def __init__(self):
        pass
        #DAO.__init__(self)
    
    def getAndSaveNHLOdds(self):
        
        df = BetanoScrap().getNHLOddsDF()
    
        for index, row in df.iterrows():
            teamsName = row['Jogos'][14:len(row['Jogos'])]
            splited = teamsName.split("  ")
            visitorName = splited[1]
            homeName = splited[0]
            
            dateHour = row['Jogos'][0:12].split(" ")
            date = dateHour[0]
            hour = dateHour[2]
            
            visitor, home = self.extractHomeVisitorOdds(row)
            total, total_upper, total_under = self.extractTotalOdds(row)            
            handicap_visitor, odd_handicap_visitor, handicap_home, odd_handicap_home = self.extractHandicapOdds(row)
                    
            OddDAO.createOdd(0, dt(2023, int(date.split("/")[1]), int(date.split("/")[0]), int(hour.split(":")[0]), int(hour.split(":")[1]), 0, 0),
                             dt.now(), visitorName, homeName, visitor, home, handicap_visitor, handicap_home, odd_handicap_visitor,
                             odd_handicap_home, total, total_under, total_upper, "NHL")
        return df
    
    def extractHandicapOdds(self, row):
        plusposition = row['HANDICAP'].index("+")
        minosposition = row['HANDICAP'].index("-")
        position = plusposition if plusposition < minosposition else minosposition
        handicap = row['HANDICAP'][position:len(row['HANDICAP'])].split(" ")
        
        if len(handicap) == 5:
            handicap_home = float(handicap[0])
            odd_handicap_home = float(handicap[1])
            handicap_visitor = float(handicap[3])
            odd_handicap_visitor = float(handicap[4])
            return handicap_visitor, odd_handicap_visitor, handicap_home, odd_handicap_home
        else:
            if plusposition < minosposition: #Home positivo, visitante negativo
                handicapVisitor = row['HANDICAP'][minosposition:len(row['HANDICAP'])].split(" ")
                handicapHome = row['HANDICAP'][plusposition:plusposition+10].split(" ")
                
                handicap_home = float(handicapHome[0])
                odd_handicap_home = float(handicapHome[1])
                handicap_visitor = float(handicapVisitor[0])
                odd_handicap_visitor = float(handicapVisitor[1])
                
                return handicap_visitor, odd_handicap_visitor, handicap_home, odd_handicap_home
            else:
                handicapVisitor = row['HANDICAP'][plusposition:len(row['HANDICAP'])].split(" ")
                handicapHome = row['HANDICAP'][minosposition:minosposition+10].split(" ")
                
                handicap_home = float(handicapHome[0])
                odd_handicap_home = float(handicapHome[1])
                handicap_visitor = float(handicapVisitor[0])
                odd_handicap_visitor = float(handicapVisitor[1])
                
                return handicap_visitor, odd_handicap_visitor, handicap_home, odd_handicap_home
    
    def extractHomeVisitorOdds(self, row):
        odds = row['1  X  2'][41:len(row['1  X  2'])].split(" ")
        
        if len(odds) == 10:
            home = float(odds[3])
            visitor = float(odds[9])
            return visitor, home
        else:
            home = float(odds[0])
            visitor = float(odds[4])
            return visitor, home
        
    
    def extractTotalOdds(self, row):
        if "+" in row['MAIS/MENOS']:
            position = row['MAIS/MENOS'].index("+")
            
            total = row['MAIS/MENOS'][position:len(row['MAIS/MENOS'])]
            total_visitor_splitted = total[0:int((len(total)/2)-1)].split(" ")
            total_home_splitted = total[int((len(total)/2)+1):len(total)].split(" ")
            
            total = float(total_visitor_splitted[1])
            total_upper = float(total_visitor_splitted[2])
            total_under = float(total_home_splitted[2])
            return total, total_upper, total_under
                
        elif "Mais" in row['MAIS/MENOS']:
            position = str(row['MAIS/MENOS']).find("Mais")
            
            totalsplited = row['MAIS/MENOS'][position:len(row['MAIS/MENOS'])].split(" ")
            total = totalsplited[1][2:len(totalsplited[1])]
            total_upper = float(totalsplited[2])
            total_under = float(totalsplited[6])
            
            return total, total_upper, total_under
        else:
            print("String Total de Pontos nao encontrada")
        
    
    def getAndSaveNBAOdds(self):
        
        df = BetanoScrap().getNBAOddsDF()
        
        for index, row in df.iterrows():
            teamsName = row['Jogos'][14:len(row['Jogos'])]
            splited = teamsName.split("  ")
            visitorName = splited[1]
            homeName = splited[0]
            
            dateHour = row['Jogos'][0:12].split(" ")
            date = dateHour[0]
            hour = dateHour[2]
            
            vencedorsplited = row['VENCEDOR'].split("  ")
            if len(vencedorsplited) == 3:
                home = float(vencedorsplited[1][len(vencedorsplited[1])-4:len(vencedorsplited[1])])
                visitor = float(vencedorsplited[2][len(vencedorsplited[2])-4:len(vencedorsplited[2])])
            else:
                odds = row['VENCEDOR'][len(row['VENCEDOR'])-10:len(row['VENCEDOR'])].split(" ")
                home = float(odds[0])
                visitor = float(odds[2])
            
            #position = row['MAIS/MENOS'].index("+")
            #total = row['MAIS/MENOS'][position:len(row['MAIS/MENOS'])]
            #total_visitor_splitted = total[0:int((len(total)/2)-1)].split(" ")
            #total_home_splitted = total[int((len(total)/2)+1):len(total)].split(" ")
            #
            #total_value = float(total_visitor_splitted[1])
            #total_upper = float(total_visitor_splitted[2])
            #total_under = float(total_home_splitted[2])
            total_value, total_upper, total_under = self.extractTotalOdds(row)
            
            #plusposition = row['HANDICAP'].index("+")
            #minosposition = row['HANDICAP'].index("-")
            #position = plusposition if plusposition < minosposition else minosposition
            #
            #handicap = row['HANDICAP'][position:len(row['HANDICAP'])].split(" ")
            #handicap_home = float(handicap[0])
            #odd_handicap_home = float(handicap[1])
            #handicap_visitor = float(handicap[3])
            #odd_handicap_visitor = float(handicap[4])
            handicap_visitor, odd_handicap_visitor, handicap_home, odd_handicap_home = self.extractHandicapOdds(row)
            
            OddDAO.createOdd(0, dt(2023, int(date.split("/")[1]), int(date.split("/")[0]), int(hour.split(":")[0]), int(hour.split(":")[1]), 0, 0),
                             dt.now(), visitorName, homeName, visitor, home, handicap_visitor, handicap_home, odd_handicap_visitor,
                             odd_handicap_home, total_value, total_under, total_upper, "NBA")
            
        return df