import pandas as pd

import datetime

df=pd.read_excel(r'Schedule.xlsx')
#print(df)
print("The first 10 rows are \n")
for i in range(10):
   print (df.values[i],"\n")
print("The dates are")
print(df['Date'])
print("Please enter Starting date \n")
year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
date1 = datetime.date(year, month, day)

print("Please enter Ending date \n")
year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
date2 = datetime.date(year, month, day)
