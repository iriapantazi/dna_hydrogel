#! /usr/bin/env python

""" Written by: Iria Pantazi
    First created: 2018/01/10
    Last updated:  2019/10/05
"""

import time
import argparse
parser = argparse.ArgumentParser(description='generate Y+L made of 10+6 beads')
parser.add_argument("-g", "--generate", nargs="+", default=None, help="generate new configuration (Y, L, box).")
parser.add_argument("-r", "--replot", nargs="+", help="Replots what has been written in the rawdata files.")
args=parser.parse_args()

import math
import numpy as np
from numpy  import linalg as LA
from random import random
from pyquaternion import Quaternion

import os
import subprocess
import glob
import sys
import json # for printing arrays in files and loading back again
import shutil
from shutil import move
from shutil import copyfile
import scipy
import matplotlib as mpl
import matplotlib.pyplot as plt
import timeit

import itertools
import pylab
from   itertools import product #,imap
from   matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'large',
          'figure.figsize': (11, 6),
          'axes.labelsize': 'x-large',
          'axes.titlesize':'x-large',
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.mplot3d.proj3d import proj_transform
from matplotlib.text import Annotation
from mpl_toolkits.mplot3d import Axes3D

# unchanged parameters for the beads:
mass = 1.0
dist = 0.96
rad  = 0.56

def print_formatted_file(acc,n_molecules,n_linkers,box_limit,mass):
    with open ("input_data.file","w") as g:
        g.write("Y:1,2,3 L:4,5,6,7,8   \n")
        g.write("1=central, 2=beads, 3=patches   \n")
        g.write("4=patches, 5,6,7,8=beads \n\n")
        y_shapes  = 10*n_molecules
        y_bonds   =  9*n_molecules
        y_angles  =  9*n_molecules
        atoms     = 10*n_molecules+6*n_linkers
        bonds     =  9*n_molecules+5*n_linkers
        angles    =  9*n_molecules+4*n_linkers
        dihedrals =  0*n_molecules+0*n_linkers
        impropers =  0*n_molecules+0*n_linkers
        g.write("%d  atoms          \n" % atoms    )
        g.write("%d  bonds          \n" % bonds    ) 
        g.write("%d  angles         \n" % angles   ) 
        g.write("%d  dihedrals      \n" % dihedrals) 
        g.write("%d  impropers    \n\n" % impropers)
        g.write("4  atom types     \n") 
        g.write("2  bond types     \n") 
        g.write("4  angle types    \n") 
        g.write("0  dihedral types \n") 
        g.write("0  improper types \n\n")
        g.write("-%f %f xlo xhi  \n"   % (box_limit,box_limit))
        g.write("-%f %f ylo yhi  \n"   % (box_limit,box_limit))
        g.write("-%f %f zlo zhi  \n\n" % (box_limit,box_limit))
        g.write("Masses\n\n")
        g.write("\t 1 %s \n"   % mass)
        g.write("\t 2 %s \n"   % mass)
        g.write("\t 3 %s \n"   % mass)
        g.write("\t 4 %s \n\n" % mass)
        g.write("Atoms \n\n")
        for i in range(0,n_molecules,1):
            # N molecule-tag atom-type q x y z nx ny nz
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+1,i+1,1,  \
            acc[10*i  ][0],acc[10*i  ][1],acc[10*i  ][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+2,i+1,2,  \
            acc[10*i+1][0],acc[10*i+1][1],acc[10*i+1][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+3,i+1,2,  \
            acc[10*i+2][0],acc[10*i+2][1],acc[10*i+2][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+5,i+1,2,  \
            acc[10*i+4][0],acc[10*i+4][1],acc[10*i+4][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+6,i+1,2,  \
            acc[10*i+5][0],acc[10*i+5][1],acc[10*i+5][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+8,i+1,2,  \
            acc[10*i+7][0],acc[10*i+7][1],acc[10*i+7][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+9,i+1,2,  \
            acc[10*i+8][0],acc[10*i+8][1],acc[10*i+8][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+4 ,i+1,3,  \
            acc[10*i+3][0],acc[10*i+3][1],acc[10*i+3][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+7 ,i+1,3,  \
            acc[10*i+6][0],acc[10*i+6][1],acc[10*i+6][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+10,i+1,3,  \
            acc[10*i+9][0],acc[10*i+9][1],acc[10*i+9][2],0,0,0))
        #for i in range(n_molecules,n_molecules+n_linkers,1):
        for i in range(0,n_linkers,1):
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(y_shapes+6*i+1,\
            n_molecules+i+1,4,acc[y_shapes+6*i  ][0],acc[y_shapes+6*i  ][1],\
                              acc[y_shapes+6*i  ][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(y_shapes+6*i+2,\
            n_molecules+i+1,5,acc[y_shapes+6*i+1][0],acc[y_shapes+6*i+1][1],\
                              acc[y_shapes+6*i+1][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(y_shapes+6*i+3,\
            n_molecules+i+1,6,acc[y_shapes+6*i+2][0],acc[y_shapes+6*i+2][1],\
                              acc[y_shapes+6*i+2][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(y_shapes+6*i+4,\
            n_molecules+i+1,7,acc[y_shapes+6*i+3][0],acc[y_shapes+6*i+3][1],\
                              acc[y_shapes+6*i+3][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(y_shapes+6*i+5,\
            n_molecules+i+1,8,acc[y_shapes+6*i+4][0],acc[y_shapes+6*i+4][1],\
                              acc[y_shapes+6*i+4][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(y_shapes+6*i+6,\
            n_molecules+i+1,4,acc[y_shapes+6*i+5][0],acc[y_shapes+6*i+5][1],\
                              acc[y_shapes+6*i+5][2],0,0,0))
        g.write("\n\n")
        g.write("Bonds \n\n")
        bnd1=1
        bnd2=2
        for i in range(0,n_molecules,1):
            # N bond-type atom1-atom2
            g.write("\t %d %d %d %d \n" % (9*i+1,bnd1,10*i+1,10*i+2 ))
            g.write("\t %d %d %d %d \n" % (9*i+2,bnd1,10*i+2,10*i+3 ))
            g.write("\t %d %d %d %d \n" % (9*i+3,bnd1,10*i+1,10*i+5 ))
            g.write("\t %d %d %d %d \n" % (9*i+4,bnd1,10*i+5,10*i+6 ))
            g.write("\t %d %d %d %d \n" % (9*i+5,bnd1,10*i+1,10*i+8 ))
            g.write("\t %d %d %d %d \n" % (9*i+6,bnd1,10*i+8,10*i+9 ))
            g.write("\t %d %d %d %d \n" % (9*i+7,bnd2,10*i+3,10*i+4 ))
            g.write("\t %d %d %d %d \n" % (9*i+8,bnd2,10*i+6,10*i+7 ))
            g.write("\t %d %d %d %d \n" % (9*i+9,bnd2,10*i+9,10*i+10))
        #for i in range(n_molecules,n_molecules+n_linkers,1):
        for i in range(0,n_linkers,1):
            g.write("\t %d %d %d %d \n" % (y_bonds+5*i+1,bnd2,\
                                           y_shapes+6*i+1,y_shapes+6*i+2 ))
            g.write("\t %d %d %d %d \n" % (y_bonds+5*i+2,bnd1,\
                                           y_shapes+6*i+2,y_shapes+6*i+3 ))
            g.write("\t %d %d %d %d \n" % (y_bonds+5*i+3,bnd1,\
                                           y_shapes+6*i+3,y_shapes+6*i+4 ))
            g.write("\t %d %d %d %d \n" % (y_bonds+5*i+4,bnd1,\
                                           y_shapes+6*i+4,y_shapes+6*i+5 ))
            g.write("\t %d %d %d %d \n" % (y_bonds+5*i+5,bnd2,\
                                           y_shapes+6*i+5,y_shapes+6*i+6 ))
        g.write("\n\n")
        g.write("Angles \n\n")
        ang1 = int(1) # 1=120 degrees 
        ang2 = int(2) # 2=180 degrees
        ang3 = int(3) # 3=variate-will be determined in in.run file
        ang4 = int(4) # 3=variate-will be determined in in.run file
        for i in range(0,n_molecules,1):
            # N angle-type atom1-atom2(central)-atom3
            g.write("\t %d %d %d %d %d \n" % (9*i+1,ang1,10*i+2,10*i+1,10*i+5 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+2,ang1,10*i+5,10*i+1,10*i+8 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+3,ang1,10*i+8,10*i+1,10*i+2 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+4,ang2,10*i+1,10*i+2,10*i+3 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+5,ang4,10*i+2,10*i+3,10*i+4 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+6,ang2,10*i+1,10*i+5,10*i+6 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+7,ang4,10*i+5,10*i+6,10*i+7 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+8,ang2,10*i+1,10*i+8,10*i+9 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+9,ang4,10*i+8,10*i+9,10*i+10))
        #for i in range(n_molecules,n_molecules+n_linkers,1):
        for i in range(0,n_linkers,1):   
            g.write("\t %d %d %d %d %d \n" % (y_angles+4*i+1,ang3,\
                y_shapes+6*i+1,y_shapes+6*i+2,y_shapes+6*i+3 ))
            g.write("\t %d %d %d %d %d \n" % (y_angles+4*i+2,ang2,\
                y_shapes+6*i+2,y_shapes+6*i+3,y_shapes+6*i+4 ))
            g.write("\t %d %d %d %d %d \n" % (y_angles+4*i+3,ang2,\
                y_shapes+6*i+3,y_shapes+6*i+4,y_shapes+6*i+5 ))
            g.write("\t %d %d %d %d %d \n" % (y_angles+4*i+4,ang3,\
                y_shapes+6*i+4,y_shapes+6*i+5,y_shapes+6*i+6 ))
    return();


def within_box(ghost,box_lim):
    flag = True
    toBreak = False
    for i in range(3,10,3):
        for j in range(3):
            if (abs(ghost[i][j]) > box_lim):
                print("not in")
                flag = False
                toBreak = True
                break
        if (toBreak == True):
            break
    return(flag);

def perform_rand_rot_lnk(ghost_lnk):
    new_ghost_lnk = np.zeros((6,3))
    ran_rot = Quaternion.random()
    for i in range(6):
        new_ghost_lnk[i] = ran_rot.rotate(ghost_lnk[i])
    return(new_ghost_lnk);          

def perform_rand_rot(ghost):
    new_ghost = np.zeros((10,3))
    ran_rot = Quaternion.random()
    for i in range(10):
        new_ghost[i] = ran_rot.rotate(ghost[i])
    return(new_ghost);

def they_overlap(ghost,accepted,mol,rad):
    overlap = False
    lista = [0,1,2,4,5,7,8]    
    break_flag = False
    for k in range(mol):
        for i in lista:
            for j in lista:
                dist = math.sqrt((accepted[10*k+i][0]-ghost[j][0])**2 + \
                                 (accepted[10*k+i][1]-ghost[j][1])**2 + \
                                 (accepted[10*k+i][2]-ghost[j][2])**2 )
                if (dist < 3*rad ):
                    break_flag  = True
                    overlap = True
                    break;
            if (break_flag == True):
                break
        if (break_flag == True):
            break
    return(overlap);

def they_overlap_w_mol(ghost_lnk,accepted_mol,mol,rad):
    overlap    = False
    lista_mol  = [0,1,2,4,5,7,8]    
    lista_lnk  = [1,2,3,4]
    break_flag = False
    for k in range(mol):
        for i in lista_mol:
            for j in lista_lnk:
                dist = math.sqrt((accepted_mol[10*k+i][0]-ghost_lnk[j][0])**2 + \
                                 (accepted_mol[10*k+i][1]-ghost_lnk[j][1])**2 + \
                                 (accepted_mol[10*k+i][2]-ghost_lnk[j][2])**2 )
                if (dist < 3*rad ):
                    break_flag  = True
                    overlap = True
                    break;
            if (break_flag == True):
                break
        if (break_flag == True):
            break
    return(overlap);

def they_overlap_w_lnk(ghost_lnk,accepted_lnk,lnk,rad):
    overlap = False
    lista = [1,2,3,4]    
    break_flag = False
    for k in range(lnk):
        for i in lista:
            for j in lista:
                dist = math.sqrt((accepted_lnk[6*k+i][0]-ghost_lnk[j][0])**2 + \
                                 (accepted_lnk[6*k+i][1]-ghost_lnk[j][1])**2 + \
                                 (accepted_lnk[6*k+i][2]-ghost_lnk[j][2])**2 )
                if (dist < 3*rad ):
                    break_flag  = True
                    overlap = True
                    break;
            if (break_flag == True):
                break
        if (break_flag == True):
            break
    return(overlap);

def within_box_lnk(ghost_lnk,box_lim):    
    flag    = True
    toBreak = False
    i_list  = [0,5]
    for i in i_list:
        for j in range(3):
            if (abs(ghost_lnk[i][j]) > box_lim):
                print("not in")
                flag = False
                toBreak = True
                break
        if (toBreak == True):
            break
    return(flag);

def gen_ghost_lnk(box_limit,dist,rad):
    ghost_lnk = np.zeros((6,3))
    ran_rot   = Quaternion.random()
    #---orientation along z-axis----------------------------
    ghost_lnk[1][2] = 1 * dist
    ghost_lnk[2][2] = 2 * dist   
    ghost_lnk[3][2] = 3 * dist
    ghost_lnk[4][2] = 4 * dist
    ghost_lnk[5][2] = 5 * dist
    #---perform random rotation------------------------------
    for i in range(6):
        ghost_lnk[i] = ran_rot.rotate(ghost_lnk[i])
    #---preform random displacement--------------------------
    ran_dis_x = (random() - 0.5e0)*2.0*(box_limit)
    ran_dis_y = (random() - 0.5e0)*2.0*(box_limit)
    ran_dis_z = (random() - 0.5e0)*2.0*(box_limit)
    for i in range(6):
        ghost_lnk[i][0] += ran_dis_x
        ghost_lnk[i][1] += ran_dis_y
        ghost_lnk[i][2] += ran_dis_z
    return(ghost_lnk)

def gen_ghost(box_limit,dist,rad):
    ghost = np.zeros((10,3))
    rot120y = Quaternion(axis=[0, 1, 0], angle=2*math.pi/3)
    rot240y = Quaternion(axis=[0, 1, 0], angle=4*math.pi/3)
    #center 0
    ghost[0][0] = 0
    ghost[0][1] = 0
    ghost[0][2] = 0
    #tail z 1
    ghost[1][0] = ghost[0][0]   
    ghost[1][1] = ghost[0][1]
    ghost[1][2] = ghost[0][2]+dist
    #tail z 2
    ghost[2][0] = ghost[0][0]
    ghost[2][1] = ghost[0][1]
    ghost[2][2] = ghost[0][2]+dist*2
    #tail z 3 patch
    ghost[3][0] = ghost[0][0]
    ghost[3][1] = ghost[0][1]
    ghost[3][2] = ghost[0][2]+dist*2+rad
    ghost[4] = rot120y.rotate(ghost[1])#tail x 4
    ghost[5] = rot120y.rotate(ghost[2])#tail x 5
    ghost[6] = rot120y.rotate(ghost[3])#tail x 6 patch
    ghost[7] = rot240y.rotate(ghost[1])#tail y 7
    ghost[8] = rot240y.rotate(ghost[2])#tail y 8
    ghost[9] = rot240y.rotate(ghost[3])#tail y 9 patch
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
    #print(ghost)
    return(ghost);

#def plot_one(ghost):
#    x_list = [row[0] for row in ghost]
#    y_list = [row[1] for row in ghost]
#    z_list = [row[2] for row in ghost]
#    fig = plt.figure()
#    ax  = fig.add_subplot(111, projection='3d')
#    ax.scatter(x_list,y_list,z_list,marker='o',s=600)
#    plt.show()
#    return();

def plot_all(accepted,n_mol,n_lnk,box_lim):
    colour = []
    x_list = [row[0] for row in accepted]
    y_list = [row[1] for row in accepted]
    z_list = [row[2] for row in accepted]
    for i in range(n_mol):
        colour.extend(("c","m","m","r","m","m","r","m","m","r")) if \
                                                   (i % 2 ==1) else \
        colour.extend(("c","m","m","r","m","m","r","m","m","r"))
    for i in range(n_lnk):
        colour.extend(("b","m","m","m","m","b")) 
    fig = plt.figure()
    ax  = fig.add_subplot(111, projection='3d')
    ax.scatter(x_list,y_list,z_list,c=colour,marker='o',s=10) 
    ax.set_xlim(-box_lim,box_lim)
    ax.set_ylim(-box_lim,box_lim)
    ax.set_zlim(-box_lim,box_lim)
    ax.set_title("Y-shapes and linkers configuation represented by beads")
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show() 
    return(); 





#-----------------------------------------------------------
if args.generate:
    
    n_molecules = int(args.generate[0])
    n_linkers   = int(args.generate[1])
    box_limit   = float(args.generate[2])/2

    rot_threshold = 500
    ghost_mol = np.zeros((10,3))
    accpt_mol = np.zeros((10*n_molecules,3))
    ghost_lnk = np.zeros((6,3))
    accpt_lnk = np.zeros((6*n_linkers,3))
    
    #--------------------------------timing--------------------------------
    start_time = time.time()
    #------------first one is always accepted------------------------------
    ghost_mol = gen_ghost(box_limit,dist,rad)
    while ( within_box(ghost_mol,box_limit) == False ):
        ghost_mol = gen_ghost(box_limit,dist,rad)
    
    for i in range(10):
        accpt_mol[i] = ghost_mol[i]
    #--------------------molecules----------------------------------------
    mol = 1
    while (mol < n_molecules ):
        #----------------------generate ghost molecule--------------------
        ghost_mol = gen_ghost(box_limit,dist,rad)
        while ( within_box(ghost_mol,box_limit) == False ): 
            ghost_mol = gen_ghost(box_limit,dist,rad)
        #---check overlaping and perform a max of rot_threshold rots------
        flag = they_overlap(ghost_mol,accpt_mol,mol,rad)    
        attempt_num = 0
        while  (flag == True):
            attempt_num += 1
            if (attempt_num > rot_threshold):
                mol -= 1
                break;
            ghost_mol = perform_rand_rot(ghost_mol)
            while ( within_box(ghost_mol,box_limit) == False ):
                ghost_mol = gen_ghost(box_limit,dist,rad)
            flag = they_overlap(ghost_mol,accpt_mol,mol,rad)
    
        #------if not overlapping then add them to the list of accepted---
        if (flag == False):
            for i in range(10):
                accpt_mol[10*mol+i] = ghost_mol[i]
        print(mol)
        #-----------------------move to next mol--------------------------
        mol +=1   
    #----------------------linkers----------------------------------------
    lnk = 0
    while (lnk < n_linkers ):
        #----------------------generate ghost linker----------------------
        ghost_lnk = gen_ghost_lnk(box_limit,dist,rad)
        while ( within_box_lnk(ghost_lnk,box_limit) == False ): 
            ghost_lnk = gen_ghost_lnk(box_limit,dist,rad)
        #----check overlaping and perform a max of rot_threshold rots-----
        if (lnk >= 1):
            flag1 = they_overlap_w_lnk(ghost_lnk,accpt_lnk,lnk,rad)    
        else:
            flag1 = True
        flag2     = they_overlap_w_mol(ghost_lnk,accpt_mol,mol,rad)
        attempt_num = 0           
        while  ((flag1 == True) or (flag2 == True)):
            attempt_num += 1
            if (attempt_num > rot_threshold):
                lnk -= 1
                break;
            ghost_lnk = perform_rand_rot_lnk(ghost_lnk)
            while ( within_box_lnk(ghost_lnk,box_limit) == False ):
                ghost_lnk = gen_ghost_lnk(box_limit,dist,rad)
            flag1 = they_overlap_w_lnk(ghost_lnk,accpt_lnk,lnk,rad)        
            flag2 = they_overlap_w_mol(ghost_lnk,accpt_mol,mol,rad)
        #----if not overlapping then add them to the list of accepted------
        if ((flag1 == False) and (flag2 == False)):
            for i in range(6):
                accpt_lnk[6*lnk+i] = ghost_lnk[i]
        print(lnk)
        #-----------------------move to next mol--------------------------
        lnk += 1
    #---------------------------timing------------------------------------
    end_time=time.time()
    print("\n time for execution: "+str(end_time-start_time)+" seconds \n")
    #---------------------------plot all----------------------------------
    accpt_all = np.concatenate((accpt_mol,accpt_lnk))
    plot_all(accpt_all,n_molecules,n_linkers,box_limit)    
    #--------------------------print all----------------------------------
    print_formatted_file(accpt_all,n_molecules,n_linkers,box_limit,mass)
    with open('accepted.dat','w') as f:
        string_accpt_all = str(accpt_all).replace('[','').replace(']','')
        f.writelines(string_accpt_all+"\n")
    #---------------- rename the input_data.file -------------------------   
    src = "input_data.file"
    dst = "files/input_data_"+str(n_molecules)+"_"+str(n_linkers)+"_"+str(int(box_limit))+"_variate_angle_coefficient.file"
    copyfile(src,dst)
