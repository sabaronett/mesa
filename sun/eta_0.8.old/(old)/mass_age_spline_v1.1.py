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

# =============================================================================
# Import MESA history.data using PyMesaReader
# =============================================================================
# Make a MesaData object from a history file
h = mr.MesaData('LOGS/history_to_end_agb.data')
h1 = mr.MesaData('LOGS/history_to_wd.data')
# Input sequence of data files into x and y arrays
x0 = ([])
x = h.star_age
x1 = h1.star_age
y0 = 
y = h.star_mass
y1 = h1.star_mass
# Concatenate data into single arrays
x = np.append(x0, x, [x1])
y = np.append(y0, y, [y1])

# =============================================================================
# Cubic spline interpolation
# =============================================================================
# Generate cubic splines with various boundary condition types
cs1 = CubicSpline(x, y)
cs2 = CubicSpline(x, y, bc_type='natural')

# =============================================================================
# Plots of data to compare
# =============================================================================
xs1 = np.arange(1.225e+10, 1.255e+10, 1e+5) # 100,000 year steps
fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(x, y, 'o', label='data')

ax.plot(xs1, cs1(xs1), label="Default")
ax.plot(xs1, cs2(xs1), label="Natural")

#ax.set_xlim(-0.5, 9.5)
ax.legend(loc='best', ncol=3)
plt.show()
