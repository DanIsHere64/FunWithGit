import time
import serial
import pandas as pd

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
arduino.reset_input_buffer()

liveData = pd.read_csv("liveData.csv", encoding='utf-8')
historicData = pd.read_csv("historicData.csv", encoding='utf-8')
hourlyData = pd.read_csv("hourlyData.csv", encoding='utf-8')
dailyData = pd.read_csv("dailyData.csv", encoding='utf-8')

def getTime():
    time.strftime("%H:%M:%S", time.localtime())

def getDay():
    time.strftime("%x", time.localtime())

while True:
    if time.strftime("%M", time.localtime()) % 5 == 0:
        avgTemp = liveData.iloc[liveData.count()-60:, 2].mean()

    if arduino.in_waiting > 0 and time.strftime("%S", time.localtime()) % 5 == 0:
        data = arduino.readline().decode('utf-8').rstrip()
        temp, sal, pH = data.split(",")
        current_time = getTime()

        liveData["timeStamp"].append(current_time)
        liveData["temp"].append(temp)
        liveData["sal"].append(sal)
        liveData["pH"].append(pH)
        print(dailyData)
