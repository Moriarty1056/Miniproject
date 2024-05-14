import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import numpy as np
import random
import pandas as pd

size_of_simulation_matrix= 128
particle_existence_probability=.73
creation_reaction_probability=.04
total_time_stamps=2000
sample_size=200
no_of_particles=0
area_of_matrix = size_of_simulation_matrix*size_of_simulation_matrix

def getRandom():
    return random.random()

def moveUp(i,j):
    if(i==0):
        return size_of_simulation_matrix-1,j
    return i-1,j

def moveRight(i,j):
    if(j==size_of_simulation_matrix-1):
        return i,0
    return i,j+1

def moveDown(i,j):
    if(i==size_of_simulation_matrix-1):
        return 0,j
    return i+1,j

def moveLeft(i,j):
    if(j==0):
        return i,size_of_simulation_matrix-1
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

def topple(i,j):
    global topple_grid
    direction=getRandom()
    if(direction<.25):
        a,b = moveLeft(i,j)
        topple_grid[a][b]+=1
    if(direction>=.25 and direction<.50):
        a,b = moveUp(i,j)
        topple_grid[a][b]+=1
    if(direction>=.50 and direction<.75):
        a,b = moveRight(i,j)
        topple_grid[a][b]+=1
    if(direction>=.75):
        a,b = moveDown(i,j)
        topple_grid[a][b]+=1    

def reaction(i,j):
    global no_of_particles
    global grid
    global area_of_matrix
    global no_of_reactions
    if(grid[i][j]>1):
        number_of_reaction = math.floor(grid[i][j]/2)
        for c in range(number_of_reaction):
            type_of_reaction = getRandom()
            if(type_of_reaction<creation_reaction_probability):
                grid[i][j]+=1
                no_of_particles+=1
            else:
                grid[i][j]-=1
                no_of_particles-=1
        no_of_reactions=0    
        number_of_topple = grid[i][j]
        for b in range(int(number_of_topple)):
            diffusion(i,j)
    no_of_reactions+=1

# Main code
no_of_iterations = []
particle_density = np.zeros(total_time_stamps)
for a in range(sample_size):
    no_of_particles = 0
    no_of_reactions = 0
    grid = np.zeros((size_of_simulation_matrix,size_of_simulation_matrix))

    # Filling of the particle
    for i in range(size_of_simulation_matrix):
        for j in range(size_of_simulation_matrix):
            if(getRandom()<particle_existence_probability):
                grid[i][j]=1
                no_of_particles+=1

    # Diffusion process 
    for i in range(size_of_simulation_matrix):
        for j in range(size_of_simulation_matrix):
            diffusion(i,j)

    # Reaction process 
    for k in range(total_time_stamps):
        for i in range(size_of_simulation_matrix):
            for j in range(size_of_simulation_matrix):
                reaction(i,j)
        if(no_of_reactions>=area_of_matrix):
            for i in range(size_of_simulation_matrix):
                for j in range(size_of_simulation_matrix):
                    diffusion(i,j)
        particle_density[k]+=(no_of_particles/area_of_matrix)
for k in range(total_time_stamps):
    particle_density[k]= sample_size[k]/sample_size
    no_of_iterations.append(k)

plt.scatter(no_of_iterations,particle_density,color= "green",s=5)
plt.ylim(0,1)
plt.title('2D Matrix Visualization')
plt.xlabel('# Iterations')
plt.ylabel('particle density')
plt.show()

            
            