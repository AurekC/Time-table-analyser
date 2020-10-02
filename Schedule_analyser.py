import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import datetime
import math


def cal_avg(category,no_of_days):
    x=[];y=[];sum=0;                        # sum calculates y value for plotting for every x
    dur=0;
    eff=0;count_studies_not=0; x1=[];y1=[];sum1=0;  #variable to calculate efficiency and count for counting number of times studies
    i=0;temp=i;
    while(date1!=df.values[i][0]):
      i=i+1;temp=i;
    while(date2!=df.values[i][0]):
      i=i+1;
      if(pd.isnull(df.values[i-1][0])):             #pd.isnull returns true for null and nat
        zz=0;#print("NaT")          #do nothing statement
      else:
          x.append(str(df.values[i-1][0]))
          y.append(sum)
          sum=0;
          if(category.lower()=="studies" or category.lower()=="studies work"):
           sum1=0;
           x1.append(str(df.values[i-1][0]))
           y1.append(sum1)

      if(df.values[i][3].lower()==category.lower() or df.values[i][3].lower()=="college class "+" "+category.lower() or df.values[i][3].lower()=="college lab "+" "+category.lower()):
          t1=df.values[i][2];t2=df.values[i][1]
          t1_mins=t1.hour*60+t1.minute
          t2_mins=t2.hour*60+t2.minute
          dur=dur+t1_mins-t2_mins
          sum+=t1_mins-t2_mins
      if(category.lower()=="studies" or category.lower()=="studies work"):
          #calculating efficiency avg
          if(pd.isnull(df.values[i-1][5]) or df.values[i-1][5]=="N.A."):             #pd.isnull returns true for null and nat
            zz=0;#print("NaT")          #do nothing statement
          else:
            try:
                eff+=df.values[i-1][5]
                count_studies_not+=1
                sum1+=eff;
            except:
                print("error reading efficiency value at ",i,"th row")
                print("Ignored efficiency value of this row")





    dur_hrs=math.floor(dur/60);dur_mins=dur%60;
    print("\nTotal duration of ",category," during chosen period is ",dur_hrs, "hrs and ",dur_mins," mins.")
    avg=dur/(no_of_days);
    avg_dur_hrs=math.floor(avg/60);avg_dur_mins=avg%60;
    print("Average time spend everyday on ",category, " during the choosen period is",avg_dur_hrs, "hrs and ",avg_dur_mins," mins.")

    plt.plot(x,y, label='linear')
    plt.savefig(category+".pdf")
    plt.show()

    if(category.lower()=="studies" or category.lower()=="studies work"):
        avg_eff=0;
        avg_eff=eff/count_studies_not
        print("The average efficeincy for ",category," is ", avg_eff)
        plt.plot(x1,y1, label='linear')
        plt.savefig(category+" efficiency"+".pdf")
        plt.show()


#end of function

f_log=open("log.txt","w")

userchoice=int(input("Enter 1 for reading Schedule.xlsx \nEnter 2 for reading Corrected_schedule.xlsx"))
if(userchoice==1):
    df=pd.read_excel(r'Schedule.xlsx')
else:
    df=pd.read_excel(r'Corrected_schedule.xlsx')
Log_Lines=["The first 10 rows are \n"]
f_log.writelines(Log_Lines)
for i in range(10):
   Log_Lines=[str(df.values[i]),"\n"]
   f_log.writelines(Log_Lines)
Log_Lines=["The dates are",str(df['Date'])]
f_log.writelines(Log_Lines)

date_string=input("Enter starting date time(inclusive) as %Y-%m-%d")
date_string+=" 00:00:00"
#date_string = "2020-07-15 00:00:00"
date1 = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

date_string=input("Enter ending date time(exclusive) as %Y-%m-%d")
date_string+=" 00:00:00"
#date_string = "2020-07-20 00:00:00"
date2 = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

i=0;no_of_days=0;
while(date1!=df.values[i][0]):
  i=i+1;
while(date2!=df.values[i][0]):
  i=i+1;
  if(pd.isnull(df.values[i-1][0])):             #pd.isnull returns true for null and nat
    zz=0;#print("NaT")          #do nothing statement
  else:
      no_of_days=no_of_days+1;
print("no of days are: ",no_of_days)
cal_avg("Studies work",no_of_days)
cal_avg("Entertainment",no_of_days)
cal_avg("Non useful work",no_of_days)
cal_avg("Others",no_of_days)
cal_avg("Studies",no_of_days)

f_log.close()
