#! /usr/bin/env python3.7

from math  import pi
from numpy import around

num_mol = 300
box     =  30  
bins    = 500  
cutoff  =  14



binlength = float(cutoff)/bins

R = 0.56
d = 0.69

num_den = num_mol/box**3
vol_den = 7*num_den - 6*num_mol*pi/12*(4*R+d)*(2*R-d)**2/box**3
num_den = around(num_den,4)
vol_den = around(vol_den,4)
