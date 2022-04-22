import time
import serial
import pandas as pd
from math import trunc
from math import remainder

liveData = pd.read_csv("liveData.csv")

historicData = {
    "day": [],
    "time": [],
    "temp": [],
    "salinity": [],
    "pH": []
}

for i in range(0, 120):
    historicData['day'].append(liveData.iloc[i*6,0])
    historicData['time'].append(liveData.iloc[i*6,1])
    historicData['temp'].append(trunc(liveData.iloc[i*6:(i+1)*6,2].mean()))
    historicData['salinity'].append(trunc(liveData.iloc[i*6:(i+1)*6,3].mean()))
    historicData['pH'].append(liveData.iloc[i*6:(i+1)*6,4].mean()-remainder(liveData.iloc[i*6:(i+1)*6,4].mean(), 0.01))

dataFrame = pd.DataFrame(historicData)
print(dataFrame)
dataFrame.to_csv('historicalData.csv')