#!/usr/bin/env -S python3

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:52:28 2024

@author: yugad

description: Applies cosima to all the .source files in the directory.
"""

import subprocess
import os
import sys

working_directory = sys.argv[1]

file_list = os.listdir(working_directory)

for filename in file_list:
	
	file_path = os.path.join(working_directory, filename)
	
	if file_path.endswith('.source'):
		
		subprocess.run(["cosima","-v","0", file_path])
		
		

