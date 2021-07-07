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
x = h.star_age
x1 = h1.star_age
y = h.star_mass
y1 = h1.star_mass
# Concatenate data into single arrays
x = np.append(x, [x1])
y = np.append(y, [y1])

# =============================================================================
# Cubic spline interpolation
# =============================================================================
# Generate cubic splines with various boundary condition types
cs1 = CubicSpline(x, y)
cs2 = CubicSpline(x, y, bc_type='clamped')
cs3 = CubicSpline(x, y, bc_type='natural')
# Define various steps of dependent variable
xs1 = np.arange(1.225e+10, 1.255e+10, 1e+7) # 10 million year steps
xs2 = np.arange(1.225e+10, 1.255e+10, 1e+6) # 5 million year steps
xs3 = np.arange(1.225e+10, 1.255e+10, 1e+5) # 1 million year steps

# =============================================================================
# Plots of data to compare
# =============================================================================
fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(x, y, 'o', label='data')
# 3 bc_types with 10 mil. yr. steps
ax.plot(xs1, cs1(xs1), label="Default 10e7")
ax.plot(xs1, cs2(xs1), label="Clamped 10e7")
ax.plot(xs1, cs3(xs1), label="Natural 10e7")
# 3 bc_types with 5 mil. yr. steps
ax.plot(xs2, cs1(xs2), label="Default 10e6")
ax.plot(xs2, cs2(xs2), label="Clamped 10e6")
ax.plot(xs2, cs3(xs2), label="Natural 10e6")
# 3 bc_types with 1 mil. yr. steps
ax.plot(xs3, cs1(xs3), label="Default 10e5")
ax.plot(xs3, cs2(xs3), label="Clamped 10e5")
ax.plot(xs3, cs3(xs3), label="Natural 10e5")
#ax.set_xlim(-0.5, 9.5)
ax.legend(loc='best', ncol=3)
plt.show()
