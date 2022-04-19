import pandas as pd

livePath = "/Users/cosmi/Documents/Code/FunWithGit/CSC-132/SMaRRT_Tank/liveData.csv"
liveData = pd.read_csv(livePath, encoding='utf-8')
historicPath = "/Users/cosmi/Documents/Code/FunWithGit/CSC-132/SMaRRT_Tank/historicalData.csv"
historicData = pd.read_csv(historicPath, encoding='utf-8')
hourlyPath = "/Users/cosmi/Documents/Code/FunWithGit/CSC-132/SMaRRT_Tank/hourlyData.csv"
hourlyData = pd.read_csv(hourlyPath, encoding='utf-8')
dailyPath = "/Users/cosmi/Documents/Code/FunWithGit/CSC-132/SMaRRT_Tank/dailyData.csv"
dailyData = pd.read_csv(dailyPath, encoding='utf-8')

print(f"This is the live data:\n{liveData}")
print(f"This is the historical data:\n{historicData}")
print(f"This is the hourly data:\n{hourlyData}")
print(f"This is the daily data:\n{dailyData}")