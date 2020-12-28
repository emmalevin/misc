# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from netCDF4 import Dataset, num2date
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

filename = "/Users/emmalevin/Downloads/HadISST_sst.nc"

f1 = Dataset(filename,"r")

print f1.variables.keys()

sst = f1.variables["sst"]
lon = f1.variables["longitude"]
lat = f1.variables["latitude"]
time = f1.variables["time"]



ndate = num2date(time[:],calendar=time.calendar, units=time.units)

#print sst[0,:,:]
print type(sst[:,:,:])


sst = np.ma.masked_where(sst[:,:,:]==-1000, sst[:,:,:])


fig = plt.figure(figsize=(10,10))
m = Basemap(projection='mill', llcrnrlat=-50, urcrnrlat=50, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()

flon, flat= np.meshgrid(lon[:],lat[:])
x,y = m(flon,flat)

#cmap = cm.bwr
cmap = cm.rainbow
contours = np.arange(-10,40,5)

#cs = m.contourf(x,y,sst[200,:,:], contours, cmap=cmap) 
cs = m.contourf(x,y,sst[:,:,:].mean(axis=0), contours, cmap=cmap) 

m.colorbar(drawedges=True)

cs = m.contour(x,y,sst[:,:,:].mean(axis=0), contours, linestyle='-', linewidths=1.0, colors='k')
plt.clabel(cs,fmt='%.1f', inline=True, fontsize=8)

for ii in range(100):    
 print ndate[ii], sst[ii,:,:].mean()

plt.show()

sstmonthly = sst[:,:,:].mean(axis=1).mean(axis=1)
print sstmonthly

xx = np.arange(1,1001,1)
yy = sstmonthly[0:1000]

fig = plt.figure(figsize=(8,8))
plt.plot(xx,yy)
plt.show()


