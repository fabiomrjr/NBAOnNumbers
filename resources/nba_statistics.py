import pandas as pd
from datetime import datetime as dt
from sympy import symbols, Eq, solve

class nbaStatistics():
    def __init__(self):
        pass
    
    def prepareTeamsData(self, dfgames):
        d = {'name':['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers', 'Toronto Raptors',
                        'Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers', 'Milwaukee Bucks',
                        'Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic', 'Washington Wizards',
                        'Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder', 'Portland Trail Blazers', 'Utah Jazz',
                        'Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns', 'Sacramento Kings',
                        'Dallas Mavericks', 'Houston Rockets', 'Memphis Grizzlies', 'New Orleans Pelicans', 'San Antonio Spurs'], 
            'record':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            'jogos':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}      

        df = pd.DataFrame(d)

        for index, row in dfgames.iterrows():
            if row['winner'] == "HOME":
                df.loc[df.name == row['visitor'], 'record'] = df.loc[df.name == row['visitor'], 'record'] - 1
                df.loc[df.name == row['home'], 'record'] = df.loc[df.name == row['home'], 'record'] + 1
            elif row['winner'] == "VISIT":
                df.loc[df.name == row['home'], 'record'] = df.loc[df.name == row['home'], 'record'] - 1
                df.loc[df.name == row['visitor'], 'record'] = df.loc[df.name == row['visitor'], 'record'] + 1
            
            df.loc[df.name == row['home'], 'jogos'] = df.loc[df.name == row['home'], 'jogos'] + 1
            df.loc[df.name == row['visitor'], 'jogos'] = df.loc[df.name == row['visitor'], 'jogos'] + 1

        return df

    def nbaRank(self, df):
    
        #(R_Bruins, R_MapleLeafs, R_Lightning, R_Sabres, R_Panthers, R_Senators, R_RedWings, R_Canadiens, R_Hurricanes, R_Devils, R_Rangers, R_Islanders, R_Penguins,
        #R_Capitals, R_Flyers, R_BlueJackets, R_Stars, R_Wild, R_Avalanche, R_Jets, R_Predators, R_Blues, R_Coyotes, R_Blackhawks, R_Knights, R_Kings, R_Kraken, R_Oilers,
        #R_Flames, R_Canucks, R_Sharks, R_Ducks)
        (Boston_Celtics, Brooklyn_Nets, New_York_Knicks, Philadelphia_76ers, Toronto_Raptors, Chicago_Bulls, Cleveland_Cavaliers, 
        Detroit_Pistons, Indiana_Pacers, Milwaukee_Bucks, Atlanta_Hawks, Charlotte_Hornets, Miami_Heat, Orlando_Magic, Washington_Wizards, 
        Denver_Nuggets, Minnesota_Timberwolves, Oklahoma_City_Thunder, Portland_Trail_Blazers, Utah_Jazz, Golden_State_Warriors, Los_Angeles_Clippers, 
        Los_Angeles_Lakers, Phoenix_Suns, Sacramento_Kings, Dallas_Mavericks, Houston_Rockets, Memphis_Grizzlies, New_Orleans_Pelicans, San_Antonio_Spurs) = symbols(
            'Boston_Celtics Brooklyn_Nets New_York_Knicks Philadelphia_76ers Toronto_Raptors Chicago_Bulls Cleveland_Cavaliers Detroit_Pistons Indiana_Pacers \
            Milwaukee_Bucks Atlanta_Hawks Charlotte_Hornets Miami_Heat Orlando_Magic Washington_Wizards Denver_Nuggets Minnesota_Timberwolves Oklahoma_City_Thunder \
            Portland_Trail_Blazers Utah_Jazz Golden_State_Warriors Los_Angeles_Clippers Los_Angeles_Lakers Phoenix_Suns Sacramento_Kings Dallas_Mavericks Houston_Rockets \
            Memphis_Grizzlies New_Orleans_Pelicans San_Antonio_Spurs')

        eq1 = Eq(float(df.loc[df.name == 'Boston Celtics', 'record']) + float((1/df.loc[df.name == 'Boston Celtics', 'jogos'])) * 
                    (Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + 
                    Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq2 = Eq(float(df.loc[df.name == 'Brooklyn Nets', 'record']) + float((1/df.loc[df.name == 'Brooklyn Nets', 'jogos'])) * 
                    (Boston_Celtics + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + 
                    Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq3 = Eq(float(df.loc[df.name == 'New York Knicks', 'record']) + float((1/df.loc[df.name == 'New York Knicks', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + 
                    Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq4 = Eq(float(df.loc[df.name == 'Philadelphia 76ers', 'record']) + float((1/df.loc[df.name == 'Philadelphia 76ers', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + 
                    Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq5 = Eq(float(df.loc[df.name == 'Toronto Raptors', 'record']) + float((1/df.loc[df.name == 'Toronto Raptors', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + 
                    Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))

        eq6 = Eq(float(df.loc[df.name == 'Chicago Bulls', 'record']) + float((1/df.loc[df.name == 'Chicago Bulls', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq7 = Eq(float(df.loc[df.name == 'Cleveland Cavaliers', 'record']) + float((1/df.loc[df.name == 'Cleveland Cavaliers', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Detroit_Pistons + Indiana_Pacers + Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq8 = Eq(float(df.loc[df.name == 'Detroit Pistons', 'record']) + float((1/df.loc[df.name == 'Detroit Pistons', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Indiana_Pacers + Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq9 = Eq(float(df.loc[df.name == 'Indiana Pacers', 'record']) + float((1/df.loc[df.name == 'Indiana Pacers', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq10 = Eq(float(df.loc[df.name == 'Milwaukee Bucks', 'record']) + float((1/df.loc[df.name == 'Milwaukee Bucks', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))

        eq11 = Eq(float(df.loc[df.name == 'Atlanta Hawks', 'record']) + float((1/df.loc[df.name == 'Atlanta Hawks', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq12 = Eq(float(df.loc[df.name == 'Charlotte Hornets', 'record']) + float((1/df.loc[df.name == 'Charlotte Hornets', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq13 = Eq(float(df.loc[df.name == 'Miami Heat', 'record']) + float((1/df.loc[df.name == 'Miami Heat', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq14 = Eq(float(df.loc[df.name == 'Orlando Magic', 'record']) + float((1/df.loc[df.name == 'Orlando Magic', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq15 = Eq(float(df.loc[df.name == 'Washington Wizards', 'record']) + float((1/df.loc[df.name == 'Washington Wizards', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))


        eq16 = Eq(float(df.loc[df.name == 'Denver Nuggets', 'record']) + float((1/df.loc[df.name == 'Denver Nuggets', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Minnesota_Timberwolves + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq17 = Eq(float(df.loc[df.name == 'Minnesota Timberwolves', 'record']) + float((1/df.loc[df.name == 'Minnesota Timberwolves', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Oklahoma_City_Thunder + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq18 = Eq(float(df.loc[df.name == 'Oklahoma City Thunder', 'record']) + float((1/df.loc[df.name == 'Oklahoma City Thunder', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq19 = Eq(float(df.loc[df.name == 'Portland Trail Blazers', 'record']) + float((1/df.loc[df.name == 'Portland Trail Blazers', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq20 = Eq(float(df.loc[df.name == 'Utah Jazz', 'record']) + float((1/df.loc[df.name == 'Utah Jazz', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))

        eq21 = Eq(float(df.loc[df.name == 'Golden State Warriors', 'record']) + float((1/df.loc[df.name == 'Golden State Warriors', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq22 = Eq(float(df.loc[df.name == 'Los Angeles Clippers', 'record']) + float((1/df.loc[df.name == 'Los Angeles Clippers', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq23 = Eq(float(df.loc[df.name == 'Los Angeles Lakers', 'record']) + float((1/df.loc[df.name == 'Los Angeles Lakers', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq24 = Eq(float(df.loc[df.name == 'Phoenix Suns', 'record']) + float((1/df.loc[df.name == 'Phoenix Suns', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq25 = Eq(float(df.loc[df.name == 'Sacramento Kings', 'record']) + float((1/df.loc[df.name == 'Sacramento Kings', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Dallas_Mavericks + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))

        eq26 = Eq(float(df.loc[df.name == 'Dallas Mavericks', 'record']) + float((1/df.loc[df.name == 'Dallas Mavericks', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Houston_Rockets + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq27 = Eq(float(df.loc[df.name == 'Houston Rockets', 'record']) + float((1/df.loc[df.name == 'Houston Rockets', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Memphis_Grizzlies + New_Orleans_Pelicans + San_Antonio_Spurs))
        eq28 = Eq(float(df.loc[df.name == 'Memphis Grizzlies', 'record']) + float((1/df.loc[df.name == 'Memphis Grizzlies', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + 
                    New_Orleans_Pelicans + San_Antonio_Spurs))
        eq29 = Eq(float(df.loc[df.name == 'New Orleans Pelicans', 'record']) + float((1/df.loc[df.name == 'New Orleans Pelicans', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + 
                    Memphis_Grizzlies + San_Antonio_Spurs))
        eq30 = Eq(float(df.loc[df.name == 'San Antonio Spurs', 'record']) + float((1/df.loc[df.name == 'San Antonio Spurs', 'jogos'])) * 
                    (Boston_Celtics + Brooklyn_Nets + New_York_Knicks + Philadelphia_76ers + Toronto_Raptors + Chicago_Bulls + Cleveland_Cavaliers + Detroit_Pistons + Indiana_Pacers + 
                    Milwaukee_Bucks + Atlanta_Hawks + Charlotte_Hornets + Miami_Heat + Orlando_Magic + Washington_Wizards + Denver_Nuggets + Minnesota_Timberwolves + Oklahoma_City_Thunder + 
                    Portland_Trail_Blazers + Utah_Jazz + Golden_State_Warriors + Los_Angeles_Clippers + Los_Angeles_Lakers + Phoenix_Suns + Sacramento_Kings + Dallas_Mavericks + Houston_Rockets + 
                    Memphis_Grizzlies + New_Orleans_Pelicans))


        sol = solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12, eq13, eq14, eq15, eq16,
                        eq17, eq18, eq19, eq20, eq21, eq22, eq23, eq24, eq25, eq26, eq27, eq28, eq29, eq30),
                    (Boston_Celtics, Brooklyn_Nets, New_York_Knicks, Philadelphia_76ers, Toronto_Raptors, Chicago_Bulls, Cleveland_Cavaliers, 
                    Detroit_Pistons, Indiana_Pacers, Milwaukee_Bucks, Atlanta_Hawks, Charlotte_Hornets, Miami_Heat, Orlando_Magic, Washington_Wizards, 
                    Denver_Nuggets, Minnesota_Timberwolves, Oklahoma_City_Thunder, Portland_Trail_Blazers, Utah_Jazz, Golden_State_Warriors, Los_Angeles_Clippers, 
                    Los_Angeles_Lakers, Phoenix_Suns, Sacramento_Kings, Dallas_Mavericks, Houston_Rockets, Memphis_Grizzlies, New_Orleans_Pelicans, San_Antonio_Spurs))
        
        d={'teamName': ['Boston Celtics', 'Brooklyn Nets', 'New York Knicks', 'Philadelphia 76ers', 'Toronto Raptors', 'Chicago Bulls', 'Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers', \
                        'Milwaukee Bucks', 'Atlanta Hawks', 'Charlotte Hornets', 'Miami Heat', 'Orlando Magic', 'Washington Wizards', 'Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder', \
                        'Portland Trail Blazers', 'Utah Jazz', 'Golden State Warriors', 'Los Angeles Clippers', 'Los Angeles Lakers', 'Phoenix Suns', 'Sacramento Kings', 'Dallas Mavericks', 'Houston Rockets', \
                        'Memphis Grizzlies', 'New Orleans Pelicans', 'San Antonio Spurs'],
           'teamRank': [sol[Boston_Celtics], sol[Brooklyn_Nets], sol[New_York_Knicks], sol[Philadelphia_76ers], sol[Toronto_Raptors], sol[Chicago_Bulls], sol[Cleveland_Cavaliers],
                        sol[Detroit_Pistons], sol[Indiana_Pacers], sol[Milwaukee_Bucks], sol[Atlanta_Hawks], sol[Charlotte_Hornets], sol[Miami_Heat], sol[Orlando_Magic],
                        sol[Washington_Wizards], sol[Denver_Nuggets], sol[Minnesota_Timberwolves], sol[Oklahoma_City_Thunder], sol[Portland_Trail_Blazers], sol[Utah_Jazz],
                        sol[Golden_State_Warriors], sol[Los_Angeles_Clippers], sol[Los_Angeles_Lakers], sol[Phoenix_Suns], sol[Sacramento_Kings], sol[Dallas_Mavericks], sol[Houston_Rockets], 
                        sol[Memphis_Grizzlies], sol[New_Orleans_Pelicans], sol[San_Antonio_Spurs]]}
        
        return pd.DataFrame(d)