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

# Concatenate data into single arrays
a = np.append(a, [a1])
a = np.append(a, [a2])
m = np.append(m, [m1])
m = np.append(m, [m2])

# =============================================================================
# Plot
# =============================================================================
fig, ax = plt.subplots(figsize=(8, 4.5))
plt.title('Mass vs. Age')
plt.xlabel('yr')
plt.ylabel(r'$M_{\odot}$')
ax.plot(a, m)
plt.savefig('graphs/M_vs_age.png', dpi=300)
plt.show()