#! /usr/bin/python2.7

from importing_modules import *
from  graphing_modules import *


def within_box(ghost,box_lim):
    flag = True
    toBreak = False
    for i in range(3,10,3):
        for j in range(3):
            #print(i,j)
            if (abs(ghost[i][j]) > box_lim):
                print("in")
                flag = False
                toBreak = True
                break
        if (toBreak == True):
            break

    return(flag);
#-----------------------------------------------------------










def perform_rand_rot(ghost):
    new_ghost = np.zeros((10,3))
    ran_rot = Quaternion.random()

    for i in range(10):
        new_ghost[i] = ran_rot.rotate(ghost[i])

    return(new_ghost);
#-----------------------------------------------------------










def they_overlap(ghost,accepted,mol,rad):
    overlap = False
    lista = [0,1,2,4,5,7,8]    
    break_flag = False


    for k in range(mol):
        for i in lista:
            for j in lista:
                dist = math.sqrt((accepted[10*k+i][0]-ghost[j][0])**2 + \
                                 (accepted[10*k+i][1]-ghost[j][1])**2 + \
                                 (accepted[10*k+i][2]-ghost[j][2])**2 )
                if (dist < 3*rad ):
                    break_flag  = True
                    overlap = True
                    break;
            if (break_flag == True):
                break
        if (break_flag == True):
            break


    return(overlap);
#-----------------------------------------------------------










def gen_ghost(box_limit,dist,rad):
    ghost = np.zeros((10,3))
    rot120y = Quaternion(axis=[0, 1, 0], angle=2*math.pi/3)
    rot240y = Quaternion(axis=[0, 1, 0], angle=4*math.pi/3)

    #center 0
    ghost[0][0] = 0#(random() - 0.5e0)*2.0*(box_limit)
    ghost[0][1] = 0#(random() - 0.5e0)*2.0*(box_limit)
    ghost[0][2] = 0#(random() - 0.5e0)*2.0*(box_limit)
        
    #tail z 1
    ghost[1][0] = ghost[0][0]   
    ghost[1][1] = ghost[0][1]
    ghost[1][2] = ghost[0][2]+dist

    #tail z 2
    ghost[2][0] = ghost[0][0]
    ghost[2][1] = ghost[0][1]
    ghost[2][2] = ghost[0][2]+dist*2

    #tail z 3 patch
    ghost[3][0] = ghost[0][0]
    ghost[3][1] = ghost[0][1]
    ghost[3][2] = ghost[0][2]+dist*2+rad

    ghost[4] = rot120y.rotate(ghost[1])#tail x 4
    ghost[5] = rot120y.rotate(ghost[2])#tail x 5
    ghost[6] = rot120y.rotate(ghost[3])#tail x 6 patch
    ghost[7] = rot240y.rotate(ghost[1])#tail y 7
    ghost[8] = rot240y.rotate(ghost[2])#tail y 8
    ghost[9] = rot240y.rotate(ghost[3])#tail y 9 patch
    
    #preform random rotation 
    ran_rot = Quaternion.random()
    for i in range(10):
        ghost[i] = ran_rot.rotate(ghost[i])

    #preform random displacement
    ran_dis_x = (random() - 0.5e0)*2.0*(box_limit)
    ran_dis_y = (random() - 0.5e0)*2.0*(box_limit)
    ran_dis_z = (random() - 0.5e0)*2.0*(box_limit)

    for i in range(10):
        ghost[i][0] += ran_dis_x
        ghost[i][1] += ran_dis_y
        ghost[i][2] += ran_dis_z

    #print(ghost)
    return(ghost);
#-----------------------------------------------------------










def plot_one(ghost):
    
    x_list = [row[0] for row in ghost]
    y_list = [row[1] for row in ghost]
    z_list = [row[2] for row in ghost]

    fig = plt.figure()
    ax  = fig.add_subplot(111, projection='3d')
    ax.scatter(x_list,y_list,z_list,marker='o',s=600)
    plt.show() 

    return();
#-----------------------------------------------------------










def plot_all(accepted,n_mol,box_lim):

    colour = []
    x_list = [row[0] for row in accepted]
    y_list = [row[1] for row in accepted]
    z_list = [row[2] for row in accepted]

    #x_list_a = x_list[0:1500]
    #y_list_a = y_list[0:1500]
    #z_list_a = z_list[0:1500]
    #x_list_b = x_list[1500:3000]
    #y_list_b = y_list[1500:3000]
    #z_list_b = z_list[1500:3000]

    #cols_b = cm.Blues(np.linspace(0, 10, 1000)/5)
    #cols_l = cm.Reds(np.linspace(0, 6,  900)/4)


    cols = cm.seismic(np.linspace(0, 10, 10*n_mol)/8)

    for i in range(n_mol):
        colour.extend(("c","m","m","r","m","m","r","m","m","r")) if \
                                                   (i % 2 ==1) else \
        colour.extend(("c","m","m","b","m","m","b","m","m","b"))
    
    fig = plt.figure()
    ax  = fig.add_subplot(111, projection='3d')
    ax.scatter(x_list,y_list,z_list,c=cols,marker='o',s=30)
    ax.set_xlim(-box_lim,box_lim)
    ax.set_ylim(-box_lim,box_lim)
    ax.set_zlim(-box_lim,box_lim)
    ax.grid(False)
    ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
    #ax.set_title("Y-DNAs of types A (shades of red) and B (shades of blue)")
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    
    
    plt.show() 
    
    
    #
    #pl.dump(fig,file('test10.pickle','wb'))

    return();
#-----------------------------------------------------------















