#! /usr/bin/env python3.7

from read_input   import read_filenames
from create_plots import plot_melting_curves_for_patch_bonds 
from constants    import plot_all 


pairlist,labels = read_filenames()

if (plot_all == True):
    plot_melting_curves_for_patch_bonds(pairlist,labels)

