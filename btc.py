import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from random import choice
import quandl
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

quandl.ApiConfig.api_key = "cA7YzGVpFRnzCEThcyrZ"
data = quandl.get("Bitstamp/USD", start_date="2017-06-01", end_date="2017-09-23")

dates = []

for i in data.Last.index:
    dates.append(i)


xvalues = dates
yvalues = data.Last

data['Lastmean'] = pd.rolling_mean(data['Last'], 7)
data[['Last', 'Lastmean']].plot(ax=ax1)

plt.show()

#plt.scatter(dates, data['Last'])
