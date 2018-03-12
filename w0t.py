import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("androsense.csv",skiprows=1, sep=";")
#df.reindex(axis="columns",fill_value='|)

print(df)

row = df.shape[0] 
col = df.shape[1]
#Dataframe is df, it holds the variable reference as a list
#shape represents the dimensonality of the dataframe
plt.plot(df.iloc[:,col-2]) 
#plot the graph out
plt.ylabel('yuh')
plt.xlabel('idk')
out_png = 'time2.png'
#export as a png
plt.savefig(out_png, dpi=150)
#save the pyplot as a png