from datetime import datetime as dt

class util():
    def __init__(self):
        pass

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

    def getDateTimeByDayAndTime(self, dayGame, timeGame):

        #  Tue, Oct 18, 2022   7:30p
        dayGameRemoved = dayGame.replace(",","")
        splitted = dayGameRemoved.split(" ")
        #startTimeSplitted = startTime[:-1].split(":")

        year = int(splitted[3])
        month = self.getMonthByAbreviation(splitted[1])
        #day = int(splitted[2][:-1])
        day = int(splitted[2])
        
        time = timeGame.split(":")
        hour = 12 + int(time[0])
        minutes = int(time[1][:-1])

        if hour == 24:
            hour = 0

        return dt(year, month, day, hour, minutes, 0, 0)
