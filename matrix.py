import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import numpy as np
import random
import math

L= 64
Q=.42
R=.5
no_of_particles=0
grid = np.zeros((L,L))
repeat = L*L
no_of_reactions = 0

def getRandom():
    return random.random()


def moveUp(i,j):
    if(i==0):
        return L-1,j
    return i-1,j

def moveRight(i,j):
    if(j==L-1):
        return i,0
    return i,j+1

def moveDown(i,j):
    if(i==L-1):
        return 0,j
    return i+1,j

def moveLeft(i,j):
    if(j==0):
        return i,L-1
    return i,j-1

def diffusion(i,j):
    global grid
    if(grid[i][j]>=1):
        direction=getRandom()
        if(direction<.25):
            grid[i][j]-=1
            a,b = moveLeft(i,j)
            grid[a][b]+=1
        if(direction>=.25 and direction<.50):
            grid[i][j]-=1
            a,b = moveUp(i,j)
            grid[a][b]+=1
        if(direction>=.50 and direction<.75):
            grid[i][j]-=1
            a,b = moveRight(i,j)
            grid[a][b]+=1
        if(direction>=.75):
            grid[i][j]-=1
            a,b = moveDown(i,j)
            grid[a][b]+=1    


def reaction(i,j):
    global no_of_particles
    global grid
    global repeat
    global no_of_reactions
    if(grid[i][j]>1):
        # print(i,j)
        number_of_reaction = math.floor(grid[i][j]/2)
        # print("No.of rxn: ", number_of_reaction)
        for c in range(number_of_reaction):
            type_of_reaction = getRandom()
            if(type_of_reaction<.5):
                grid[i][j]+=1
                no_of_particles+=1
                # print("creation : ",no_of_particles)
            else:
                grid[i][j]-=1
                no_of_particles-=1
                # print("annihilation : ",no_of_particles)
        number_of_topple = grid[i][j]
        # print("no. f topples and coordinate value:" ,grid[i][j], number_of_topple)
        for b in range(int(number_of_topple)):
            diffusion(i,j)
        no_of_reactions=0    
        # for i in range(L):
            # for j in range(L):
                # print(grid[i][j],end="\t")
            # print()        
        # print()
        # print()
    no_of_reactions+=1

N=1000
for i in range(L):
    for j in range(L):
        if(getRandom()>Q):
            grid[i][j]=1
            no_of_particles+=1
#         print(grid[i][j], end="\t")
#     print()        
# print()
# print()
initial_particle= no_of_particles
# print("Initial:", no_of_particles)
for i in range(L):
    for j in range(L):
        diffusion(i,j)

# for i in range(L):
    # for j in range(L):
        # print(grid[i][j], end="\t")
    # print()    
plt.figure(figsize=(100,100))
# print()
# print()


for k in range(N):
    # print("iteration number: ", k)
    for i in range(L):
        for j in range(L):
            reaction(i,j)
    if(no_of_reactions>=repeat):
        for i in range(L):
            for j in range(L):
                diffusion(i,j)
    # print("final : ", no_of_particles)
    # for i in range(L):
        # for j in range(L):
            # print(grid[i][j], end="\t")
        # print()    
    plt.scatter(k,no_of_particles/repeat,color= "green")
    # print() 
    # print()

# colors = ['blue', 'green', 'yellow', 'red']
# cmap = ListedColormap(colors)
# # Plot the matrix as a heatmap using Seaborn
# sns.heatmap(matrix, cmap=cmap)

# Add title and labels
plt.title('2D Matrix Visualization')
plt.xlabel('# Iterations')
plt.ylabel('particle density')
# Show the plot
plt.show()
