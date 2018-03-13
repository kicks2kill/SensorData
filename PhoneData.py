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


number = df.values


light = column(number, LIGHT)
time = column(number, TIME)

#I want to pass each dataset as a frame, to be able to access the values present in the column index.
#Ensure that the lighting is dim
def is_dim(frame):
    return (frame[LIGHT] < 100)

#ensure if the phone is in our phone or outside of our pocket
def is_moving(frame):
    return (frame[LINEAR_ACCEL_X] + (frame[LINEAR_ACCEL_Y])) > 1
#60 decibels is average volume
def is_audible(frame):
    return frame[SOUND] > 60

#foreach frame in the dt.values, if light < 100 then put that into a frame
low_light =[frame for frame in number if is_dim(frame)]


pocket = [frame for frame in low_light if is_moving(frame)]

noise = [frame for frame in pocket if is_audible(frame)]

print("There are" + str(len(low_light)) + "frames with dim lighting")


movement_time = []
for frame in number:
    movement_time.append((abs(frame[LINEAR_ACCEL_X]) + abs(frame[LINEAR_ACCEL_Y])))

# plt.plot(time,movement_time)
# plt.title("Toal movement vs time.")
# plt.show()
# print(plt)




# plt.plot(time, column(number, LIGHT))
# plt.title("Light level vs Time")
# plt.show()
# print(plt)

#shape up the rows/columns for ease of viewing(of the csv)
row = df.shape[0] 
col = df.shape[1]
out_png = 'MovementVsTime.png'
#export as a png
plt.savefig(out_png, dpi=150)
#save the pyplot as a png






