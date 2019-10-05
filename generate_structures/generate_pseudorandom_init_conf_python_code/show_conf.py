#! /usr/bin/python

from importing_modules import *
from  graphing_modules import *
from         functions import *


atom = np.zeros((3500,3))
i =0
n_molecules = 350
box_limit   =  15.0


#---------------------------plot all------------------------------                  
with open ('accepted.dat','r') as f:
    for line in f.readlines():
        print i
        atom[i][0],atom[i][1],atom[i][2] = line.split()
        i += 1
    
    

plot_all(atom,n_molecules,box_limit)

