import pandas as pd 
import matplotlib.pyplot as mp 

data1 = pd.read_csv('SampleData.csv')
data2 = pd.read_csv('ReferenceData.csv')

y1 = data1['IMU[0].AccX']
y2 = data2['IMU[0].AccX']

x1 = data1['timestamp(ms)']
x2 = data2['timestamp(ms)']

mp.figure(figsize=(20,10))
mp.plot(x1,y1,'r-',label='1st Graph')
mp.plot(x2,y2,'b-',label='2nd Graph')
mp.xlabel('TimeStamp(s)')
mp.ylabel('IMU[0]AccX')
mp.grid(True)
mp.show()
