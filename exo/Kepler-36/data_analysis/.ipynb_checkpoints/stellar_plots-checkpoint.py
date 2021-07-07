"""
Created on Fri Aug 23 2019
Last updated on Fri Aug 23 2019
Version 1.0

@author: Stanley A. Baronett
"""
import numpy as np
import matplotlib.pyplot as plt
import mesa_reader as mr

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

# Concatenate data into single arrays
a = np.append(a, [a1])
a = np.append(a, [a2])
m = np.append(m, [m1])
m = np.append(m, [m2])
r = np.append(r, [r1])
r = np.append(r, [r2])
l = np.append(l, [l1])
l = np.append(l, [l2])

# =============================================================================
# Plot figures
# =============================================================================
plt.figure(figsize=(8, 4.5))
plt.title('Mass vs. Age')
plt.xlabel('yr')
plt.ylabel(r'$M_{\odot}$')
plt.plot(a, m)
plt.savefig('graphs/M_vs_age.png', dpi=300)

plt.figure(figsize=(8, 4.5))
plt.title('Radius vs. Age')
plt.xlabel('yr')
plt.ylabel(r'$R_{\odot}$')
plt.plot(a, r)
plt.savefig('graphs/R_vs_age.png', dpi=300)

plt.figure(figsize=(8, 4.5))
plt.title('Luminosity vs. Age')
plt.xlabel('yr')
plt.ylabel(r'$L_{\odot}$')
plt.plot(a, l)
plt.savefig('graphs/L_vs_age.png', dpi=300)

plt.figure(figsize=(8, 4.5))
plt.title('Mass, Radius, Luminosity vs. Age')
plt.xlabel('yr')
plt.yscale("log")
plt.ylabel(r'$M_{\odot}, R_{\odot}, L_{\odot}$')
plt.plot(a, m, label='Mass')  
plt.plot(a, r, label='Radius')
plt.plot(a, l, label='Luminosity')
plt.legend(loc='best', ncol=1)
plt.savefig('graphs/combined.png', dpi=400)

plt.show() # Show all figures