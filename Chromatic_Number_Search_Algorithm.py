#Graph Coloring: Vertex Coloring

#An algorithm to find the chromatic number of a graph quickly  (applies to chromatic index as well via line grpahs)

#The idea is simple: Find the gradient of the graph region where it is the most likely to find 'color-distinct' vertices (thus called the distinct region method) that are not adjacent to each others.
# In other words, enumerate all the possibilities and pick the cluster/subgraph where the number of adjacent vertices is maximum (number of non-adjacent vertices is minimum) and calculate the chromatic number
# Everything else is just a reiteration of that subgraph in terms of vertex coloring (color-preservation): Big Bang analogy

#It's all about finding a maximum clique such that the subgraph is perfect ie; chromatic number = clique number
#Heisenberg theorem: Chromatic number * Independence number >= number of vertices

import networkx as nx
from nxpd import draw
import numpy as np
import random
import math
import itertools
import functools



N = 20

CG = np.zeros((N,N))

for k in range(N):
    for j in range(N):
        if k != j:
            CG[k][j] = int(random.uniform(0,2))
            CG[j][k] = CG[k][j]
        else:
            CG[k][j] = 0
            

def Primary_Degree(G,v):
    return np.sum(G[v])/2

def Maximum_Degree(G):
    Degree = []
    for k in range(len(G)):
        Degree.append(Primary_Degree(G,k))
    max_deg = np.max(Degree)
    max_index = Degree.index(max_deg)
    return max_deg, max_index


def Maximum_Clique(G):
    Max_Clique = []
    s = Maximum_Degree(G)[1] #A good heuristic
    Max_Clique.append(s)
    t = 0
    Max_Iter = len(G)//2
    while t < Max_Iter:
        k = int(random.uniform(0,len(G)))
        B = True
        for j in Max_Clique:
            B = B * bool(G[k][j] == 1 or G[j][k] == 1)
        if B == True:
            Max_Clique.append(k) 
        t =  t + 1
    return Max_Clique

def Monte_Carlo(G,MCnumber):
    Clique_Set = []
    Clique_Size = []
    MCt = 0
    while MCt < MCnumber:
        Clique = Maximum_Clique(G)
        Clique_Set.append(Clique)
        Clique_Size.append(len(Clique))
        MCt = MCt + 1
    
    maximum_size = np.max(Clique_Size) 
    maxcindex = Clique_Size.index(maximum_size)
    MAXCLIQUE = Clique_Set[maxcindex]
    return MAXCLIQUE

def Chromatic_Number(G):
    MCN = 1000
    MaxClique = Monte_Carlo(G,MCN)
    return len(MaxClique)
    
    
        
        
CN = Chromatic_Number(CG)
print(CN)
