#!/usr/bin/env -S python3

# description: This is a script that uses Daniel's EventViewer.plot function to plot an event of a simulation.

import argparse
import sys
import EventStatistics as es
import EventViewer as ev
from numpy import random

def main():
	
	parser = argparse.ArgumentParser(description="%(prog)s displays an event in the simulation file. Unless specified, an event is chosen at random between 1-1000")
	
	
	parser.add_argument('simfile', help = "Path to the simulation file. It is usually the file that ends in *inc1.id1.sim")
	
	#parser.add_argument('geofile', help = "Path to the geometry file. It is usually the file that ends in *geo.setup")
	
	parser.add_argument('-e', '--event_number', default = random.randint(low = 1, high = 1000), help = "Event number to show the plot of")
	
	args = parser.parse_args()
	
	if args.event_number == 'All':
		event_no = 'All'
		
	else:
		event_no = int(args.event_number)
		
	
	ev.plot(filename = args.simfile, showEvent = event_no)

	
	print('Done!')
	

if __name__ == "__main__":
	main()






