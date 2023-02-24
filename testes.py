import pandas as pd
from datetime import datetime as dt

d1 = dt(2022,3,10)
print(d1) 

data1 = {
  "age": [16, 14, 10],
  "qualified": [2,1,2]
}
df1 = pd.DataFrame(data1)

data2 = {
  "age": [55, 40],
  "qualified": [1,2]
}
df2 = pd.DataFrame(data2)

a = [77, 3]
#b = ["t" , "g"]

#c = [a, b]
#print(c)

newdf = df1.append(df2)
newdf.loc[len(newdf)] = a
print(newdf)