import csv
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#I generated constants to make it easier to access the columns within the spread sheet
ACCELEROMETER_X = 0
LIGHT  = 13
GRAVITY_Y  = 5
LINEAR_ACCEL_X =  7
LINEAR_ACCEL_Y = 8
TIME = 31
SOUND = 21
LATITUDE = 22
LONGITUDE = 23
PRESSURE = 20

#read from the csv file and wrap it in pandas
df = pd.read_csv("androsense.csv.csv",skiprows=1, sep=";")

#iterate through each column, for that item within range(len) append the index
#to the list, then return
def column(arr,lst):
    ret = []
    for i in range(0, len(arr)):
        ret.append(arr[i][lst])
    return ret

   #generate our columns for use 
GravCol = column(df.values,ACCELEROMETER_X)
LightCol = column(df.values,LIGHT)
TimeCol = column(df.values,TIME)
LinearX = column(df.values,LINEAR_ACCEL_X)
AccelX = column(df.values,ACCELEROMETER_X)
LinearY = column(df.values,LINEAR_ACCEL_Y)
Sound = column(df.values,SOUND)
Latitude = column(df.values,LATITUDE)
Longitude = column(df.values,LONGITUDE)
Pressure = column(df.values,PRESSURE)

#as long as our gravity is not 0, display the linearY 
if(GravCol != 0):
    plt.plot(GravCol)
    plt.plot(LinearY)
    plt.xlabel('GravCol')
    plt.ylabel('LinearY')
    plt.show()
    print(plt)


##As long as our light is 1 or greater, we know that the phone was not within a pocket.
LightCol.sort()
if(LightCol.count(1)):
    plt.plot(LightCol)
    plt.plot(AccelX)
    
# plt.plot(Sound)
# plt.plot(Latitude)
#plt.plot(Longitude)
# plt.plot(Pressure)

#plt.plot(TimeCol) 
#plt.plot(LinearX)





#shape up the rows/columns for ease of viewing(of the csv)
row = df.shape[0] 
col = df.shape[1]
out_png = 'Yup.png'
#export as a png
plt.savefig(out_png, dpi=150)
#save the pyplot as a png






