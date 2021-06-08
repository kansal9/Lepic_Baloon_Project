# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 19:21:50 2018

@author: vanshika
"""

import matplotlib.pyplot as plt
import math 
import csv


acc_x = []
acc_y = []
acc_z = []
acc =[]
Acc = []
Bar = []
Temp = []
Temp_bias =1.25
Bar_bias = 0.03
bar_temp = [] ## celcius
bar_pres = [] ## Hect Pascal
time = []
temp = []
m = 0
with open("Resuts.csv") as csvfile:
    av = csv.reader(csvfile, dialect = 'excel')
    for row in av:
        Bar.append(row [0])
        Temp.append( (row[1]))
        Acc.append(row[2])
        time.append(m)
        m=m+1

Acc = str(Acc).replace('[','').replace(']','').replace(',','')
Acc = Acc.split()
Acc = [i.replace("'", "") for i in Acc] 

j=0
m=0
for j in range(0, len(Acc),3):
    Acc[j].replace("'","")
    acc_x.append(float (Acc[j]))
    acc_y.append(float (Acc[j+1]))
    acc_z.append(float (Acc[j+2]))
    acc.append(math.sqrt(acc_x[m]**2+acc_y[m]**2+acc_z[m]**2))
    m=m+1

j=0
Bar = str(Bar).replace('[','').replace(']','').replace(',','')
Bar = Bar.split()
Bar = [i.replace("'", "") for i in Bar] 
for j in range(0,len(Bar),2): 
    bar_temp.append(float (Bar[j]))
    bar_pres.append((float (Bar[j+1]))-Bar_bias)
j=0
Temp = str(Temp).replace('[','').replace(']','').replace(',','')
Temp = Temp.split()
Temp = [i.replace("'", '') for i in Temp] 

#for j in range (len(Temp)):
#    Temp = float (Temp[j])


#==============================================================================
#==============================================================================
plt.figure()
plt.title ('Acc Vs Time')
#plt.plot(time,acc_y,'r')
plt.plot(time, acc_x, 'r', time, acc_y, 'g', time, acc_z, 'b',time, acc, 'k')


plt.figure()
plt.title ('Bar_Temp Vs Time')
plt.plot(time, bar_temp, 'r')
plt.figure()
plt.title ('Bar_Pressure Vs Time')
plt.plot(time, bar_pres, 'g')
# 
#plt.figure()
#plt.title('Temp Vs Time')
#plt.plot(time, Temp)
#==============================================================================