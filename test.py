import time
import serial

day = time.ctime()
day = day.split()
weekday, month, date, year = day[0], day[1], day[2], day[4]
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def getTime():
    t = time.ctime()
    t = t.split()
    t = t[3]
    return t

arduino.reset_input_buffer()

while True:
    TimeOfRecord = {}
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').rstrip()
        current_time = getTime()

