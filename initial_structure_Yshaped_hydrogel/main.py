#! /usr/bin/python2.7

from importing_modules import *
from functions import *
from print_formatted import *
#from parseArguments import *
import argparse

######## Load many input #######
parser = argparse.ArgumentParser(description='generate configuration of Y-shapes')


#------1
parser.add_argument("-g","--generate",\
nargs="+",default=None,\
help="generate new configuration from scratsch.")


#------2
parser.add_argument("-r","--replot",nargs="+",\
help="Replots proexisting configurations from files of the form xyz.\
        input required: filename(str),n_molecules(int),box_limit(float)")


#------3
parser.add_argument("-s","--steady_state",nargs="+",\
help="generate after reached steady state.")
#------
args=parser.parse_args()


if args.generate: 

    #inititalsation
    n_molecules = int(args.generate[0])
    box_limit = float(args.generate[1])
    mass = 1.0
    dist = 0.96
    rad  = 0.56
    rot_threshold = 500
    
    ghost_mol = np.zeros((10,3))
    accpt_mol = np.zeros((10*n_molecules,3))
    
    ##----
    start_time = time.time()
    
    #first one is always accepted
    ghost_mol = gen_ghost(box_limit,dist,rad)
    while ( within_box(ghost_mol,box_limit) == False ):
        ghost_mol = gen_ghost(box_limit,dist,rad)
        #ghost_mol = perform_rand_rot(ghost_mol)
    
    
    for i in range(10):
        accpt_mol[i] = ghost_mol[i]
    
    
    
    
    mol = 1
    while (mol < n_molecules ):
    
        #----------------------generate ghost molecule--------------------
        ghost_mol = gen_ghost(box_limit,dist,rad)
        while ( within_box(ghost_mol,box_limit) == False ): 
            ghost_mol = gen_ghost(box_limit,dist,rad)
            #ghost_mol = perform_rand_rot(ghost_mol)
    
    
    
    
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
                ghost_mol = gen_ghost(box_limit,dist,rad)
                #ghost_mol = perform_rand_rot(ghost_mol)
            flag = they_overlap(ghost_mol,accpt_mol,mol,rad)
    
                
    
    
    
        #----------------------if not then add them to--------------------
        #----------------------the list of accepted-----------------------
        if (flag == False):
            for i in range(10):
                accpt_mol[10*mol+i] = ghost_mol[i]
        print mol
    
    
    
    
    
        #-----------------------move to next mol--------------------------
        mol +=1   
    
    
    
    end_time=time.time()
    print("\n time for execution: "+str(end_time-start_time)+" seconds \n")
    
    #---------------------------plot all------------------------------
    plot_all(accpt_mol,n_molecules,box_limit)    
    
    
    
    
    
    #--------------------------print all-------------------------------- 
    print_formatted_file(accpt_mol,n_molecules,box_limit,mass)
    
    with open('accepted.dat','w') as f:
        string_accpt_mol = str(accpt_mol).replace('[','').replace(']','')
        f.writelines(string_accpt_mol+"\n")
    
    #--save a copy to be read by load_plot.py----------------------------
    target_name = "rawdata_"+str(n_molecules)+"_"+str(box_limit)
    copyfile('accepted.dat',target_name)
    
    #---------------- rename the input_data.file ------------------------    
    src = "input_data.file"
    dst = "input_data"+"_"+str(n_molecules)+"_"+str(box_limit)+".file"
    copyfile(src,dst)
    


if args.replot:
    infile,n_molecules,box_limit = args.replot
    n_molecules = int(n_molecules)
    box_limit   = float(box_limit)

    #------------------- initialisation ---------------------
    accepted = np.zeros((10*n_molecules,3))
    i = 0
    
    #------------------ call from functions.py --------------
    with open (infile,'r') as g:
        for row in g.readlines():
            accepted[i][0],accepted[i][1],accepted[i][2] = row.split()
            i+=1
        plot_all(accepted,n_molecules,box_limit)









