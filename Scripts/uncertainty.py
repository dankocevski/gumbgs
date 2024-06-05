#!/usr/bin/env -S python3


# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:17:05 2024

@author: yugad

About: This code takes as input a directory with the list of simulation files prints out the average detection rate, and the number of times the simulation has been repeated.
	My advice is to have only the simulation results of one sepecific volume fill ratio in the input directory.

"""

import EventStatistics as es
import numpy
import os
import sys
import numpy as np

working_directory = sys.argv[1]


file_list = os.listdir(working_directory)

DE_array = []  # detection efficiency array
fraction_fill_array = []

for filename in file_list:
	
	file_path = os.path.join(working_directory, filename)
	
	if file_path.endswith('id1.sim'):
		
		#print(filename)
		
		fraction_fill = filename.split("_")[1].split(".")[0]
		
		results = es.run(file_path)
		
		DE_array.append(results[2])
		fraction_fill_array.append(int(fraction_fill))
		

#print(DE_array)
#print(fraction_fill_array)

average_DE = np.average(DE_array)
std_DE = np.std(DE_array)



print(f"\nNumber of simulations: {len(DE_array)}")

print(f"The average detector rate is {np.round(average_DE, 3)} +/- {np.round(std_DE, 3)} photons/sec")

print(f"The fill is {np.round(np.average(fraction_fill_array))}%")

print(f"The square root of the average is {np.round(np.sqrt(average_DE), 3)} photons/sec\n")




























