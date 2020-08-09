import pandas as pd
import numpy as np

import datetime
import math


df=pd.read_excel(r'Schedule.xlsx')
print("The first 10 rows are \n")
for i in range(10):
   print (df.values[i],"\n")
print("The dates are")
print(df['Date'])

date_string=input("Enter starting date time(inclusive) as %Y-%m-%d %H:%M:%S")
#date_string = "2020-07-15 00:00:00"

date1 = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

date_string=input("Enter ending date time(exclusive) as %Y-%m-%d %H:%M:%S")
#date_string = "2020-07-17 00:00:00"

date2 = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
dur=0;
i=0;temp=i;no_of_days=0;
while(date1!=df.values[i][0]):
  i=i+1;temp=i;
while(date2!=df.values[i][0]):
  i=i+1;
  if(df.values[i][3]=="studies" or df.values[i][3]=="Studies"):
      t1=df.values[i][2];t2=df.values[i][1]
      #print(t1," ",t2)
      t1_mins=t1.hour*60+t1.minute
      t2_mins=t2.hour*60+t2.minute
      dur=dur+t1_mins-t2_mins

  if(pd.isnull(df.values[i-1][0])):             #pd.isnull returns true for null and nat
    print("NaT")
  else:
      no_of_days=no_of_days+1;
print("no of days are: ",no_of_days)
  

study_hrs=math.floor(dur/60);study_mins=dur%60;
print("Total duration of studies during chosen period is ",study_hrs, "hrs and ",study_mins," mins.")
avg=dur/(no_of_days);
avg_study_hrs=math.floor(avg/60);avg_study_mins=avg%60;
print("Average time studied everyday during the choosen period is",avg_study_hrs, "hrs and ",avg_study_mins," mins.")
