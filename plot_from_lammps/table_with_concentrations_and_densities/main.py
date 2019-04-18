#! /usr/bin/python 

from constants import N, box, N_tot_mol, N_eff_mol, radius, dist_bb, dist_bp 
from numpy import around
from math  import pi

num_den_list = []
vol_den_list = []


for i in range(len(N)):

    num_den = float(N[i])/float(box[i]**3)
    num_den = around(num_den,4)
    num_den_list.append(num_den)
    vol_den = 7*num_den*(4/3)*pi*radius**3 - 6*(pi/12)*(4*radius+dist_bb)*(2*radius-dist_bb)**2/box[i]**3
    vol_den = around(vol_den,4)
    vol_den_list.append(vol_den)
    
    print(" "+str(N[i])+" & "+str(box[i])+" & "+str(num_den)+" & "+str(vol_den)+" ")

print(N)
print(box)
print(num_den_list)
print(vol_den_list)
