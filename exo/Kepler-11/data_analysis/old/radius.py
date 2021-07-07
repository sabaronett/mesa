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

# SOLAR RADIUS DATA (measured in Rsun units)
r = np.array([]) 
r1 = h1.radius
r2 = h2.radius

# Concatenate data into single arrays
a = np.append(a, [a1])
a = np.append(a, [a2])
r = np.append(r, [r1])
r = np.append(r, [r2])

# =============================================================================
# Plot
# =============================================================================
fig, ax = plt.subplots(figsize=(8, 4.5))
plt.title('Radius vs. Age')
plt.xlabel('yr')
plt.ylabel(r'$R_{\odot}$')
ax.plot(a, r)
plt.savefig('graphs/R_vs_age.png', dpi=300)
plt.show()