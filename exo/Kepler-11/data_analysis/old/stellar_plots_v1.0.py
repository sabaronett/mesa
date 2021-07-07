#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 2019
Last updated on Fri Aug 23 2019
Version 1.0

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

# SOLAR AGE DATA (measured in years)
a = np.array([]) 
a1 = h1.star_age
a2 = h2.star_age

# SOLAR MASS DATA (measured in Msun units)
m = np.array([]) 
m1 = h1.star_mass
m2 = h2.star_mass

# SOLAR RADIUS DATA (measured in Rsun units)
r = np.array([]) 
r1 = h1.radius
r2 = h2.radius

# SOLAR LUMINOSITY DATA (measured in Lsun units)
l = np.array([]) 
l1 = h1.luminosity
l2 = h2.luminosity

# SOLAR LUMINOSITY DATA (measured in log10[Lsun] units)
logL = np.array([]) 
logL1 = h1.log_L
logL2 = h2.log_L

# Concatenate data into single arrays
a = np.append(a, [a1])
a = np.append(a, [a2])
m = np.append(m, [m1])
m = np.append(m, [m2])
l = np.append(l, [l1])
l = np.append(l, [l2])
logL = np.append(logL, [logL1])
logL = np.append(logL, [logL2])

# =============================================================================
# Plots
# =============================================================================
# Mass vs. Age
# Plot for R vs. Age
fig, ax1 = plt.subplots(figsize=(8, 4.5))
plt.title('Mass vs. Age')
plt.xlabel('yr')
plt.ylabel(r'$R_{sun}$')
ax1.plot(a, m)
#plt.savefig('graphs/M_vs_age.png', dpi=300)
plt.show()

fig, ax2 = plt.subplots(figsize=(8, 4.5))
plt.title(r'$\log_{10}$ Radius vs. Age')
plt.xlabel('Stellar Age [' r'$10^{10}$' ' yrs]')
plt.ylabel('Stellar Radius [' r'$\log_{10} R_\odot$]')
#ax2.scatter(a, logR, s=1, marker='.')
#plt.savefig('graphs/log_R_vs_age.png', dpi=300)
plt.show()

#temp = np.log10(5)
#temp2 = 10**temp

# Convert logR values into AU (REBOUND default units) and store in new array r.
#r = np.zeros(logR.size)
#for i,lrad in enumerate(logR):
#    r[i] = (10**lrad) * 0.00465047 # convert from log10(Rsun) to AU


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