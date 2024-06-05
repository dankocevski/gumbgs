#!/usr/bin/env -S python3


# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 09:09:06 2024

@author: yugad

description: While mkgs.py is useful to create one new volume files at once, this code reads in an input text file and creates multiple geometry and source files. 
"""


import sys
import re

def mkgs(input_value):
    # Calculate the new_fraction
    new_fraction = round(input_value / 100, 2)
    
    # Format the output filename
    output_filename = f"{int(input_value)}"
    
    # Read the half.geo.setup file and replace the fraction_fill value
    with open('half.geo.setup', 'r') as file:
        geo_setup_content = file.read()
    geo_setup_content = re.sub(r'fraction_fill 0.5', f'fraction_fill {new_fraction}', geo_setup_content)
    with open(f'{output_filename}.geo.setup', 'w') as file:
        file.write(geo_setup_content)
    
    # Read the half.source file and replace the 'half' with the output filename
    with open('half.source', 'r') as file:
        source_content = file.read()
    source_content = re.sub(r'half', output_filename, source_content)
    with open(f'{output_filename}.source', 'w') as file:
        file.write(source_content)

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Ignore empty lines
                    try:
                        input_value = float(line)
                        mkgs(input_value)
                    except ValueError:
                        print(f"Skipping invalid value: {line}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python mkgs_batch.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    process_file(file_path)
