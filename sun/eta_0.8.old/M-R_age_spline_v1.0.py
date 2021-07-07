#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 2019
Last updated on Tue Jun 25 2019
Version 0.1*

@author: Stanley A. Baronett
"""
import numpy as np
import matplotlib.pyplot as plt
import mesa_reader as mr
from scipy.interpolate import CubicSpline

# =============================================================================
# Import MESA history.data using PyMesaReader
# =============================================================================
# Make MesaData objects from a history files
h1 = mr.MesaData('LOGS/history_to_end_agb.data')
h2 = mr.MesaData('LOGS/history_to_wd.data')

# Input sequence of data files into a, m, and logR arrays
# for the age (in years), mass (in Msun units) and radius (in log10 Rsun units)

# SOLAR AGE DATA (measured in years)
# (First real age entry at approx. 1.2275e+10 yrs;
# initial 3 points used for smooth transition of 10 millions years)
a = np.array([1.226500e+10, 1.226525e+10, 1.226550e+10]) 
a1 = h1.star_age
a2 = h2.star_age

# SOLAR MASS DATA (measured in Msun units)
# (First 3 data points used for smooth transition from 1 Msun)
m = np.array([1.0, 1.0, 1.0]) 
m1 = h1.star_mass
m2 = h2.star_mass

# SOLAR RADIUS DATA (measured in log10 Rsun units)
# (First 3 data points used for smooth transition from 1 Rsun)
logR = np.array([0.0, 0.0, 0.0]) 
logR1 = h1.log_R
logR2 = h2.log_R

# Concatenate data into single arrays
a = np.append(a, [a1])
a = np.append(a, [a2])
m = np.append(m, [m1])
m = np.append(m, [m2])
logR = np.append(logR, [logR1])
logR = np.append(logR, [logR2])

# Plot for log_R vs. Age
fig, ax1 = plt.subplots(figsize=(8, 4.5))
plt.title(r'$\log_{10}$ Radius vs. Age')
plt.xlabel('Stellar Age [' r'$10^{10}$' ' yrs]')
plt.ylabel('Stellar Radius [' r'$\log_{10} R_\odot$]')
ax1.scatter(a, logR, s=1, marker='.')
plt.savefig('graphs/log_R_vs_age.png', dpi=300)
plt.show()

#temp = np.log10(5)
#temp2 = 10**temp

# Convert logR values into AU (REBOUND default units) and store in new array r.
r = np.zeros(logR.size)
for i,lrad in enumerate(logR):
    r[i] = (10**lrad) * 0.00465047 # convert from log10(Rsun) to AU
    
# Plot for R vs. Age
fig, ax2 = plt.subplots(figsize=(8, 4.5))
plt.title('Radius vs. Age')
plt.xlabel('Stellar Age [' r'$10^{10}$' ' yrs]')
plt.ylabel('Stellar Radius [AU]')
ax2.scatter(a, r, s=1, marker='.')
plt.savefig('graphs/R_vs_age.png', dpi=300)
plt.show()

# =============================================================================
# Cubic spline interpolation
# =============================================================================
# Generate cubic splines
csm = CubicSpline(a, m)
csr = CubicSpline(a, r)

# =============================================================================
# Plots to compare splines with data
# =============================================================================
as1 = np.arange(1.2260e+10, 1.255e+10, 1e+6) # 1 million year steps
fig, ax3 = plt.subplots(figsize=(8, 4.5))
plt.title('Comparison of Spline and Data')
plt.xlabel('Stellar Age [' r'$10^{10}$' ' yrs]')
plt.ylabel('Stellar Radius [AU]')
ax3.plot(a, r, '.', label='data')
ax3.plot(as1, csr(as1), label="spline")
ax3.set_ylim(bottom=0)
ax3.legend(loc='best', ncol=1)
plt.savefig('graphs/R_vs_age_spline-data.png', dpi=300)
plt.show()