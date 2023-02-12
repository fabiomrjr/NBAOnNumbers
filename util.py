from datetime import datetime as dt

class util():
    def __init__(self):
        pass

    def getMonthByAbreviation(self, month):

        switcher = {
            "Jan": 1,
            "Fev": 2,
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

    def getDateTimeByDayAndTime(self, dayTimeGame):

        #  Tue, Oct 18, 2022   7:30p
        dayGameRemoved = dayTimeGame.replace(",","")
        splitted = dayGameRemoved.split(" ")
        #startTimeSplitted = startTime[:-1].split(":")

        year = int(splitted[3])
        month = self.getMonthByAbreviation(splitted[1])
        #day = int(splitted[2][:-1])
        day = int(splitted[2])
        
        time = dayTimeGame.split(":")
        hour = int(time[0])
        minutes = int(time[1][:-1])

        #if startTimeSplitted[1][2:] == "pm":
        #    hour += 12

        return dt(year, month, day, hour, minutes, 0, 0)
