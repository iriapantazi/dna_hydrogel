#! /usr/bin/python


import math
import numpy as np
from numpy  import linalg as LA
from random import random
from pyquaternion import Quaternion

#
#np.set_printoptions(threshold=np.nan)
#import scipy
#import random
#


#--- changed for nunchunks
def within_box(ghost,box_lim):
    flag = True
    toBreak = False
    for i in range(0,10,9): #to check only the edge beads
        for j in range(3):
            if (abs(ghost[i][j] > box_lim)):
                print("out")
                flag = False
                toBreak = True
                break
        if (toBreak == True):
            break
    return(flag);
#-----------------------------------------------------------




#--- no need to change
def perform_rand_rot(ghost):
    new_ghost = np.zeros((10,3))
    ran_rot = Quaternion.random()

    for i in range(10):
        new_ghost[i] = ran_rot.rotate(ghost[i])

    return(new_ghost);
#-----------------------------------------------------------









#--- changed for nunchunks
def they_overlap(ghost,accepted,mol,rad):
    overlap = False
    lista = list(range(10))#[0,1,2,4,5,7,8]    
    break_flag = False


    for k in range(mol):
        for i in lista:
            for j in lista:
                dist = np.linalg.norm(accepted[10*k+i]-ghost[j])
                if (dist < 2*rad ):
                    break_flag  = True
                    overlap = True
                    break;
            if (break_flag == True):
                break
        if (break_flag == True):
            break


    return(overlap);
#-----------------------------------------------------------










#--- changed for nunchunks
def gen_ghost(box_limit,dist):
    ghost = np.zeros((10,3))

    #center 0
    ghost[0][0] = 0
    ghost[0][1] = 0
    ghost[0][2] = 0
        
    #tail of the next 9 beads
    for i in range(1,10,1):
        ghost[i]     = ghost[0]
        ghost[i][2] += i*dist

    
    #preform random rotation 
    ran_rot = Quaternion.random()
    for i in range(10):
        ghost[i] = ran_rot.rotate(ghost[i])

    #preform random displacement
    ran_dis_x = (random() - 0.5e0)*2.0*(box_limit)
    ran_dis_y = (random() - 0.5e0)*2.0*(box_limit)
    ran_dis_z = (random() - 0.5e0)*2.0*(box_limit)

    for i in range(10):
        ghost[i][0] += ran_dis_x
        ghost[i][1] += ran_dis_y
        ghost[i][2] += ran_dis_z

    return(ghost);
#-----------------------------------------------------------










#--- changed for nunchunks
def plot_all(accepted,n_mol,box_lim):
    import matplotlib.pyplot as plt
    #import itertools
    import pylab
    
    
    #from   itertools import product,imap
    #from   matplotlib.backends.backend_pdf import PdfPages
    import matplotlib.pylab as pylab
    params = {'legend.fontsize': 'large',
              'figure.figsize': (11, 6),
              'axes.labelsize': 'x-large',
              'axes.titlesize':'x-large',
              'xtick.labelsize':'x-large',
              'ytick.labelsize':'x-large'}
    pylab.rcParams.update(params)
    import matplotlib.cm as cm
    
    
    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
    from mpl_toolkits.axes_grid1.inset_locator import mark_inset
    
    from mpl_toolkits.mplot3d.proj3d import proj_transform
    from matplotlib.text import Annotation
    
    from mpl_toolkits.mplot3d import Axes3D

    colour = []
    x_list = [row[0] for row in accepted]
    y_list = [row[1] for row in accepted]
    z_list = [row[2] for row in accepted]




    cols = cm.seismic(np.linspace(0, 10, 10*n_mol)/10)

    #for i in range(n_mol):
    #    colour.extend(("c","m","m","r","m","m","r","m","m","r")) if \
    #                                               (i % 2 ==1) else \
    #    colour.extend(("c","m","m","b","m","m","b","m","m","b"))
    
    fig = plt.figure()
    ax  = fig.add_subplot(111, projection='3d')
    ax.scatter(x_list,y_list,z_list,c=cols,marker='o',s=350)
    ax.set_xlim(-box_lim,box_lim)
    ax.set_ylim(-box_lim,box_lim)
    ax.set_zlim(-box_lim,box_lim)
    ax.grid(False)
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    #ax.set_title("Y-DNAs of types A (shades of red) and B (shades of blue)")
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    
    
    plt.show() 
    

    return();
#-----------------------------------------------------------
#-----------------------------------------------------------
