import math

from datetime import datetime as dt

class util():
    def __init__(self):
        pass
    
    def getMonthByDesc(self, month):
    
        switcher = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        return switcher.get(month, "Invalid month")
    
    def getMonthByAbreviation(self, month):
    
        switcher = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12
        }
        return switcher.get(month, "Invalid month")

    def getDateTimeByDayAndTime(self, dayGame, timeGame, type):
        if "-" in dayGame:
            #  2022-10-18
            splitted = dayGame.split("-")
            year = int(splitted[0])
            month = int(splitted[1])
            day = int(splitted[2])
            
            return dt(year, month, day, 0, 0, 0, 0)
        
        elif  "mlb_preview" == type:
            dayGameRemoved = dayGame.replace(",","")
            splitted = dayGameRemoved.split(" ")
            year = int(splitted[3][0:-5])
            month = self.getMonthByDesc(splitted[1])
            day = int(splitted[2])
            
            return dt(year, month, day, 0, 0, 0, 0)
        
        elif  "mlb_boxscore" == type:
            #'>Thursday, March 30, 2023</'
            #'>Start Time: 2:10 p.m. Local</'
            #March 30, 2023
            #0:
            #''
            #1:
            #'April'
            #2:
            #''
            #3:
            #'1'
            #4:
            #'2023</h1>'
            #len():
            #5
            dayGameRemoved = dayGame.replace(",","")
            splitted = dayGameRemoved.split(" ")
            year = int(splitted[3][0:-2])
            month = self.getMonthByDesc(splitted[1])
            day = int(splitted[2])
            
            splitted_string_time = timeGame.split(" ")
            splitted_time = splitted_string_time[2].split(":")
            hour = int(splitted_time[0])
            minute = int(splitted_time[1])
            
            return dt(year, month, day, hour, minute, 0, 0)
        else:    
            #  Tue, Oct 18, 2022   7:30p
            dayGameRemoved = dayGame.replace(",","")
            splitted = dayGameRemoved.split(" ")
            
            year = int(splitted[3])
            month = self.getMonthByAbreviation(splitted[1])
            day = int(splitted[2])
            time = timeGame.split(":")
            hour = 12 + int(time[0])
            minutes = int(time[1][:-1])

            if hour == 24:
                hour = 0

            return dt(year, month, day, hour, minutes, 0, 0)
    
    def emptyOrNan(self, value):
        if value == '' or math.isnan(value): 
            return 0.0 
        else: 
            return value
    
