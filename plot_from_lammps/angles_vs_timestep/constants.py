#! /usr/bin/env python3.7

n_bins = 100
tau_submulti      = float(0.005)
skip_info_lines   = 7 
timestep_to_start = 19860000

num_y = 300
num_l = 0
beads_per_y = 10
beads_per_l =  6
angs_per_y = 9
angs_per_l = 4




# unchanged -- prakseis
num_atoms    =  beads_per_y * num_y + beads_per_l * num_l
num_angles_y =   angs_per_y * num_y   
num_angles_l =   angs_per_l * num_l  
num_angles   = num_angles_l + num_angles_y
num_beads_y  = num_y * beads_per_y
num_beads_l  = num_l * beads_per_l

## maybe useless
#read_atom_type  = 1
#num_bins = 300  # example
#r_cut    = 15 # example 
#box_size = 30  # example (-15,+15)
#normalisation = 4*pi**num_molecules*
