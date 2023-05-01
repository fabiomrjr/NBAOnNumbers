import requests
import re
import numpy as np
import pandas as pd
import resources.config as config

from selenium import webdriver
from datetime import datetime as dt
from bs4 import BeautifulSoup, Comment
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketballReferenceGameScrap:
    def __init__(self):
     pass

    def callPage(self, url, visitCode, homeCode):
        
        driver = webdriver.Chrome()
        driver.implicitly_wait(10) # seconds
        driver.get(config.baseURL + url)
        visitorBasic = ""
        visitorAdvanced = ""
        homeBasic = ""
        homeAdvanced = ""
        inactives = ""
        print('-------------------------')
        print('Inicio processando Jogo ' + url)
        
        try:
            visitorBasic = (driver.find_elements(By.ID, "box-" + visitCode + "-game-basic"))[0].get_attribute("outerHTML")
            visitorAdvanced = (driver.find_elements(By.ID, "box-" + visitCode + "-game-advanced"))[0].get_attribute("outerHTML")
            
            homeBasic = (driver.find_elements(By.ID, "box-" + homeCode + "-game-basic"))[0].get_attribute("outerHTML")
            homeAdvanced = (driver.find_elements(By.ID, "box-" + homeCode + "-game-advanced"))[0].get_attribute("outerHTML")

            inactives  = (driver.find_elements(By.XPATH, "//*[@id='"'content'"']/div[23]/div[1]"))[0].get_attribute("outerHTML")
        finally:
            driver.quit()
            
        dfVisitorBasic, dfVisitorAdvanced, dfHomeBasic, dfHomeAdvanced = self.formatData(visitorBasic, visitorAdvanced, homeBasic, homeAdvanced)
        dfVisitor, dfHome = self.joinBasicAdvancedDataFrames(dfVisitorBasic, dfVisitorAdvanced, dfHomeBasic, dfHomeAdvanced)
        dfVisitor, dfHome = self.inputInactives(inactives, visitCode, homeCode, dfVisitor, dfHome)
        print('Fim processamento Jogo ' + url)
        print('-------------------------')
        return dfVisitor, dfHome
    
    def formatData(self, visitorBasic, visitorAdvanced, homeBasic, homeAdvanced):
        dfVisitorBasic = pd.read_html(str(visitorBasic))[0]
        dfVisitorAdvanced = pd.read_html(str(visitorAdvanced))[0]
        dfHomeBasic = pd.read_html(str(homeBasic))[0]
        dfHomeAdvanced = pd.read_html(str(homeAdvanced))[0]

        dfVisitorBasic.columns = dfVisitorBasic.columns.droplevel(0)
        dfVisitorAdvanced.columns = dfVisitorAdvanced.columns.droplevel(0)
        dfHomeBasic.columns = dfHomeBasic.columns.droplevel(0)
        dfHomeAdvanced.columns = dfHomeAdvanced.columns.droplevel(0)
        
        dfVisitorBasic = dfVisitorBasic.replace('Did Not Play', '0').fillna(0)
        dfVisitorAdvanced = dfVisitorAdvanced.replace('Did Not Play', '0').fillna(0)
        dfHomeBasic = dfHomeBasic.replace('Did Not Play', '0').fillna(0)
        dfHomeAdvanced = dfHomeAdvanced.replace('Did Not Play', '0').fillna(0)
        
        dfVisitorBasic = dfVisitorBasic.drop([5])
        dfHomeBasic = dfHomeBasic.drop([5])
        
        return dfVisitorBasic, dfVisitorAdvanced, dfHomeBasic, dfHomeAdvanced

    def joinBasicAdvancedDataFrames(self, dfVisitorBasic, dfVisitorAdvanced, dfHomeBasic, dfHomeAdvanced):
        
        dfVisitorBasic = dfVisitorBasic.assign(ts_perc= dfVisitorAdvanced['TS%'])
        dfVisitorBasic = dfVisitorBasic.assign(efg_perc= dfVisitorAdvanced['eFG%'])
        dfVisitorBasic = dfVisitorBasic.assign(threepar_perc= dfVisitorAdvanced['3PAr'])
        dfVisitorBasic = dfVisitorBasic.assign(ftr_perc= dfVisitorAdvanced['FTr'])
        dfVisitorBasic = dfVisitorBasic.assign(orb_perc= dfVisitorAdvanced['ORB%'])
        dfVisitorBasic = dfVisitorBasic.assign(drb_perc= dfVisitorAdvanced['DRB%'])
        dfVisitorBasic = dfVisitorBasic.assign(trb_perc= dfVisitorAdvanced['TRB%'])
        dfVisitorBasic = dfVisitorBasic.assign(ast_perc= dfVisitorAdvanced['AST%'])
        dfVisitorBasic = dfVisitorBasic.assign(stl_perc= dfVisitorAdvanced['STL%'])
        dfVisitorBasic = dfVisitorBasic.assign(blk_perc= dfVisitorAdvanced['BLK%'])
        dfVisitorBasic = dfVisitorBasic.assign(tov_perc= dfVisitorAdvanced['TOV%'])
        dfVisitorBasic = dfVisitorBasic.assign(usg_perc= dfVisitorAdvanced['USG%'])
        dfVisitorBasic = dfVisitorBasic.assign(or_tg= dfVisitorAdvanced['ORtg'])
        dfVisitorBasic = dfVisitorBasic.assign(dr_tg= dfVisitorAdvanced['DRtg'])
        dfVisitorBasic = dfVisitorBasic.assign(bpm= dfVisitorAdvanced['BPM'])
        
        dfHomeBasic = dfHomeBasic.assign(ts_perc= dfHomeAdvanced['TS%'])
        dfHomeBasic = dfHomeBasic.assign(efg_perc= dfHomeAdvanced['eFG%'])
        dfHomeBasic = dfHomeBasic.assign(threepar_perc= dfHomeAdvanced['3PAr'])
        dfHomeBasic = dfHomeBasic.assign(ftr_perc= dfHomeAdvanced['FTr'])
        dfHomeBasic = dfHomeBasic.assign(orb_perc= dfHomeAdvanced['ORB%'])
        dfHomeBasic = dfHomeBasic.assign(drb_perc= dfHomeAdvanced['DRB%'])
        dfHomeBasic = dfHomeBasic.assign(trb_perc= dfHomeAdvanced['TRB%'])
        dfHomeBasic = dfHomeBasic.assign(ast_perc= dfHomeAdvanced['AST%'])
        dfHomeBasic = dfHomeBasic.assign(stl_perc= dfHomeAdvanced['STL%'])
        dfHomeBasic = dfHomeBasic.assign(blk_perc= dfHomeAdvanced['BLK%'])
        dfHomeBasic = dfHomeBasic.assign(tov_perc= dfHomeAdvanced['TOV%'])
        dfHomeBasic = dfHomeBasic.assign(usg_perc= dfHomeAdvanced['USG%'])
        dfHomeBasic = dfHomeBasic.assign(or_tg= dfHomeAdvanced['ORtg'])
        dfHomeBasic = dfHomeBasic.assign(dr_tg= dfHomeAdvanced['DRtg'])
        dfHomeBasic = dfHomeBasic.assign(bpm= dfHomeAdvanced['BPM'])

        return dfVisitorBasic, dfHomeBasic
    
    def inputInactives(self, inactives, visitCode, homeCode, dfVisitor, dfHome):
        
        lineTableDataBS = BeautifulSoup(str(inactives), 'html.parser')
        for lineData in lineTableDataBS:
            lineDataBS = BeautifulSoup(str(lineData.extract()), 'html.parser')
            value = lineDataBS.get_text()
            splitted = value.split("\xa0")
            
            visitInactives = []
            homeInactives = []
            current=""
            for item in splitted:
                if item == visitCode:
                    current=visitCode
                elif item == homeCode:
                    current=homeCode
                else:
                    if current == visitCode and item != '':
                        t = [item.replace(",",""),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        visitInactives.append(t)
                    elif current == homeCode and item != '':
                        t = [item.replace(",",""),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                        homeInactives.append(t)
            #['Inactive:', 'PHI', 'Julian Champagnie,', 'Michael Foster Jr.', '', '', 'BOS', 'Danilo Gallinari,', 'Robert Williams', '', '', '']

        for line in visitInactives:
            dfVisitor.loc[len(dfVisitor)] = line
            print()
        
        for line in homeInactives:
            dfHome.loc[len(dfHome)] = line
            print()
            
        return dfVisitor, dfHome