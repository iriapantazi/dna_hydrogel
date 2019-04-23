#! /usr/bin/python 


import time
import argparse
parser = argparse.ArgumentParser(description='generate nunchunks of 10 beads')
parser.add_argument("-g","--generate",nargs="+",default=None,help="generate new configuration from scratsch.")
parser.add_argument("-r","--replot",nargs="+",help="Replots what has been written in the rawdata files.")
args=parser.parse_args()


if args.generate: 

    from functions import gen_ghost,within_box,they_overlap,perform_rand_rot,plot_all
    from print_formatted import print_formatted_file
    from constants import mass,dist,rad
    import numpy as np
    from shutil import copyfile

    #inititalsation
    n_molecules = int(args.generate[0])
    box_limit = float(args.generate[1])/2.0

    rot_threshold = 500
    ghost_mol = np.zeros((10,3))
    accpt_mol = np.zeros((10*n_molecules,3))
    
    ##----
    start_time = time.time()
    
    #first one is always accepted
    ghost_mol = gen_ghost(box_limit,dist)
    while ( within_box(ghost_mol,box_limit) == False ):
        ghost_mol = gen_ghost(box_limit,dist)
    
    
    for i in range(10):
        accpt_mol[i] = ghost_mol[i]
    
    
    
    
    mol = 1
    while (mol < n_molecules ):
    
        #----------------------generate ghost molecule--------------------
        ghost_mol = gen_ghost(box_limit,dist)
        while ( within_box(ghost_mol,box_limit) == False ): 
            ghost_mol = gen_ghost(box_limit,dist)
    
        #----------------------check overlaping---------------------------
        #-------------------and perform a mx of 200 rots-------------------
        flag = they_overlap(ghost_mol,accpt_mol,mol,rad)
        attempt_num = 0
    
        while  (flag == True):
            attempt_num += 1
            if (attempt_num > rot_threshold):
                mol -= 1
                break;
            ghost_mol = perform_rand_rot(ghost_mol)
            while ( within_box(ghost_mol,box_limit) == False ):
                ghost_mol = gen_ghost(box_limit,dist)

            flag = they_overlap(ghost_mol,accpt_mol,mol,0.56)
    
                
    
    
    
        #----------------------if not then add them to--------------------
        #----------------------the list of accepted-----------------------
        if (flag == False):
            for i in range(10):
                accpt_mol[10*mol+i] = ghost_mol[i]
        print(mol)
    
    
    
    
    
        #-----------------------move to next mol--------------------------
        mol +=1   
    
    
    
    end_time=time.time()
    print("\n time for execution: "+str(end_time-start_time)+" seconds \n")
    
    #---------------------------plot all------------------------------
    plot_all(accpt_mol,n_molecules,box_limit)    
    
    
    
    
    
    #--------------------------print all-------------------------------- 
    print_formatted_file(accpt_mol,n_molecules,box_limit,mass)
    print('done')
    
    with open('accepted.dat','w') as f:
        string_accpt_mol = str(accpt_mol).replace('[','').replace(']','')
        f.writelines(string_accpt_mol+"\n")
    
    #--save a copy to be read by load_plot.py----------------------------
    target_name = "files/rawdata_"+str(n_molecules)+"_"+str((box_limit)*2)
    copyfile('accepted.dat',target_name)
    
    #---------------- rename the input_data.file ------------------------    
    src = "input_data.file"
    dst = "files/input_data_nunchucks_"+str(n_molecules)+"_"+str((box_limit)*2)+".file"
    copyfile(src,dst)
    


if args.replot:
    n_molecules,box_limit = args.replot
    n_molecules = int(n_molecules)
    box_limit   = float(box_limit)
    infiles     =  "files/rawdata_"+str(n_molecules)+"_"+str((box_limit)*2)

    #------------------- initialisation ---------------------
    accepted = np.zeros((10*n_molecules,3))
    i = 0
    
    #------------------ call from functions.py --------------
    with open (infile,'r') as g:
        for row in g.readlines():
            accepted[i][0],accepted[i][1],accepted[i][2] = row.split()
            i+=1
        plot_all(accepted,n_molecules,box_limit)









