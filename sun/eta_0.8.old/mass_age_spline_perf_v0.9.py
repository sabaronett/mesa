#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11, 2019
Last updated on Thu Jun 13, 2019
@author: Stanley A. Baronett
Version ***
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
x = np.array([1.22650e+10, 1.22655e+10]) # First real age entry at 1.2275e+10
x1 = h1.star_age
x2 = h2.star_age
y = np.array([1.0, 1.0]) # Initial mass endpoints for smooth transition
y1 = h1.star_mass
y2 = h2.star_mass
# Append data into single arrays
x = np.append(x, [x1])
y = np.append(y, [y1])
x = np.append(x, [x2])
y = np.append(y, [y2])

# =============================================================================
# Interpolate data with cubic spline using default (i.e., "not-a-knot")
# boundary condition type
# =============================================================================
cs = CubicSpline(x, y)
    
# =============================================================================
# Time performance tracking for spline calls
# =============================================================================
# Create arrays to store retrieval times for various step resolutions
t6 = np.array([])
t5 = np.array([])
t4 = np.array([])
t3 = np.array([])
t2 = np.array([])
t1 = np.array([])
t0 = np.array([])
# Create ranges with various step resolutions
se6 = np.arange(1.22650e+10, 1.25363e+10, 1e+6)
se5 = np.arange(1.22650e+10, 1.25363e+10, 1e+5)
se4 = np.arange(1.22650e+10, 1.25363e+10, 1e+4)
se3 = np.arange(1.22650e+10, 1.25363e+10, 1000)
se2 = np.arange(1.22650e+10, 1.25363e+10, 100)
se1 = np.arange(1.22650e+10, 1.25363e+10, 10)
se0 = np.arange(1.22650e+10, 1.25363e+10, 1)
# Collect retrieval time data into respective arrays
for item in se6:
    start = time.perf_counter_ns()
    mass = cs(item)
    end = time.perf_counter_ns()
    dt = end - start
    t6 = np.append(t6, dt)
for item in se5:
    start = time.perf_counter_ns()
    mass = cs(item)
    end = time.perf_counter_ns()
    dt = end - start
    t5 = np.append(t5, dt)
for item in se4:
    start = time.perf_counter_ns()
    mass = cs(item)
    end = time.perf_counter_ns()
    dt = end - start
    t4 = np.append(t4, dt)
for item in se3:
    start = time.perf_counter_ns()
    mass = cs(item)
    end = time.perf_counter_ns()
    dt = end - start
    t3 = np.append(t3, dt)
for item in se2:
    start = time.perf_counter_ns()
    mass = cs(item)
    end = time.perf_counter_ns()
    dt = end - start
    t2 = np.append(t2, dt)
for item in se1:
    start = time.perf_counter_ns()
    mass = cs(item)
    end = time.perf_counter_ns()
    dt = end - start
    t1 = np.append(t1, dt)
for item in se0:
    start = time.perf_counter_ns()
    mass = cs(item)
    end = time.perf_counter_ns()
    dt = end - start
    t0 = np.append(t0, dt)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(se6, t6, label='1e+6')
ax.plot(se5, t5, label='1e+5')
ax.plot(se4, t4, label='1e+4')
ax.plot(se3, t3, label='1000')
ax.plot(se2, t2, label='100')
ax.plot(se1, t1, label='10')
ax.plot(se0, t0, label='1')
ax.legend(loc='best', ncol=2)
plt.show()
print("1e+6 average time: ", np.average(t6), "ns")
print("1e+5 average time: ", np.average(t5), "ns")
print("1e+4 average time: ", np.average(t4), "ns")
print("1e+3 average time: ", np.average(t3), "ns")
print("1e+2 average time: ", np.average(t2), "ns")
print("1e+1 average time: ", np.average(t1), "ns")
print("1e+0 average time: ", np.average(t0), "ns")


#t_default = np.array([])
#t_natural = np.array([])
#for z in range(1000):
#    start = time.perf_counter_ns()
#    cs1 = CubicSpline(x, y)
#    end = time.perf_counter_ns()
#    dt = end - start
#    t_default = np.append(t_default, dt)
#    start = time.perf_counter_ns()
#    cs2 = CubicSpline(x, y, bc_type='natural')
#    end = time.perf_counter_ns()
#    dt = end - start
#    t_natural = np.append(t_natural, dt)
#    
#fig, ax = plt.subplots(figsize=(6, 4))
#z = np.arange(1000)
#ax.plot(z, t_default, label='Default')
#ax.plot(z, t_natural, label='Natural')
#ax.legend(loc='best', ncol=1)
#plt.show()
#print("Default average time: ", np.average(t_default), "ns")
#print("Natural average time: ", np.average(t_natural), "ns")

# =============================================================================
# Plots of data to compare
# =============================================================================
#xs1 = np.arange(1.2264e+10, 1.2276e+10, 100) # 1 million year steps
#fig, ax = plt.subplots(figsize=(15, 7))
#ax.plot(x, y, 'o', label='init. breakpts.') # Uncomment to highlight initial transition
#ax.plot(x1, y1, 'o', label='data')
#ax.plot(xs1, cs1(xs1), label="Default")
#ax.plot(xs1, cs2(xs1), label="Natural")
##ax.set_xlim(1.2264e+10, 1.2276e+10) # Uncomment to highlight initial transition
##ax.set_ylim(0.99, 1.001) # Uncomment to highlight initial transition
#ax.legend(loc='best', ncol=1)
#plt.show()