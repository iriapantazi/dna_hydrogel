#! /usr/bin/env python3.7
from math import pi 

num_mols  = 300
box_size  = 30
num_atoms = num_mols * 10
eff_atoms = num_mols * 7 
rad_atoms = 0.96

plot_all = True
number_density =  num_mols                  / (box_size)**3
volume_density = (eff_atoms*pi*rad_atoms**2) / (box_size)**3
