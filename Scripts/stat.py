#!/usr/bin/env -S python3



# -*- coding: utf-8 -*-
"""
Created on Wed May 29 14:48:36 2024

@author: yugad

description: This is a file that uses Daniel's EventStatistics.run function to print some statistics of a simulation file. Can customize easily in the future if needed.
"""

import argparse
import sys
import EventStatistics as es
import EventViewer as ev


def main():
	
	parser = argparse.ArgumentParser(description="%(prog)s summarizes the simulation file into a few statistics.")
	
	
	parser.add_argument('simfile', help = "Path to the simulation file. It is usually the file that ends in *inc1.id1.sim")
	
	parser.add_argument('-p', '--plot', action='store_true', help="show summary plot.") #this is another optional flag that, when included, will plot the cropped rpjbs.
	
	args = parser.parse_args()
	
	plot_flag = False
	
	if args.plot:  # if the -p flag is present in the command line, then we change the variable 'plot_flag' to True. Otherwise, it remains False. This is passed later into the run command.
		
		plot_flag = True
	
	es.run(filename = args.simfile, showPlots = plot_flag)
	
	print('Done!')
	
	

if __name__ == "__main__":
	main()






