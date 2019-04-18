#! /usr/bin/env python3.7 

from itertools import islice
from constants import n_bins, tau_submulti, timestep_to_start, skip_info_lines, num_angles, num_angles_y, num_angles_l, num_beads_y 
import numpy as np
import math
#from math import pi
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})


def create_to_plot_file(filename):

    print(filename)
    with open (filename,'r') as f:

        time_list = []        
        all_angles  = np.zeros((num_angles,   5), dtype='float')
        y_angles    = np.zeros((num_angles_y, 5), dtype='float')
        l_angles    = np.zeros((num_angles_l, 5), dtype='float')
        y_angs= []
        y_angs_1 = [] # 120
        y_angs_2 = [] # 180 bead-bead
        y_angs_3 = [] # 180 bead_patch
        l_angs= []

        for line in f:
            if  ('ITEM: TIMESTEP' in line) :
                timestep = int(''.join(islice(f, 1)))
                if (timestep > 19700000):
                    timestep = timestep * tau_submulti 
                    time_list.append(timestep)
                    # con for the connected lines. later will be split into the all_angles np.array
                    all_angles_con = ''.join(islice(f,skip_info_lines,num_angles+skip_info_lines))
                    all_angles_con = all_angles_con.splitlines()
                    i = 0
                    y = 0
                    y_1 = 0
                    y_2 = 0
                    y_3 = 0
                    l = 0
                    for num_rows in range(num_angles):
                        #at_1, at_2, at_3, ang, en  = all_atoms[num_rows].split()
                        all_angles[num_rows][0:5]  = all_angles_con[num_rows].split()
                        # now separate Y and L into the corresponding np.array's
                        if (int(all_angles[num_rows][0]) <= num_beads_y):
                            y_angles[y][0:5] = all_angles[num_rows][0:5]
                            y_angs.append(y_angles[y][3])
                            if (int(y_angles[y][1])%10 == 1):
                                y_angs_1.append(y_angles[y][3])
                                y_1 += 1
                            if ( (int(y_angles[y][1])%10 == 2) or (int(y_angles[y][1])%10 == 5) or (int(y_angles[y][1])%10 == 8)):
                                y_angs_2.append(y_angles[y][3])
                                y_2 += 1
                            if ( (int(y_angles[y][1])%10 == 3) or (int(y_angles[y][1])%10 == 6) or (int(y_angles[y][1])%10 == 9)):
                                y_angs_3.append(y_angles[y][3])
                                y_3 += 1
                                
                            #y_angs.append(math.cos(math.pi*y_angles[y][3]/180))
                            y += 1
                        else:    
                            l_angles[l][0:5] = all_angles[num_rows][0:5]
                            l_angs.append(l_angles[l][3])
                            #l_angs.append(math.cos(math.pi*l_angles[l][3]/180))
                            l += 1
                        i+=1

                    print(i,y,l,y_1,y_2,y_3)


        plt.title('Angle distribution in degrees')
        #plt.legend(frameon=False,bbox_to_anchor=(0.85, 0.5),loc='center',prop={'size': 15})
        #plt.xlabel('Angle in degrees',fontsize=19)
        #plt.ylabel(r'$ T (k_b / \epsilon_{LJ}) $',fontsize=19)
        n_y_1, bins_y_1, patches_y_1 = plt.hist(y_angs_1, n_bins, facecolor='blue',  alpha=0.5, density=True)
        n_y_2, bins_y_2, patches_y_2 = plt.hist(y_angs_2, n_bins, facecolor='red',   alpha=0.5, density=True)
        n_y_3, bins_y_3, patches_y_3 = plt.hist(y_angs_3, n_bins, facecolor='green', alpha=0.5, density=True)
        
        plt.savefig(filename+'_y.png')
        plt.show()
        plt.clf()



        #plt.title(filename+'_l')
        #n_l, bins_l, patches_l = plt.hist(l_angs, n_bins, facecolor='blue', alpha=0.5)
        #plt.savefig(filename+'_l.pdf')
        #plt.show()
        #print('y')
        #print(n_y, bins_y, patches_y)
        #print('l')
        #print(n_l, bins_l, patches_l)



    return()

