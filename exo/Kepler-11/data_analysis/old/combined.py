"""
Created on Fri Aug 23 2019
Last updated on Fri Aug 23 2019
Version 1.0

@author: Stanley A. Baronett
"""
import numpy as np
import matplotlib.pyplot as plt
import mesa_reader as mr
import math

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

plt.plot(range(4))

plt.figure()
plt.plot(range(4), 'ro-')

plt.figure(), plt.plot(...)

plt.show() # only do this once, at the end

# =============================================================================
# Combined Plot
# =============================================================================
fig, ax = plt.subplots(figsize=(8, 4.5))
plt.title('Mass, Radius, Luminosity vs. Age')
plt.xlabel('yr')
plt.yscale("log")
plt.ylabel(r'$M_{\odot}, R_{\odot}, L_{\odot}$')
ax.plot(a, m, label='Mass')  
ax.plot(a, r, label='Radius')
ax.plot(a, l, label='Luminosity')
ax.legend(loc='best', ncol=1)
plt.savefig('graphs/combined.png', dpi=400)
plt.show()