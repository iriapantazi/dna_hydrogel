#! /usr/bin/env python3.7    


def read_filenames():

    # 300_30_1
    prefix = "rdf_300_30_1/rdf_N_300_box_30_timesteps_200000_T_"
    middle = ["0.10","0.15","0.20","0.25","0.30","0.33","0.36","0.37","0.40","0.42","0.45","0.50","0.60","0.70","0.80"]
    suffix = ".rdf"

    filenames = [prefix+str(middle[i])+suffix for i in range(len(middle))]
    temp_list = middle





    return(filenames,temp_list)

# extra files



    ## 1000_50_1
    #prefix = "rdf_1000_50_1/rdf_N_1000_box_50_timesteps_200000_T_"
    #middle = ["0.10","0.15","0.20","0.25","0.30","0.33","0.36","0.37","0.40","0.42","0.45","0.48","0.50","0.60","0.70"]
    #suffix = ".rdf"
