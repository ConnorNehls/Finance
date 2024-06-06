import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

sp = yf.download('SPY', period="max")
sp_change = []
dates = []
for index, row in sp.iterrows():
    sp_change.append(row['Close'] - row['Open'])
    dates.append(index)
    if index.day == 24 and index.year == 2022 and index.month == 2:
        print(row)
        print(row['Close'])
        print(row['Open'])

curr_yr = 1993
change_sum = 0
yr_change = []
yrs = [curr_yr]
for idx, x in enumerate(sp_change):
    if dates[idx].year != curr_yr:
        if curr_yr!= 1993:
            yrs.append(curr_yr)
        yr_change.append(change_sum)
        change_sum = 0
        curr_yr = dates[idx].year
    change_sum += x

print(yr_change)
print(yrs)
    
    
    
##dates = np.arange(dates)
##sp = np.arange(sp_percent_change)
#print(dates)
        
##plt.scatter(dates, sp_change)
##plt.ylabel('Stock Price Change')
##plt.xlabel('Time(days)')
##plt.title('Stock Price Change by Day')
##plt.show()

plt.scatter(yrs, yr_change)
plt.ylabel('Stock Price Change')
plt.xlabel('Time(years)')

plt.show()


#print(sp_percent_change)
    



