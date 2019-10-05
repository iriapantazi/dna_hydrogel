#! /usr/bin/python

from importing_modules import *
from functions import *
from print_formatted import *
#from parseArguments import *



#inititalsation
n_molecules = 10
box_limit = float(15)/2.0
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
target_name = "rawdata_"+str(n_molecules)+"_"+str(box_limit*2)
copyfile('accepted.dat',target_name)

#---------------- rename the input_data.file ------------------------    
src = "input_data.file"
dst = "input_data"+"_"+str(n_molecules)+"_"+str(box_limit*2)+".file"
copyfile(src,dst)





