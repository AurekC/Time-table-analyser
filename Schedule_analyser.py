import pandas as pd

df=pd.read_excel(r'Schedule.xlsx')
print(df)
print("The first row is \n")
print (df.values[0])
print("The dates are")
print(df['Date'])
