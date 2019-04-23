#! /usr/bin/python2.7

from shutil import copyfile

def print_formatted_file(acc,n_molecules,box_limit,mass):

    with open ("input_data.file","w") as g:
        g.write("LAMMPS nunchunk data file \n\n")

        atoms  =   10*n_molecules
        bonds  =    9*n_molecules
        angles =    8*n_molecules
        dihedrals = 0*n_molecules
        impropers = 0*n_molecules

        g.write("%d  atoms          \n" % atoms    )
        g.write("%d  bonds          \n" % bonds    ) 
        g.write("%d  angles         \n" % angles   ) 
        g.write("%d  dihedrals      \n" % dihedrals) 
        g.write("%d  impropers    \n\n" % impropers)

        g.write("10 atom types     \n") 
        g.write("9  bond types     \n") 
        g.write("8  angle types    \n") 
        g.write("0  dihedral types \n") 
        g.write("0  improper types \n\n")

        g.write("-%f %f xlo xhi  \n"   % (box_limit,box_limit))
        g.write("-%f %f ylo yhi  \n"   % (box_limit,box_limit))
        g.write("-%f %f zlo zhi  \n\n" % (box_limit,box_limit))

        g.write("Masses\n\n")
        g.write("\t 1  %s \n"   % mass)
        g.write("\t 2  %s \n"   % mass)
        g.write("\t 3  %s \n"   % mass)
        g.write("\t 4  %s \n"   % mass)
        g.write("\t 5  %s \n"   % mass)
        g.write("\t 6  %s \n"   % mass)
        g.write("\t 7  %s \n"   % mass)
        g.write("\t 8  %s \n"   % mass)
        g.write("\t 9  %s \n"   % mass)
        g.write("\t 10 %s \n\n" % mass)


        
        g.write("Atoms \n\n")
        for i in range(0,n_molecules,1): 
             
            # N molecule-tag atom-type q x y z nx ny nz
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+1, i+1,1, acc[10*i  ][0],acc[10*i  ][1],acc[10*i  ][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+2, i+1,2, acc[10*i+1][0],acc[10*i+1][1],acc[10*i+1][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+3, i+1,3, acc[10*i+2][0],acc[10*i+2][1],acc[10*i+2][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+4, i+1,4, acc[10*i+3][0],acc[10*i+3][1],acc[10*i+3][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+5, i+1,5, acc[10*i+4][0],acc[10*i+4][1],acc[10*i+4][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+6, i+1,6, acc[10*i+5][0],acc[10*i+5][1],acc[10*i+5][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+7, i+1,7, acc[10*i+6][0],acc[10*i+6][1],acc[10*i+6][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+8, i+1,8, acc[10*i+7][0],acc[10*i+7][1],acc[10*i+7][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+9, i+1,9, acc[10*i+8][0],acc[10*i+8][1],acc[10*i+8][2],0,0,0))
            g.write("\t %d %d %d %s %s %s %d %d %d \n"%(10*i+10,i+1,10,acc[10*i+9][0],acc[10*i+9][1],acc[10*i+9][2],0,0,0))

        g.write("\n\n")
        g.write("Bonds \n\n")
        for i in range(0,n_molecules,1):   
            # N bond-type atom1-atom2
            g.write("\t %d %d %d %d \n" % (9*i+1,1,10*i+1,10*i+2 ))
            g.write("\t %d %d %d %d \n" % (9*i+2,2,10*i+2,10*i+3 ))
            g.write("\t %d %d %d %d \n" % (9*i+3,3,10*i+3,10*i+4 ))
            g.write("\t %d %d %d %d \n" % (9*i+4,4,10*i+4,10*i+5 ))
            g.write("\t %d %d %d %d \n" % (9*i+5,5,10*i+5,10*i+6 ))
            g.write("\t %d %d %d %d \n" % (9*i+6,6,10*i+6,10*i+7 ))
            g.write("\t %d %d %d %d \n" % (9*i+7,7,10*i+7,10*i+8 ))
            g.write("\t %d %d %d %d \n" % (9*i+8,8,10*i+8,10*i+9 ))
            g.write("\t %d %d %d %d \n" % (9*i+9,9,10*i+9,10*i+10))


        g.write("\n\n")
        g.write("Angles \n\n")
        for i in range(0,n_molecules,1):
            # N angle-type atom1-atom2(central)-atom3
            g.write("\t %d %d %d %d %d \n" % (9*i+1,1,10*i+1,10*i+2,10*i+3 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+2,2,10*i+2,10*i+3,10*i+4 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+3,3,10*i+3,10*i+4,10*i+5 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+4,4,10*i+4,10*i+5,10*i+6 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+5,5,10*i+5,10*i+6,10*i+7 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+6,6,10*i+6,10*i+7,10*i+8 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+7,7,10*i+7,10*i+8,10*i+9 ))
            g.write("\t %d %d %d %d %d \n" % (9*i+8,8,10*i+8,10*i+9,10*i+910))

    return();
