#! /usr/bin/env python3.7    

def read_filenames():


    ## pairlocals for the 200 Y's in box of 29*29*29
    prefix =  "/home/iria/year_2/many_runs_for_melring_curves/pairlocal_200_29_1/pairlocal_T_"
    middle = ["0.10","0.15","0.20","0.25","0.30","0.33","0.36","0.37","0.40","0.42","0.45","0.50","0.52","0.60"]#,"0.70","0.80"]
    suffix =  "_N_200_box_29_run_100000_tau_num_1.dump"

    templist = middle
    pairlist = [prefix+middle[i]+suffix  for i in range(len(middle))]
    meltlist = [pairlist[i]+"_melt"  for i in range(len(pairlist))]
    print(templist,pairlist,meltlist)

    return(pairlist,templist,meltlist)




def read_time_all_pairs(pairlocal):
    from itertools import islice
    time_list = []
    nume_list = []
    with open(pairlocal,'r') as f: #, open (time_pairs,'w') as g:
        for line in f:
            if 'ITEM: TIMESTEP' in line:
                timestep   = int(''.join(islice(f, 1)))
                time_list.append(timestep)
            if 'ITEM: NUMBER OF ENTRIES' in line:
                numentries = int(''.join(islice(f, 1)))
                nume_list.append(numentries)
    return(time_list,nume_list)


# possible folders to look at:    


    ### pairlocals for the 700 Y's in box of 40*40*40
    #prefix =  "/home/iria/year_2/many_runs_for_melring_curves/pairlocal_700_40_1_2/pairlocal_T_"
    #middle = ["0.10","0.15","0.20","0.25","0.30","0.33","0.36","0.37","0.40","0.42","0.48","0.50","0.52","0.60","0.70","0.80"]
    #suffix =  "_N_700_box_40_run_100000_tau_num_2.dump"

    ## pairlocals for the 1000 Y's in box of 50*50*50
    #prefix   =  "/home/iria/year_2/many_runs_for_melring_curves/pairlocal_1000_50_1_2/pairlocal_T_"
    #pairlist = ["0.10","0.20","0.25","0.30","0.33","0.36","0.37","0.40","0.45","0.50","0.60","0.70"]
    #suffix   = [ "_N_1000_box_50_mix_1000000_run_100000_tau_num_1.dump"]


    #prefix   =  "/home/iria/year_2/soften_patch_angle_coefficient/y_l/pairlocal_T_"
    #pairlist = ["0.1","0.15","0.2","0.25","0.3","0.36","0.37","0.4","0.45","0.48","0.5","0.52","0.6","0.7"]
    #suffix   =  "_N_300_L_150_box_32_run_100000_tau_ang_coe_60_num_1.dump"

    #prefix   =  "/home/iria/year_2/soften_patch_angle_coefficient/y_y/pairlocal_T_"
    #pairlist = ["0.10","0.20","0.30","0.36","0.37","0.40","0.50","0.60","0.70","0.80"]
    #suffix   =  "_N_300_box_30_mix_200000_run_100000_tau_angle_coe_60_num_1.dump"

    #prefix   =  "/home/iria/year_2/aligned_run/pairlocals/pairlocal_T_"
    #pairlist = ["0.10","0.15","0.20","0.25","0.30","0.33","0.36","0.37","0.40","0.45","0.50","0.52","0.60","0.70","0.80"]
    #suffix   =  "_N_300_box_30_run_100000_tau_num_1_aligned.dump"

    #prefix   =  "/home/iria/year_2/many_runs_for_melring_curves/pairlocal_of_all_T/pairlocal_T_"
    #pairlist = ["0.10","0.15","0.20","0.25","0.30","0.33","0.36","0.37","0.40","0.45","0.50","0.52","0.60","0.70","0.80"]
    #suffix   =  "_N_300_box_30_run_100000_tau_num_1.dump"


    #~/year_2/many_runs_for_melring_curves/pairlocal_1000_50_1_2/pairlocal_T_0.10_N_1000_box_50_mix_1000000_run_100000_tau_num_1.dump
    ##
    #prefix   =  "/home/iria/year_2/aligned_run/pairlocal_T_"
    #pairlist = ["0.10","0.36","0.60"]
    #suffix   =  "_N_300_box_30_run_100000_tau_num_1_aligned.dump"



    ##
    #prefix   =  "/home/iria/year_2/many_runs_for_melring_curves/pairlocal_of_all_T/pairlocal_T_"
    #pairlist = ["0.10","0.20","0.25","0.30","0.33","0.36","0.37","0.40","0.45","0.50","0.52","0.60","0.70","0.80"]
    #suffix   =  "_N_300_box_30_run_100000_tau_num_4.dump"


    ## melting curve from year 1, unmixed
    #prefix   =  "/home/iria/year_2/many_runs_for_melring_curves/lammps_plain_melting_curves_from_year_one/pairlocal_"
    #pairlist = ["0.08","0.15","0.24","0.28","0.32","0.34","0.36","0.37","0.40","0.45","0.52","0.60","0.70"]
    #suffix   =  ".dump"

    ## second round of runs for the melting curves
    #prefix   =  "/home/iria/year_2/many_runs_for_melting_curves/pairlocal_of_all_T/pairlocal_T_"
    #pairlist = ["0.10","0.20","0.25","0.30","0.37","0.40","0.48","0.50","0.55","0.60","0.70","0.80"]
    #suffix   =  "_N_300_box_30_run_100000_tau_num_2.dump"




    ## variate mixing steps
    #prefix   =  "/home/iria/year_2/thermalise_for_mixing_to_compare_chris_mix/files/pairlocal_Ttherm_0.8_T_0.36_N_300_box_30_mix_"
    #pairlist = ["100","1000","10000"]
    #suffix   =  "_run_100000_tau.dumps"



    ## variate box size for N=100 molecules
    #prefix   =  "/home/iria/year_2/box_variate_dimensions_N_100/files/pairlocal_T_0.36_N_100_box_"
    #pairlist = ["19","20","22","24","25","26"]
    #suffix   =  "_mix_100_run_100000_tau.dumps"



    ## test the randomness with the initial run 
    ##
    #prefix   =  "/home/iria/year_2/randomness_of_initial_configuration/files/pairlocal_T_0.36_N_300_box_30_mix_"
    #pairlist = ["0","100","1000"]
    #suffix   =  "_run_100000_tau.dump"
    #templist = pairlist


    ## the old files which I had not mixed in the beginning 
    ## they are only for 300 Yshapes and I only have the _melt files
    ## there have to be additional changes in the way that the input is read
    ## the normalisation etc 
    ## in order to get correct results
    #prefix   =  "/home/iria/year_2/initial_Yshaped_pairlocal_files_year1/pairlocal_"
    #pairlist = ["0.08","0.15","0.24","0.28","0.32","0.34","0.36","0.37","0.40",\
    #            "0.45","0.52","0.60","0.70"]
    #suffix   =  "_dump"
    #templist = [pairlist[i][0:4] for i in range(len(pairlist))]


    ## variable box dimensions to test the convergence
    #prefix   =  "/home/iria/year_2/box_variate_dimensions/files/pairlocal_T_0.36_N_100_box_"
    #pairlist = ["20","22","24","25"]
    #suffix   =  "_mix_100_run_100000_tau.dumps"
    #templist = [pairlist[i][0:1] for i in range(len(pairlist))]


