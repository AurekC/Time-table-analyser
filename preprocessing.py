import pandas as pd
import numpy as np
import datetime
import math

f_log=open("preprocessing.txt","w")
df=pd.read_excel(r'Schedule.xlsx')

date_string=input("Enter starting date time(inclusive) as %Y-%m-%d")
date_string+=" 00:00:00"
#date_string = "2020-07-15 00:00:00"
date1 = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

date_string=input("Enter ending date time(exclusive) as %Y-%m-%d")
date_string+=" 00:00:00"
#date_string = "2020-07-20 00:00:00"
date2 = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

text=["The The starting date is ",str(date1)," and the ending date is ",str(date2)]
f_log.writelines(text)


i=0;no_of_days=0;
while(date1!=df.values[i][0]):
  i=i+1;
while(date2!=df.values[i][0]):
  i=i+1;
  if(pd.isnull(df.values[i-1][0])):             #pd.isnull returns true for null and nat
   try:
    t1=df.values[i][2];t2=df.values[i][1]
    t1_mins=t1.hour*60+t1.minute
    t2_mins=t2.hour*60+t2.minute
    dur=t1_mins-t2_mins
    if(dur<0):
        #if(df.values[i][4]!="pubg"):
           #print("The duration is neagtive for row number: ",str(i+1))
           text=["The duration is neagtive for row number: ",str(i+1),"\n"]
           f_log.writelines(text)
           set_date=datetime.date(1,1,1)
           ampm_var=datetime.time(12,0,0)
           datetime1 = datetime.datetime.combine(set_date, t1)
           datetime2 = datetime.datetime.combine(set_date, ampm_var)
           time_elapsed = datetime1 - datetime2
           df.values[i][2]=time_elapsed;
        #else:
            #zz=0; #do nothing as of now. To be edited later
   except:
        print("error at ",str(i+1))
        text=["error at ",str(i+1),"\n"]
        f_log.writelines(text)
 
df.to_excel(r'Corrected_schedule.xlsx', index= False)
