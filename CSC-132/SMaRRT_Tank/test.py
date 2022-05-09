import time
import serial
import pandas as pd
from math import *
from random import *

liveData = pd.read_csv("liveData.csv", encoding='utf-8')

liveData['unixTime'] = liveData['unixTime'].astype(int)
liveData['temp'] = liveData['temp'].astype(float)
liveData['sal'] = liveData['sal'].astype(int)
liveData['pH'] = liveData['pH'].astype(float)
liveData = liveData.set_index('unixTime', drop=False)

df = {
    "unixTime": [],
    "temp": [],
    "sal": [],
    "pH": []
}
df = pd.DataFrame(df)

earliestTime = liveData.iloc[0,0]

for i in range(24):
    stuff = {
        "unixTime": [earliestTime + i * 3600],
        "temp": [round(liveData.loc[earliestTime + i * 3600:(earliestTime + (i + 1) * 3600) - 5, 'temp'].mean(), 1)],
        "sal": [round(liveData.loc[earliestTime + i * 3600:(earliestTime + (i + 1) * 3600) - 5, 'sal'].mean())],
        "pH": [round(liveData.loc[earliestTime + i * 3600:(earliestTime + (i + 1) * 3600) - 5, 'pH'].mean(), 2)]
    }
    data = pd.DataFrame(stuff)
    df = pd.concat([df, data], ignore_index=True)

df = df.set_index('unixTime')


print(df)
#df.to_csv('hourlyData.csv', index=True)