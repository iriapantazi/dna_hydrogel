#! /usr/bin/env python3.7 

from itertools import islice
from constants import tau_submulti, num_atoms, num_molecules, skip_info_lines, r_cut, delta_r, num_bins, bs
import numpy as np
import math
import matplotlib.pyplot as plt

def create_to_plot_file(filename):
    x_axis = np.linspace(0,r_cut,num_bins+1)
    counts = np.zeros((num_bins+1), dtype='int')

    with open (filename,'r') as f:
        time_list = []        
        distances = []
        all_at_single_t  = np.zeros((num_atoms,    9), dtype='float')
        ones             = np.zeros((num_molecules,9), dtype='float') #ones_at_single_t 
        for line in f:
            if 'ITEM: TIMESTEP' in line:
                timestep = int(''.join(islice(f, 1)))
                if (timestep >= 10): #consider only final steps of steady state
                    timestep = timestep * tau_submulti 
                    #print(timestep)
                    time_list.append(timestep)
                    all_atoms = ''.join(islice(f,skip_info_lines,num_atoms+skip_info_lines))
                    all_atoms = all_atoms.splitlines()
                    i = 0
                    for n in range(num_atoms):
                        #at_id, mol, at_type, at_x, at_y, at_z, at_vx, at_vy, at_vz 
                        all_at_single_t[n][0:9]  = all_atoms[n].split()
                        if  (int (all_at_single_t[n][2]) == 1 ): # only the central particle
                            ones[i][0:9] = all_at_single_t[n][0:9] #ones_at_single_t[i][0:9] 
                            i+=1
                    for i in range(0,num_molecules,1):
                        for j in range(i+1,num_molecules,1):
                            dr = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                            if  (dr <= r_cut):
                                distances.append(dr)
                            else:
                                dr_1 = math.sqrt((ones[i][3]-ones[j][3]-bs)**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                                dr_2 = math.sqrt((ones[i][3]-ones[j][3]+bs)**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                                dr_3 = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4]-bs)**2 + (ones[i][5]-ones[j][5])**2) 
                                dr_4 = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4]+bs)**2 + (ones[i][5]-ones[j][5])**2) 
                                dr_5 = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5]-bs)**2) 
                                dr_6 = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5]+bs)**2) 
                                #dr_7 = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                                #dr_8 = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                                #dr_9 = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                                #dr_a = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                                #dr_b = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                                #dr_c = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                                #dr_d = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                                #dr_e = math.sqrt((ones[i][3]-ones[j][3])**2 + (ones[i][4]-ones[j][4])**2 + (ones[i][5]-ones[j][5])**2) 
                                dr = min(dr_1,dr_2,dr_3,dr_4,dr_5,dr_6)
                                if  (dr <= r_cut):
                                    distances.append(dr)
                                
        
        n, bins, patches = plt.hist(distances, num_bins, facecolor='blue', alpha=0.5)
        plt.clf()
        a = []
        for i in range(len(n)):
            a_tmp = int(n[i])/ (4*math.pi*(bins[i+1]-bins[i])*bins[i+1]**2)
            a.append(a_tmp)
        a.append(0)
        plt.plot(bins,a)
        plt.show()

    return()


