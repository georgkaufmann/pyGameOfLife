"""
pyGameOfLife
library for Conway's Game of Life
2024-02-09
Georg Kaufmann
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

#================================#
def gridInit(N,M):
    """
    Conway's Game of Life
    initial state, only dead cells only
    input:
     N,M       - grid dimensions
    output:
     grid      - 2D grid field initialised with zeros (dead cells)
    use:
     grid = libGameOfLife.gridInit(N,M)
    """
    grid = np.zeros(N*M).reshape(N,M)
    return grid


#================================#
def gridUpdate(grid):
    """
    Conway's Game of Life
    update function (cyclic across boundaries)
    input:
     grid      - 2D grid field
    outnput:
     grid      - 2D grid field (updated)
    use:
     grid = libGameOfLife.gridUpdate(grid)
    """
    N = grid.shape[0]
    M = grid.shape[1]
    # first, make a copy of the old grid
    newgrid = grid.copy()
    # then, apply Conway's rules to each cell
    for i in range(N):
        for j in range(M):
            total = 0
            # top row of neighbors
            total += np.roll(grid,(1,1),(0,1))[i,j]   #grid[i-1,j-1]
            total += np.roll(grid,(1,0),(0,1))[i,j]   #grid[i-1,j]
            total += np.roll(grid,(1,-1),(0,1))[i,j]  #grid[i-1,j+1]
            # middle row of neighbors
            total += np.roll(grid,(0,1),(0,1))[i,j]   #grid[i,j-1]
            total += np.roll(grid,(0,-1),(0,1))[i,j]  #grid[i,j+1]
            # bottom row of neighbors
            total += np.roll(grid,(-1,1),(0,1))[i,j]  #grid[i+1,j-1]
            total += np.roll(grid,(-1,0),(0,1))[i,j]  #grid[i+1,j]
            total += np.roll(grid,(-1,-1),(0,1))[i,j] #grid[i+1,j+1]
            # fate of living cell
            if grid[i,j]  == 1: 
                if (total < 2) or (total > 3): 
                    newgrid[i,j] = 0 
            # fate of dead cell
            else: 
                if total == 3: 
                    newgrid[i,j] = 1
    #grid[:] = newgrid[:]
    return newgrid
    
    
#================================#
def gridPlot(grid,itime,size=(6,6),plot=False):
    """
    Conway's Game of Life
    function plots grid, uses own color table
    input:
     grid      - NxM grid
     itime     - time counter
    output:
     (to figure)
    use:
     libGameOfLife.gridPlot(grid,itime)
    """
    filename = "work/GoL-"+f"{itime:04}.png"
    colors = [( 0.9 , 0.9 , 0.9 ),( 1 , 0 , 0 )]
    colors = [( 1, 1 , 1 ),( 1 , 0 , 0 )]
    myCmap = matplotlib.colors.ListedColormap(colors)
    plt.figure()
    plt.title(str(itime))
    plt.imshow(grid,cmap=myCmap)
    plt.axis('off')
    plt.savefig(filename)
    plt.tight_layout()
    if (not plot):
        plt.close()
    return



#================================#
def addBlock(xoffset,yoffset,grid):
    """
    Conway's Game of Life
    Block object (stable)
    11
    11
    input:
     xoffset,yoffset - offset positions of object
     grid            - 2D grid field 
    output:
     grid            - updated 2D grid field
    use:
     grid = libGameOfLife.addBlock(xoffset,yoffset,grid)
    """
    GoLobject = np.array([[1,1],[1,1]])
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
def addBeehive(xoffset,yoffset,grid):
    """
    Conway's Game of Life
    Beehive object (stable)
    010
    101
    101
    010
    input:
     xoffset,yoffset - offset positions of object
     grid            - 2D grid field 
    output:
     grid            - updated 2D grid field
    use:
     grid = libGameOfLife.addBlock(xoffset,yoffset,grid)
    """
    GoLobject = np.array([[0,1,0],[1,0,1],[1,0,1],[0,1,0]])
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
def addBarge(xoffset,yoffset,grid):
    """
    Conway's Game of Life
    Barge object (stable)
    0010
    0101
    1010
    0100
    input:
     xoffset,yoffset - offset positions of object
     grid            - 2D grid field 
    output:
     grid            - updated 2D grid field
    use:
     grid = libGameOfLife.addBlock(xoffset,yoffset,grid)
    """
    GoLobject = np.array([[0,0,1,0],[0,1,0,1],[1,0,1,0],[0,1,0,0]])
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
def addEater(xoffset,yoffset,grid):
    """
    Conway's Game of Life
    Eater object (stable)
    1100
    1010
    0010
    0010
    0011
    input:
     xoffset,yoffset - offset positions of object
     grid            - 2D grid field 
    output:
     grid            - updated 2D grid field
    use:
     grid = libGameOfLife.addBlock(xoffset,yoffset,grid)
    """
    GoLobject = np.array([[1,1,0,0],[1,0,1,0],[0,0,1,0],[0,0,1,1]])
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
def addBlinker(xoffset,yoffset,grid):
    """
    Conway's Game of Life
    Blinker object (oscillator)
    111
    input:
     xoffset,yoffset - offset positions of object
     grid            - 2D grid field 
    output:
     grid            - updated 2D grid field
    use:
     grid = libGameOfLife.addBlinker(xoffset,yoffset,grid)
    """
    GoLobject = np.array([[1,1,1]])
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
def addBipole(xoffset,yoffset,grid):
    """
    Conway's Game of Life
    Bipole object (oscillator)
    1100
    1000
    0001
    0011
    input:
     xoffset,yoffset - offset positions of object
     grid            - 2D grid field 
    output:
     grid            - updated 2D grid field
    use:
     grid = libGameOfLife.addBipole(xoffset,yoffset,grid)
    """
    GoLobject = np.array([[1,1,0,0],
                          [1,0,0,0],
                          [0,0,0,1],
                          [0,0,1,1]])
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
def addTripole(xoffset,yoffset,grid):
    """
    Conway's Game of Life
    Tripole object (oscillator)
    11000
    10000
    01010
    00001
    00011
    input:
     xoffset,yoffset - offset positions of object
     grid            - 2D grid field 
    output:
     grid            - updated 2D grid field
    use:
     grid = libGameOfLife.addBipole(xoffset,yoffset,grid)
    """
    GoLobject = np.array([[1,1,0,0,0],
                          [1,0,0,0,0],
                          [0,1,0,1,0],
                          [0,0,0,0,1],
                          [0,0,0,1,1]])
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
def addPulsator(xoffset,yoffset,grid):
    """
    Conway's Game of Life
    Pulsator object (oscillator)
    0010000100
    1101111011
    0010000100
    input:
     xoffset,yoffset - offset positions of object
     grid            - 2D grid field 
    output:
     grid            - updated 2D grid field
    use:
     grid = libGameOfLife.addBipole(xoffset,yoffset,grid)
    """
    GoLobject = np.array([[0,0,1,0,0,0,0,1,0,0],
                          [1,1,0,1,1,1,1,0,1,1],
                          [0,0,1,0,0,0,0,1,0,0]])
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
def addGlider(xoffset,yoffset,grid):
    """
    Conway's Game of Life
    glider object (moving)
    010
    001
    111
    input:
     xoffset,yoffset - offset positions of object
     grid            - 2D grid field 
    output:
     grid            - updated 2D grid field
    use:
     grid = libGameOfLife.addGlider(xoffset,yoffset,grid)
    """
    GoLobject = np.array([[0,1,0],
                          [0,0,1],
                          [1,1,1]])
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
def addLWSpaceship(xoffset,yoffset,grid):
    """
    Conway's Game of Life
    Light-weight spaceship object (moving)
    01111
    10001
    00001
    10010
    input:
     xoffset,yoffset - offset positions of object
     grid            - 2D grid field 
    output:
     grid            - updated 2D grid field
    use:
     grid = libGameOfLife.addBipole(xoffset,yoffset,grid)
    """
    GoLobject = np.array([[0,1,1,1,1],
                          [1,0,0,0,1],
                          [0,0,0,0,1],
                          [1,0,0,1,0]])
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
def addRandomField(grid,p=[0.8,0.2],seed=20220217):
    """
    Conway's Game of Life
    fill the grid with a random distribution of 0 an 1
    """
    # define object as list of strings
    rng = np.random.default_rng(seed=20220217)
    grid = rng.choice([0,1],(grid.shape),p=[0.8,0.2])
    return grid


#================================#
def addGosperGlider(xoffset,yoffset, grid):
    """
    Conway's Game of Life
    define a Gosper-Glider
    and fit string pattern into 2D integer grid
    """
    # adds a Gosper Glider Gun
    Logo = [
    ['00000000000000000000000000000000000000'],
    ['00000000000000000000000001000000000000'],
    ['00000000000000000000000101000000000000'],
    ['00000000000001100000011000000000000110'],
    ['00000000000010001000011000000000000110'],
    ['01100000000100000100011000000000000000'],
    ['01100000000100010110000101000000000000'],
    ['00000000000100000100000001000000000000'],
    ['00000000000010001000000000000000000000'],
    ['00000000000001100000000000000000000000'],
    ['00000000000000000000000000000000000000']
    ]
    # get no of strings (nrows) and characters in string (ncols)
    nrows = len(Logo)
    ncols = len(Logo[0][0])
    GoLobject = np.zeros([nrows,ncols],dtype='int')
    #print(GoLobject.shape)
    # loop over strings and characters, fill into 2D array
    irow=0
    for line in Logo:
        icol=0
        for letter in line[0]:
            #print(letter,' ',end='')
            #print(irow,icol)
            GoLobject[irow,icol] = letter
            icol += 1
        irow += 1
    # pass 2D array into larger grid
    grid[xoffset:xoffset+GoLobject.shape[0], yoffset:yoffset+GoLobject.shape[1]] = GoLobject
    return grid


#================================#
#================================#
#================================#