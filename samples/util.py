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

    def getDateTimeByDayAndTime(self, dayGame, startTime):

        dayGameSplitted = dayGame.split(" ")
        startTimeSplitted = startTime.split(":")

        year = int(dayGameSplitted[3])
        month = self.getMonthByAbreviation(dayGameSplitted[1])
        day = int(dayGameSplitted[2][:-1])
        hour = int(startTimeSplitted[0])
        minutes = int(startTimeSplitted[1][:-2])

        if startTimeSplitted[1][2:] == "pm":
            hour += 12

        return dt(year, month, day, hour, minutes, 0, 0)
