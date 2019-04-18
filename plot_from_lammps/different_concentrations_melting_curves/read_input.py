#! /usr/bin/env python3.7    


def read_filenames():


    prefix   =  ["300_30","700_40","1000_50","200_29"]
    suffix   =  ".csv"
    pairlist = [prefix[i]+suffix  for i in range(len(prefix))]

    labels  = prefix
    #labels = ["300_30_1","300_30_2","300_30_3","300_30_4","300_30_5"]#,"1000_50_1","1000_50_2"]


    return(pairlist,labels)




