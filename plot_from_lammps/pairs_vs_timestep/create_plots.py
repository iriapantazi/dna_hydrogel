#! /usr/bin/env python3.7 

import os
import os.path
from itertools import islice
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})                                                                                                                                                 
plt.rcParams['errorbar.capsize']=4
from matplotlib.pyplot import cm
from constants import tau_submul,num_atoms,normalisation,association
import statistics
import numpy as np

def errors_in_steady_state_for_convergence(meltlist,templist):

    """ print the errors in slots of 100 final 
        steps and prove that there is convergence, 
        hence the steady state has been found"""

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    color=iter(cm.viridis(np.linspace(0,1,len(meltlist))))


    all_times = [i for i in range(5,-1,-1)]                
    k = 0

    for melt in meltlist:
        fin_tim = []
        all_ave = []
        all_err = []
        with open(melt,'r') as f:
            all_lines = f.readlines()
            steps = int(100)

            for times in all_times: #range(3,-1,-1):

                steady_state_list = []
                strt = - times   * steps -1
                stop = -(times+1)* steps -1
                for i in range(strt,stop,-1):
                    the_line           = all_lines[i]
                    temp_time,temp_num = the_line.split() 
                    steady_state_list.append(int(temp_num)/normalisation)
                average = statistics.mean( steady_state_list)
                error   = statistics.stdev(steady_state_list)
                #print (strt,stop,average,error)
                """ Now plot them. """
                all_ave.append(average)
                all_err.append(error)
                fin_tim.append(temp_time)

        c=next(color)
        plt.plot(fin_tim,all_err,label=str(templist[k]),c=c)
        k+=1
        #plt.errorbar(all_times,all_ave,yerr=all_err, capsize=3 , fmt='o', ecolor='g', capthick=2)
    plt.title("Standard deviation of the association degree for every 5000 tau.")
    plt.legend()
    plt.show()

    return()
#------------------------------------------------------------------------





def plot_melting_curves_for_patch_bonds(pairlist,templist,association):
    meltlist = []
    

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    n = len(pairlist)
    color=iter(cm.viridis(np.linspace(0,1,n)))
    i = 0 

    for pair in pairlist:
        sep = "_" 
        name = (pair,"melt")
        meltName = sep.join(name)
        meltlist.append(meltName)

        plot_legend = []
        time_list   = []        
        count_list  = []
        count = 0

        if (not os.path.isfile(meltName)) :
            with open (pair,'r') as f, open (meltName,'w') as h:
                for line in f:    
                    if 'ITEM: TIMESTEP' in line:
                        timestep = int(''.join(islice(f, 1)))
                        timestep = timestep * tau_submul 
                        time_list.append(timestep)
                    if 'ITEM: NUMBER OF ENTRIES' in line: 
                        numentries = int(''.join(islice(f, 1)))
                        #print numentries
                        if (numentries > 0):
                            compute_bonds = ''.join(islice(f,5,numentries+5))
                            with open ("temp.dat",'w') as g:
                                g.write("%s" %(compute_bonds))
                             
                            with open ("temp.dat",'r') as g:
                                count = 0
                                for templine in g.readlines():
                                    # atom1 atom2 distance energy force
                                    c1,c2,c3,c4,c5 = templine.split()
                                    if (float(c4) < 0) :   #if ((int(c1)%10 == 0) or (int(c1)%7 == 0) or (int(c1)%4 == 0)) :
                                        count +=1   
                                count_list.append(count)
                            os.remove('temp.dat')
                        else:
                            count_list.append(count)
                        h.write("%d %d \n" %(timestep, count) )
            
        else:
            print (meltName)
            with open (meltName,'r') as k:
                for line in k.readlines():
                    a,b = line.split()
                    time_list.append(float(a))
                    count_list.append(float(b))


        c= next(color)
        ax.plot(time_list,count_list,c=c,linewidth=3,label="T="+str(templist[i]))
        i +=1
    plt.subplots_adjust(right=0.9)
    ax.legend(frameon=False,bbox_to_anchor=(1.05, 0.5),loc='center')
    ax.set_xscale('log')
    plt.title('Simulations for the steady state of the Y-shapes.')
    plt.xlabel(r'Timestep $(\tau)$')
    plt.ylabel('Number of bonds formed')
    #---------------------- save the plots ---------------------------
    fig.savefig("all_melting_curves_for_patches_only.pdf", bbox_inches='tight')
    plt.show()
    plt.clf()


    if (association == True):
        plot_association_degree(meltlist,templist)

    return() 




def plot_association_degree(melt,temp):

    i = 0
    bond_list = []
    error_list = []


    for tem in temp:
        komponenten = melt[i]
        bonded,bonded_error  = take_better_statistics(komponenten,tem)
        bond_list.append(bonded) 
        error_list.append(bonded_error)
        i += 1


    #------------ plot pairnumbers vs temperature ----------------------

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    plt.title('Association for the system of Y-shapes')
    plt.xlabel(r'$ T (k_b / \epsilon_{LJ}) $')
    plt.ylabel('Fraction of bonds created')
    plt.errorbar(temp,bond_list,yerr=error_list, capsize=3 , fmt='o', ecolor='g', capthick=2)
    #plt.scatter(temp,bond_list, c=temp, cmap='viridis',s=20)
    fig.savefig("melting_curve_temps.pdf", bbox_inches='tight')
    plt.show()
    plt.clf()

    return()





def take_better_statistics(komponenten,temp):

    """ Here will consider by default only the 
        final 100 steps of the pairlocal file.
        It does not check the connvergence of the 
        association degree plots, but simply 
        produces the melting curve, also known 
        as association degree plot."""

    with open(komponenten,'r') as f:    
        #print("T,abs,ave,err")
        #print(temp)
        steady_state_list = []
        all_lines = f.readlines()
        steps = int(100)
        for i in range(-1,-steps-1,-1):
            the_line           = all_lines[i]
            temp_time,temp_num = the_line.split() 
            steady_state_list.append(int(temp_num)/normalisation)
        average = statistics.mean( steady_state_list)
        error   = statistics.stdev(steady_state_list)
        print(temp,",",average*normalisation,",",average,",",error)
    return(average,error)
#-----------------------------------------------------------------------




