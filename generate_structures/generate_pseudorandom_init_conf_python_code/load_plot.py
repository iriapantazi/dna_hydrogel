#! /usr/bin/python
# Iria Pantazi 20180516
#
# since pickle does not work as expected, load_plot will load the plots from the 
# input file given, and will replot them. It's faster that recalculating.
# The date are taken from rawdata_${Nmolecules}_${boxSize}

from importing_modules import *
from  graphing_modules import *
from functions         import plot_all
import argparse


parser = argparse.ArgumentParser(description='.')
parser.add_argument("-r","--replot",nargs="+",help="Replots proexisting \
configurations from files of the form xyz.")
args=parser.parse_args()



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
































    #-------------------- read input ------------------------
    #try:
    #    infile      = str(raw_input('Input: '              ))
    #    n_molecules = int(raw_input('number of molecules: '))
    #    box_limit   = int(raw_input('box limit: '          ))
    #except ValueError:
    #    print "Not a proper input file"
