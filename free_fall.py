# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:05:22 2022

@author: 20215
"""

#####-----\\\\\ Free Fall /////-----#####
#Import Libraries
import csv
import statistics

import matplotlib.pyplot as plt
import numpy as np
#from scipy.optimize import curve_fit
#from scipy import integrate as intg
from matplotlib import style
from scipy.optimize import curve_fit  # for curve fitting

#Import CSV Data
with open("serie_10_a.csv", "r") as i:
    rawdata = list(csv.reader(i, delimiter = ","))
    
free_fall = np.array(rawdata[2:], dtype=(float))

tdata = free_fall[:,0]
pdata = free_fall[:,1]
vdata = free_fall[:,2]
adata = free_fall[:,3]


#Plot Data

#Distance over time
style.use('ggplot')
plt.figure(1, dpi=120)
plt.title("Caída Libre")
plt.xlabel("Tiempo (s)") 
plt.ylabel('Posición (m)')
#plt.xlim(0.39,0.48) 
#plt.ylim(0.157,0.335)
#plt.yscale("Linear")
#plt.xscale("Linear")
plt.plot(tdata, pdata, color = 'm', marker = '.', linestyle = '')
plt.show()

#Velocity over time
style.use('ggplot')
plt.figure(2, dpi=120)
plt.title("Caída Libre")
plt.xlabel("Tiempo (s)") 
plt.ylabel('Velocidad (m/s)')
#plt.xlim(0.39,0.48) 
#plt.ylim(0.157,0.335)
#plt.yscale("Linear")
#plt.xscale("Linear")
plt.plot(tdata, vdata,label='Free Fall', color = 'b', marker = '.', linestyle = '')
plt.show()

#Aceleration over time
style.use('ggplot')
plt.figure(3, dpi=120)
plt.title("Caída Libre")
plt.xlabel('Tiempo (s)') 
plt.ylabel('Aceleración ($m/s^2$)')
#plt.xlim(0.48,0.81) 
#plt.ylim(0.157,0.335)
#plt.yscale("Linear")
#plt.xscale("Linear")
plt.plot(tdata, adata, color = 'y', linestyle = '', marker = '.')
#plt.show()

