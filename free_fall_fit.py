#Import Packeges
import csv
import statistics

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
from scipy.optimize import curve_fit

#Free Fall Plotting and Fitting

#Import CSV Data
with open("serie_10_a.csv", "r") as i:
    rawdata = list(csv.reader(i, delimiter = ","))
    
free_fall = np.array(rawdata[2:], dtype=(float))

t_data = free_fall[:,0]
p_data = free_fall[:,1]
v_data = free_fall[:,2]
a_data = free_fall[:,3]

"""
#Plotting m/s
style.use('ggplot')
plt.scatter(t_data, p_data, color = 'm')
plt.title("Caída Libre")
plt.xlabel("Tiempo (s)") 
plt.ylabel('Posición (m)')
plt.show()

#Fitting m/s
def model_P(t, v, h, a):
    return h + v*t + a/2 * t**2

popt, pcov = curve_fit(model_P, t_data, p_data, p0=[0.7, 0.1, 9.81])
print("Optimum values: ", popt)
print("Error:", pcov)

plt.imshow(np.log(np.abs(pcov)))
plt.colorbar()
plt.show()

error = np.sqrt(np.diag(pcov))
print("Error", error)

v_opt, h_opt, a_opt = popt
x_model = np.linspace(min(t_data), max(t_data), 100)
y_model = model_P(x_model, v_opt, h_opt, a_opt)

print('Final Error', pcov)

plt.scatter(t_data, p_data, color = 'm')
plt.plot(x_model, y_model, color = 'b', label = 'Ajuste')
plt.title("Caída Libre")
plt.xlabel("Tiempo (s)") 
plt.ylabel('Posición (m)')
plt.legend()
plt.show()
"""

#Plotting v/s
style.use('ggplot')
plt.scatter(t_data, v_data, color = 'b')
plt.title("Caída Libre")
plt.xlabel("Tiempo (s)") 
plt.ylabel('Velocidad (m/s)')
plt.show()

#Fitting v/s
def model_V(t, a, v):
    return a*t + v

popt, pcov = curve_fit(model_V, t_data, v_data, p0=[9.88, 0.7])
print("Optimum values: ", popt)
print("Error:", pcov)

plt.imshow(np.log(np.abs(pcov)))
plt.colorbar()
plt.show()

a_opt, b_opt = popt
x_model = np.linspace(min(t_data), max(t_data), 100)
y_model = model_V(x_model, a_opt, b_opt)
print("Final Error", pcov)

error = np.sqrt(np.diag(pcov))
print("Error sqrt: ", error)

plt.scatter(t_data, v_data, color = 'b')
plt.plot(x_model, y_model, color = 'r', label = 'Ajuste')
plt.title("Caída Libre")
plt.xlabel("Tiempo (s)") 
plt.ylabel('Velocidad (m/s)')
plt.legend()
plt.show()

"""
#Plotting a/s
plt.scatter(t_data, a_data, color = 'y')
plt.title("Caída Libre")
plt.xlabel('Tiempo (s)') 
plt.ylabel('Aceleración ($m/s^2$)')
plt.show()

#Fitting a/s
Mean = statistics.mean(a_data)
print("Media de la aceleracion = ", Mean)

def const(size, value):
    # Using multiply operator
    requiredlist = [value]*size
    # return the list
    return requiredlist
# Driver code
# given value and size
size = len(a_data)
value = Mean
# passing value and size to createList function
a = const(size, value)

plt.scatter(t_data, a_data, color = 'y')
plt.plot(t_data, a, color = 'r', linestyle = '-', label = 'Ajuste a una constante $y$')
plt.legend()
plt.show()
"""