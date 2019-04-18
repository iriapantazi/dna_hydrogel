#! /usr/bin/env python3.7    


def read_filenames():

    ## 200 in 29
    prefix   =  "pairs_T_errors_200_29_"
    middle   =  ["1"]
    suffix   =  ".csv"
    labels = ["200_29_1"]

    ## 1000 in 50
    #prefix   =  "pairs_T_errors_1000_50_"
    #middle   =  ["1","2"]
    #suffix   =  ".csv"
    #labels = ["1000_50_1","1000_50_2"]

    ## 700 in 40
    #prefix   =  "pairs_T_errors_700_40_"
    #middle   =  ["1","2"]
    #suffix   =  ".csv"

    ## 300 in 30
    #prefix   =  "pairs_T_errors_300_30_"
    #middle   =  ["1","2","3","4","5"]
    #suffix   =  ".csv"

    pairlist = [prefix+middle[i]+suffix  for i in range(len(middle))]

    #pairlist.append("pairs_T_errors_1000_50_1.csv")
    #pairlist.append("pairs_T_errors_1000_50_2.csv")
    #pairlist.append("pairs_T_errors_300_30_aligned.csv")
    #pairlist = []
    #pairlist.append("pairs_T_errors_300_30_angle_coe_90_1.csv")
    #pairlist.append("pairs_T_errors_300_30_angle_coe_60_1.csv")

    #labels = ["300_30_ang_90","300_30_ang_60"]
    labels = ["300_30_1","300_30_2","300_30_3","300_30_4","300_30_5"]#,"1000_50_1","1000_50_2"]

    print(pairlist)
    #print(templist)

    return(pairlist,labels)




