#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 16:37:51 2017

@author: emmalevin
"""

#El nino

from netCDF4 import Dataset, num2date
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#---Readd Input Data
ifile = "/Users/hiroyukimurakami/Desktop/HadISST_sst.nc"

f1 = Dataset(ifile,"r")

sst = f1.variables['sst'] # SST
lon = f1.variables['longitude'] # Longitude
lat = f1.variables['latitude'] # Latitude
time = f1.variables['time'] # Time

# Convert time to date (see http://unidata.github.io/netcdf4-python/#netCDF4.num2date)
ndate = num2date(time[:], calendar = time.calendar, units=time.units)
nyears = np.array([ nd.year for nd in ndate]) # [1870,1870,....,2017,2017]

# Find time index between Jan 1981 to Dec 2016
syear = 1981
eyear = 2016
tidx = np.where(((nyears>=syear) & (nyears<=eyear)))[0]

ndate = ndate[tidx] # dates for the targeted period

# Find index for the Nino-3.4 region (5S-5N, 170W-120W)
slat = -5
nlat = 5
wlon = -170 
elon = -120

yidx = np.where((lat[:]>=slat) & (lat[:]<=nlat))[0]
xidx = np.where((lon[:]>=wlon) & (lon[:]<=elon))[0]


# Get SST data for the period Jan 1981 - Dec 2016
sst = np.ma.masked_where(sst[tidx,yidx,xidx]==-1000,sst[tidx,yidx,xidx])

# Compute domain mean
sst = sst.mean(axis=2).mean(axis=1)

# Check dimension
tmax = len(sst) # number of months
ymax = tmax/12 # number of years


sst = sst.reshape((ymax,12)) # reshape [year,12 months]

# Compute climatological monthly mean
sstmean = sst.mean(axis=0) # shape = [12]

# Compute anomaly from the climatological monthly mean
ssta = sst
for iyear in range(ymax):
 for imon in range(12):
    ssta[iyear,imon] = sst[iyear,imon] - sstmean[imon]
    
ssta =ssta.reshape(ymax*12)


# Plot
fig = plt.figure(figsize=(10,6))
ax = plt.subplot(1,1,1)

#--plot graph (Nino3.4 anomaly)
x = np.arange(tmax) # [0,1,.....tmax-1]

plt.plot(x,ssta, label="Nino-3.4 Index")

#--plot labels for years (every 5 years)
xlocs = []
xlabels = []
ii=0
for nd in ndate:
  if nd.year %5 ==0 and nd.month ==1:
     xlocs.append(ii)
     xlabels.append(nd.year) 
     plt.axvline(x=ii,ls='--',linewidth=1, color='k') # plot vertical dashed line

  ii=ii+1

plt.xticks(xlocs,xlabels)


#--plot zero dashed line
plt.axhline(y=0.0,ls='--',linewidth=1, color='k')

#--set range of data
ax.set_ylim((-3,3))
ax.set_xlim((0,tmax+1))

#--Add legend
plt.legend(loc=2,ncol=4)

#--Add title
plt.title("SST Anomaly in Nino-3.4 (%4i-%4i)" % (syear,eyear))

ax.set_ylabel('SST Anomally [K]')
ax.set_xlabel('Year')

for ii in range(tmax):
     print ndate[ii], ssta[ii]

plt.show()