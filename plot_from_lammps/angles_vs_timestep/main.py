#! /usr/bin/env python3.7

from read_input import read_filenames
#from constants  import tau_submulti, num_molecules, num_atoms, skip_info_lines, read_atom_type 
from create_plots import create_to_plot_file 



filenames = read_filenames()
for fname in filenames:
    create_to_plot_file(fname)


