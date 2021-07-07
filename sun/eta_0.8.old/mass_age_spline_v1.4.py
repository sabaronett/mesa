#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:42:09 2019

@author: Stanley A. Baronett & Noah Ferich
"""
import numpy as np
import matplotlib.pyplot as plt
import mesa_reader as mr
from scipy.interpolate import CubicSpline
import time

# =============================================================================
# Import MESA history.data using PyMesaReader
# =============================================================================
# Make a MesaData object from a history file
h1 = mr.MesaData('LOGS/history_to_end_agb.data')
h2 = mr.MesaData('LOGS/history_to_wd.data')
# Input sequence of data files into x and y arrays
x = np.array([1.226000e+10, 1.226525e+10, 1.226550e+10]) # First real age entry at 1.2275e+10
x1 = h1.star_age
x2 = h2.star_age
y = np.array([1.0, 1.0, 1.0]) # Initial mass breakpoints for smooth transition
y1 = h1.star_mass
y2 = h2.star_mass
# Concatenate data into single arrays
x = np.append(x, [x1])
y = np.append(y, [y1])
x = np.append(x, [x2])
y = np.append(y, [y2])

# =============================================================================
# Cubic spline interpolation
# =============================================================================
# Generate cubic splines with various boundary condition types
cs1 = CubicSpline(x, y)
#cs2 = CubicSpline(x, y, bc_type='natural')

#start = time.time()
#print(cs1(1.22675e+10), "Solar-Masses")
#end= time.time()
#print(end - start, "seconds")
#
#start = time.time()
#print(cs1(1.253e+10), "Solar-Masses")
#end= time.time()
#print(end - start, "seconds")

# =============================================================================
# Time performance tracking for spline calls
# =============================================================================
# Create arrays to store times for various steps
t6 = np.array([])
t5 = np.array([])
t4 = np.array([])
t3 = np.array([])
t2 = np.array([])
t1 = np.array([])
# Create 
se6 = np.arange(1.25655e+10, 1.25363e+10, 1e+6)
se5 = np.arange(1.25655e+10, 1.25363e+10, 1e+5)
se4 = np.arange(1.25655e+10, 1.25363e+10, 1e+4)
se3 = np.arange(1.25655e+10, 1.25363e+10, 1000)
se2 = np.arange(1.25655e+10, 1.25363e+10, 100)
se1 = np.arange(1.25655e+10, 1.25363e+10, 10)
for item in se6:
    start = time.time()
     = cs1(item)
    end= time.time()
    
start = time.time()
print(cs1(1.253e+10), "Solar-Masses")
end= time.time()



# =============================================================================
# Plots of data to compare
# =============================================================================
#xs1 = np.arange(1.2260e+10, 1.255e+10, 1e+6) # 1 million year steps
#fig, ax = plt.subplots(figsize=(7.5, 4))
#ax.plot(x, y, 'o', label='init. breakpts.') # Uncomment to highlight initial transition
#ax.plot(x1, y1, 'o', label='data')
#ax.plot(xs1, cs1(xs1), label="Default")
##ax.plot(xs1, cs2(xs1), label="Natural")
#ax.set_xlim(1.226e+10, 1.228e+10) # Uncomment to highlight initial transition
#ax.set_ylim(0.98, 1.01) # " "
#ax.legend(loc='best', ncol=1)
#plt.show()