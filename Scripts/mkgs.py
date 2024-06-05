#!/usr/bin/env -S python3

'''
Note: You must have the template files called 'half.geo.setup' and 'half.source' that I uploaded on GitHub in the same directory as where you want to save the outputs of this script.

Created this script using ChatGPT. Prompt was to convert into Python my Unix shell function called mkgs, which creates a duplicate of an already existing template of geometry and source files, and changes the fraction of water fill in the tank to a value determined by the user's input.

Usage: mkgs.py <percent fill in tank>

Example: mkgs.py 10
will create two files: 10.geo.setup and 10.source, which are copies of the template half.geo.setup and half.source, but all the half keywords are replaced by 10. Meaning the new files have 10% fill of water.
'''

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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python mkgs.py <value>")
        sys.exit(1)
    
    try:
        input_value = float(sys.argv[1])
    except ValueError:
        print("Please provide a numeric value.")
        sys.exit(1)
    
    mkgs(input_value)

