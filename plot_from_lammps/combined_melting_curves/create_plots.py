#! /usr/bin/env python3.7 

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})
plt.rcParams['errorbar.capsize']=4
from constants import number_density, volume_density
import numpy as np
import numpy.random

def plot_melting_curves_for_patch_bonds(pairlist,labels):
    
    all_x_list = []
    all_y_list = []

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    i = 0
    
    
    data = pd.read_csv(pairlist[0]) 
    ax.errorbar(data['T'], data['frac'] , yerr=data['err'], marker='o', fmt='-o',label=labels[i])
    all_x_list.extend(   data['T'].values.tolist())
    all_y_list.extend(data['frac'].values.tolist())

    for pair in pairlist[1:len(pairlist)]:
        i+=1
        tmp_data = pd.read_csv(pair) 
        ax.errorbar(tmp_data['T'], tmp_data['frac'] , yerr=tmp_data['err'], marker='o', fmt='-o',label=labels[i])
        data = pd.concat((data,tmp_data))
        print(tmp_data['T'])
        print(tmp_data['T'].values.tolist())
        all_x_list.extend(   tmp_data['T'].values.tolist())
        all_y_list.extend(tmp_data['frac'].values.tolist())


    print(len(all_x_list),len(all_y_list))
    print(all_x_list)
    print(all_y_list)

    
    plt.title('Melting curves for various initial configurations',fontsize=18)
    plt.xlabel(r'$ T (k_b / \epsilon_{LJ}) $',fontsize=18)
    plt.ylabel('Association Degree',fontsize=18)
    ax.text(0.1, 0.3, 'number density = '+str(number_density), fontsize=14)
    ax.text(0.1, 0.2, 'volume density = '+str(volume_density), fontsize=14)
    plt.legend()
    plt.show()    
    fig.clf()

    plt.scatter(data['T'],data['frac'],c=numpy.arange(len(data['T'])),cmap='viridis',alpha=0.8)
    plt.title('Melting curves for various initial configurations',fontsize=18)
    plt.xlabel(r'$ T (k_b / \epsilon_{LJ}) $',fontsize=18)
    plt.ylabel('Mixed Association Degree and average curve',fontsize=18)
    ax.text(0.1, 0.3, 'number density = '+str(number_density), fontsize=14)
    ax.text(0.1, 0.2, 'volume density = '+str(volume_density), fontsize=14)
    #plt.legend()
    plt.show()    
    fig.clf()
    

    #-- it works!
    x = all_x_list #[3,4,5,6,7,8,9,9]
    y = all_y_list #[6,5,4,3,2,1,1,2]
    plt.scatter(x,y)
    #plt.plot(x,y)
    x, y = zip(*sorted((xVal, np.mean([yVal for a, yVal in zip(x, y) if xVal==a])) for xVal in set(x)))
    plt.plot(x,y)
    print(x,y)
    plt.show()

    return() 

