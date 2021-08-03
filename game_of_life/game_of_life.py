''''
this is the simuation practice of game of life 

name :  Amzad hossain rafi 
date :  3rd aug 2021

simulution perameaters :
--grid-size (optional) 
--intarval (optional) 
--mov-file (optional) 
--glider   (optional) 

command :
1.conda activate Project 
2.python game_of_life.py
3.python game_of_life.py --grid-size (value) --interval (value) --glider 



'''


#import 
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, argparse




#veriables 

ON = 255
OFF = 0
vals = [ON, OFF]


#random grid genetetor function 
def random(N):

    ''' randomly choice value between on and off and create a 1D listthn reshape it to NxN shape  '''

    x=np.random.choice(vals, N*N, p=[0.1,0.9]).reshape(N,N)
    return x 

    # plt.imshow(x, interpolation="nearest")
    # plt.show()

def Glider(i,j,grid):
    x= np.array([[0,0,255],[255,0,0], [255,0,255]])
    grid[i:i+3 , j:j+3]=x
    # plt.imshow(grid, interpolation="nearest")
    # plt.show()

# grid=np.zeros(N*N).reshape(N,N)
# Glider(2,2,grid)
def update(farmeNum, img, grid, N):


    new_grid=grid.copy()
    for i in range(N):
        for j in range(N):

            #for loop updating and  chking the edgs 
            #impt must understand this part 
            total= int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                            grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
                            grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
                            grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/255)
            
            #condition for on off cells 
            # apply Conway's rules
            if grid[i,j] == ON:
                if(total < 2) or (total > 3):
                    new_grid[i,j]= OFF
            else:
                if total == 3:
                    new_grid[i,j]= ON

    img.set_data(new_grid)
    grid[:]=new_grid[:]
    return img,




    # apply Conway's rules
    


def main():

    '''macking arg parser for the tarminal value '''


    paser= argparse.ArgumentParser(" game of life simulation ")
    paser.add_argument('--grid-size', dest='N',required=False)
    paser.add_argument('--mov-file', dest='movfile',required=False)
    paser.add_argument('--interval', dest='interval',required=False)
    paser.add_argument('--glider', action='store_true', required=False)
    args = paser.parse_args()



    #copy 
    # set grid size

    N = 200                            #N defult value 
    if args.N and int(args.N) > 8:
        N = int(args.N)
        
    # set animation update interval
    updateInterval = 50                # defult value 
    if args.interval:
        updateInterval = int(args.interval)

    # declare grid
    grid = np.array([])
    # check if "glider" demo flag is specified
    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        Glider(1, 1, grid)
    # elif args.gosper:
    #     grid = np.zeros(N*N).reshape(N, N)
    #     addGosperGliderGun(10, 10, grid)
    else:
        # populate grid with random on/off - more off than on
        grid = random(N)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 10,
                                  interval=updateInterval,
                                  save_count=50)

  
    # set output file
    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()

if __name__ == '__main__':
    main()