# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:15:51 2021

@author: sosum
"""
import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data
#print(london_data.head())
print(london_data.iloc[100:200])
print(len(london_data))
temp=london_data.TemperatureC
average_temp=temp.mean()
# the variance of the temperature of the data
temperature_var=np.var(temp)
print(temperature_var)

#The Standard Deviation of the Temperature
temperature_standard_deviation=np.std(temp)
print(temperature_standard_deviation)
# the variance and standard deviation is the same, the only difference is the variance is the squares of the standard deviation.
print(london_data.head()) 
june=london_data.loc[london_data['month']==6]['TemperatureC']
july=london_data.loc[london_data['month']==7]['TemperatureC']
print("The mean of the June: "+ str(np.mean(june)))
print("The mean of Jult is: "+ str(np.mean(july)))
print("The Standard deviation of June: "+ str(np.std(june)))
print("The Standard Deviation of July: "+ str(np.std(july)))

# Exploring all month mean and standard deviation 
for i in range(1,13):
  month=london_data.loc[london_data['month']==i]["TemperatureC"]
  print("The mean temperature in month "+ str(i) + ' is '+ str(np.mean(np.mean(month))))
  print("Standard deviation of temperature in month "+str(i)+' is '+ str(np.std(month))+'\n')

for i in range(1,13):
  month=london_data.loc[london_data['month']==i]["Humidity"]
  print("The mean Humidity in month "+ str(i) + ' is '+ str(np.mean(np.mean(month))))
  print("Standard deviation of Humidity in month "+str(i)+' is '+ str(np.std(month))+'\n')

