#usr/bin/bash

# This script repeats cosima simulations n times. Usage: repeat.bash <path to source file> <number of times to repeat>

n=$2  #$2 stands for the second argument. Here, it will be the number of times to repeat thesimulation

for (( i=1; i<=n; i++))

do
  cosima -v 0 $1  # $1 is the first argument. Passing in the source file each time in the for loop
done


