#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 09:14:27 2017

@author: emmalevin
"""
import numpy as np
import matplotlib.pyplot as plt

"""   # two dimensional grids              # need to go over
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.linspace(-np.pi, np.pi, 50)
xx, yy = np.meshgrid(x, y)  #I understand everything up to here
print xx, yy
print xx.shape, yy.shape   """
#-----------------------------------------------------------------------
array2 = np.array([[92, 100, 95, 90],[83, 95, 92, 85],[78, 87, 85, 82]])
array2.ndim
array2.shape
array2.size
np.mean(array2, axis = 0)
np.mean(array2, axis = 1)
#print array2[:2]
#print array2[:2, :3]
array1 = np.array([92, 90, 95, 100, 95, 87, 92, 85, 87, 78, 85, 82])
np.mean(array1)
#print array1[]
#-----------------------------------------------------------------------
"""x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(np.pi * x) 

time = np.array([0, 70, 150, 185])
control = np.array([3.83, 6, 8.5, 16])
experiment = np.array([10.9, 32.9, 41.5, 97.1])

plt.figure(1)
plt.subplot(211)
plt.plot(time, experiment, "r-", time, control, "b-",)
plt.xlabel("Time Stirred (Minutes)")
plt.ylabel("Percent Transmission")
plt.title("Percent Transmission versus Stirring Time")
plt.grid()
#plt.show() 

plt.subplot(212)
plt.plot(x, y, "g-")
plt.grid()
#plt.show """
#-----------------------------------------------------------------------
x = np.arange(-10, 10)
y = x**3
#plt.plot(x, y, "r--")
#plt.axis([-5, 5, -10, 10])
#plt.show()
#-----------------------------------------------------------------------
"""import scipy.optimize

y += np.random.rand(y.size)

def linear_function(x, a, b):
    return a*x + b

popt, pcov = scipy.optimize.curve_fit(linear_function, x, y)
print("Fitted values:")
print(popt)
print("Covariance of fitted values")
print(pcov)

plt.scatter(x, y)  # scatter() is shorthand for plotting points only (no line between)
plt.plot(x, linear_function(x, popt[0], popt[1]))""" # need to go over
#-----------------------------------------------------------------------
"""x = np.random.random(50)
figure = plt.figure("Figure 1")
subplot1 = figure.add_subplot(2, 3, 1)
subplot2 = figure.add_subplot(2, 3, 2)
plt.plot(np.random.random(50), "go")
plt.grid()
subplot6 = figure.add_subplot(2, 3, 6)
plt.plot(x, 2 * x, "k--")
plt.grid()
plt.show()"""

x = np.linspace(0, 13, 50)
arizona = -30 * np.sin(x/2) + 60
sanFran = 10 * np.sin(x * 2 ) + 57
aline = plt.plot(x, arizona, "r-", x, arizona, "vm")
sline = plt.plot(x, sanFran, "^k", x, sanFran, "b-",)
plt.legend((aline, sline), ('Arizona', 'San Francisco'), loc = 'upper left', shadow = True)
plt.xlabel("Month")
plt.ylabel("Temperature (degrees F)")
plt.title("Average Monthly Temperature")
plt.show()
