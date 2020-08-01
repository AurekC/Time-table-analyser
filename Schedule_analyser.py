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

#print("Please enter Ending date \n")
#year = int(input('Enter a year'))
#month = int(input('Enter a month'))
#day = int(input('Enter a day'))
#date2 = datetime.date(year, month, day)
#date1=date1.timetuple()
#print(df.values[0][0])
date_string=input("Enter string date time as %Y-%m-%d %H:%M:%S")
#date_string = "2020-07-15 00:00:00"

date1 = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

date_string=input("Enter string date time as %Y-%m-%d %H:%M:%S")
#date_string = "2020-07-15 00:00:00"

date2 = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")


#timestamp = datetime.datetime.timestamp(date)

#print(date1,df.values[0][0])
i=0;flag=0;
while(date1!=df.values[i][0]):
  i=i+1;
while(date2!=df.values[i][0]):
  i=i+1;
  if(flag==0):
   if(df.values[i][3]=="studies" or df.values[i][3]=="Studies"):
     dur=df.values[i][2]-df.values[i][1]
  else:
    if(df.values[i][3]=="studies" or df.values[i][3]=="Studies"):
      dur=dur+df.values[i][2]-df.values[i][1]
print("Total duration of studies during chosen period is ",dur);
