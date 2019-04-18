#! /usr/bin/env python3.7

from read_input import read_filenames
from constants  import num_mol, box, cutoff, bins, binlength, num_den, vol_den 

import numpy as np
import matplotlib.pyplot as plt 
plt.rcParams.update({'font.size': 20})                                                                                                                                                 
plt.rcParams['errorbar.capsize']=4                                                                                                                                                     
from   matplotlib.pyplot import cm


filenames,temp_list = read_filenames()




fig = plt.figure(1)
ax  = fig.add_subplot(111)
color=iter(cm.viridis(np.linspace(0,1,len(filenames))))
# seismic
j=0 #for labels
for i in filenames:
    x_list  = []
    gr_list = []
    with open(i,'r') as f:
        all_lines = f.readlines()
        for l in all_lines:
            num,gr = l.split()
            num = binlength*float(num)
            #num = cutoff/bins*float(num)
            x_list.append(float(num))
            gr_list.append(float(gr))
    print(len(gr_list))
    print(len(x_list))
    c=next(color)
    plt.plot(x_list,gr_list,c=c,linewidth=3.0,label='T= '+str(temp_list[j]))
    j+=1



# plot extras
plt.title("Radial distribution function (rdf) for a system of "+str(num_mol)+" Y-shaped molecules")
plt.text(7.5, 2.0, str(num_mol)+' molecules in box', fontsize=22)
plt.text(7.5, 1.8, r'cubic box dimension '+str(box)+'$\sigma_{LJ}$', fontsize=22)
plt.text(7.5, 1.6, r'Number density '+str(num_den)+'$\sigma_{LJ}^{-3}$', fontsize=22)
plt.text(7.5, 1.4,  'Volume density '+str(vol_den), fontsize=22)
plt.legend(frameon=False)
plt.xlabel(r'r $(\sigma_{LJ})$')
plt.ylabel('g(r)')
plt.show()

