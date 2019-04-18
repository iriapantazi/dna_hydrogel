#! /usr/bin/env python3.7

from read_input   import read_filenames, read_time_all_pairs
from create_plots import plot_melting_curves_for_patch_bonds, errors_in_steady_state_for_convergence
from constants    import association, error_comparison

pairlist,templist,meltlist = read_filenames()

plot_melting_curves_for_patch_bonds(pairlist,templist,association)

if (error_comparison == True):
    errors_in_steady_state_for_convergence(meltlist,templist)
