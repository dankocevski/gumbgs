#!/usr/bin/env -S python3


# -*- coding: utf-8 -*-
"""
Created on Thu May 30 08:46:40 2024

@author: yugad

description: This python script reads all the simulation results in a directory and creates a Volume fill vs. detection rate plot, also displays the best fit curve of some functions.
"""

import EventViewer as ev
import EventStatistics as es
import numpy
import matplotlib.pylab as plt
import os
import scipy
import numpy as np

def look_nice(ax, xlabel, ylabel, title):
    ax.legend()
    ax.set_xlabel(xlabel, size=15)
    ax.set_ylabel(ylabel, size=15)
    ax.set_title(title, size=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)

#working_directory = r"/home/deep/MEGAlib_testing/scratch/"

working_directory = r"/home/deep/MEGAlib_testing/finding_fit_func"

# simfile = r"temp.inc2.id1.sim"

def exp_curve(x, a, b, c):
	
	y = a*np.exp(b*x) + c
	
	return y


def straight_line(x, m, b):
	
	return m*x + b

def hyperbolic_curve(x, a, b, c):
	
	y = b*np.sqrt(-1+(x/a)**2) + c
	
	return y

def inverse_curve(x, a, p):
	
	return a/x**p


file_list = os.listdir(working_directory)


DE_array = []  # detection efficiency array
fraction_fill_array = []

for filename in file_list:
	
	file_path = os.path.join(working_directory, filename)
	
	if file_path.endswith('inc1.id1.sim'):
		
		print(filename)
		
		fraction_fill = filename.split("_")[1].split(".")[0]
		
		results = es.run(file_path)
		
		DE_array.append(results[2])
		fraction_fill_array.append(int(fraction_fill))
		

print("\n")

print(DE_array)
print(fraction_fill_array)

print("\n")
ff_sorted , DE_sorted = zip(*sorted(zip(fraction_fill_array, DE_array)))

DE_array = np.asarray(DE_sorted)
fraction_fill_array = np.asarray(ff_sorted)

print(DE_array)
print(fraction_fill_array)



#%%

log_frac = np.log10(fraction_fill_array)

'''
fit_par, pcov = scipy.optimize.curve_fit(
	f = straight_line,
	xdata = DE_array,
	ydata = log_frac)

m_fit, b_fit = fit_par
'''


#fit_par, pcov = scipy.optimize.curve_fit(f = straight_line , xdata = DE_array, ydata = log_frac)

fit_par, pcov = scipy.optimize.curve_fit(f = inverse_curve , xdata = DE_array, ydata = fraction_fill_array , p0 = [37.45, 0.313])

fit_par2, pcov2 = scipy.optimize.curve_fit(f = exp_curve , xdata = DE_array, ydata = fraction_fill_array, p0 = [1, -1, 100 ])

DE_sampled = np.linspace(np.min(DE_array), np.max(DE_array), 100)


#volume_fit = straight_line(DE_sampled , *fit_par)
inv_fit = inverse_curve(DE_sampled , *fit_par)
exp_fit = exp_curve(DE_sampled , *fit_par2)


fig, ax = plt.subplots(figsize=(15,7))

ax.errorbar(x = DE_array , y = fraction_fill_array , fmt = 'ro', label = 'Data')

#ax.errorbar(x = DE_array , y = log_frac , fmt = 'ro', label = 'Data')

#ax.plot(DE_array , straight_line(DE_array, *fit_par), color = 'black', label = 'Fit')

ax.plot(DE_sampled, inv_fit, color = 'black', label = 'Inverse Fit')
ax.plot(DE_sampled, exp_fit, color = 'magenta', label = 'Exp Fit')

ax.grid()

# we are going to call DE detection rate instead because that is more appropriate. I don't want to chagne all the previous names now so I'll just change the name we display.

look_nice(ax, 'Detection Rate (photons/sec)', 'Tank Fill (%)', '%tank fill vs. DR')

plt.show()







