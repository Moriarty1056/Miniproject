import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import numpy as np
import random
import math

L= 16
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
        number_of_reaction = math.floor(grid[i][j]/2)
        for c in range(number_of_reaction):
            type_of_reaction = getRandom()
            if(type_of_reaction<.5):
                grid[i][j]+=1
                no_of_particles+=1
            else:
                grid[i][j]-=1
                no_of_particles-=1
        number_of_topple = grid[i][j]
        for b in range(int(number_of_topple)):
            diffusion(i,j)
        no_of_reactions=0    
    no_of_reactions+=1

N=1
for i in range(L):
    for j in range(L):
        if(getRandom()>Q):
            grid[i][j]=1
            no_of_particles+=1
        
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'orange', 'purple']
cmap =ListedColormap(colors)
plt.figure(figsize=(100,100))
for i in range(L):
    for j in range(L):
        color = colors[int(grid[i, j])]  
        plt.scatter(j, i, color=color, s=100, edgecolor='black')

plt.xlim(-1, L )
plt.ylim(-1, L )

legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='0', markerfacecolor='blue', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='1', markerfacecolor='green', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='2', markerfacecolor='red', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='3', markerfacecolor='cyan', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='4', markerfacecolor='magenta', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='5', markerfacecolor='yellow', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='6', markerfacecolor='orange', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='7', markerfacecolor='purple', markersize=10)]

plt.legend(handles=legend_elements, loc='upper left', title='Value')


plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('2-D Grid')

plt.grid(True)
plt.show()

for i in range(L):
    for j in range(L):
        diffusion(i,j)
plt.figure(figsize=(100,100))

for i in range(L):
    for j in range(L):
        color = colors[int(grid[i, j])]  
        plt.scatter(j, i, color=color, s=100, edgecolor='black')


plt.xlim(-1, L )
plt.ylim(-1, L )

legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='0', markerfacecolor='blue', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='1', markerfacecolor='green', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='2', markerfacecolor='red', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='3', markerfacecolor='cyan', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='4', markerfacecolor='magenta', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='5', markerfacecolor='yellow', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='6', markerfacecolor='orange', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='7', markerfacecolor='purple', markersize=10)]


plt.legend(handles=legend_elements, loc='upper left', title='Value')


plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('2-D Grid')

plt.grid(True)
plt.show()


for k in range(N):
    for i in range(L):
        for j in range(L):
            reaction(i,j)
    if(no_of_reactions>=repeat):
        for i in range(L):
            for j in range(L):
                diffusion(i,j)
    plt.figure(figsize=(100,100))

    for i in range(L):
        for j in range(L):
            color = colors[int(grid[i, j])]
            plt.scatter(j, i, color=color, s=100, edgecolor='black')
            
    plt.xlim(-1, L )
    plt.ylim(-1, L )

    legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='0', markerfacecolor='blue', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='1', markerfacecolor='green', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='2', markerfacecolor='red', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='3', markerfacecolor='cyan', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='4', markerfacecolor='magenta', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='5', markerfacecolor='yellow', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='6', markerfacecolor='orange', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='7', markerfacecolor='purple', markersize=10)]

    plt.legend(handles=legend_elements, loc='upper left', title='Value')


    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.title('2-D Grid')

    
    plt.grid(True)
    plt.show() 


    plt.scatter(k,no_of_particles/repeat,color= "green")

    plt.title('2D Matrix Visualization')
    plt.xlabel('# Iterations')
    plt.ylabel('particle density')
    plt.show()
