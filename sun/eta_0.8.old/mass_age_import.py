#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:56:44 2019
Last updated on Mon Jun 10, 2019

@author: Stanley A. Baronett
"""
import numpy as np
from matplotlib import pyplot as plt
import mesa_reader as mr

# Make a MesaData object from a history file
h = mr.MesaData('LOGS/history_to_end_agb.data')
h1 = mr.MesaData('LOGS/history_to_wd.data')
# Input data files into x and y arrays
x = h.star_age
x1 = h1.star_age
y = h.star_mass
y1 = h1.star_mass
# Append data into single arrays
x = np.append(x, [x1])
y = np.append(y, [y1])

# =============================================================================
# # Model check
# z = h.model_number
# z1 = h1.model_number
# z = np.append(z, [z1])
# =============================================================================

# Plot
plt.plot(x, y, 'o',)
plt.show()

fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(x, y, 'o', label='data')
ax.legend(loc='best', ncol=1)
plt.show()


##*******************************************************************
## Review David's spline code
##*******************************************************************
##Interpolate using CubicSpline
##Make sure to rerun whole page
#from scipy.interpolate import CubicSpline
#
##Split points into increasing and decreasing
#a=np.amin(x)
#b=np.amax(x)
#
#
##Clean up arrays to be always increasing and connect. Split before and after "wing" (at 709480).
#xlow=x[0:list(x).index(b)+1]
#xhigh=x[len(x):list(x).index(b)-1:-1]
#xlow=np.insert(xlow,0,x[list(x).index(a)])
#xhigh1=xhigh[0:list(xhigh).index(709480)+1]
#xhigh2=xhigh[list(xhigh).index(709480)+1:len(xhigh)]
#
#ylow=y[0:list(x).index(b)+1]
#yhigh=y[len(x):list(x).index(b)-1:-1]
#ylow=np.insert(ylow,0,y[list(x).index(a)])
#yhigh1=yhigh[0:list(xhigh).index(709480)+1]
#yhigh2=yhigh[list(xhigh).index(709480)+1:len(xhigh)]
#
#
##Cubic spline with natural boundaries
#cslow=CubicSpline(xlow,ylow,bc_type="natural")
#cshigh1=CubicSpline(xhigh1,yhigh1,bc_type="natural")
#cshigh2=CubicSpline(xhigh2,yhigh2,bc_type="natural")
#
##Plot
#x1=np.linspace(a,b,2000)
#x2=np.linspace(a,709480,1000)
#x3=np.linspace(709480,b,1000)
#
#plt.plot(x1,cslow(x1))
#plt.plot(x2,cshigh1(x2))
#plt.plot(x3,cshigh2(x3))
#plt.axis([0,14,-6,3])
#plt.show()