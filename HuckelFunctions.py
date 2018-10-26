#All the Functions required to run the program Exercise_1.py separately grouped as a python file to be imported.
import numpy as np 
from numpy import linalg as LA
import math
import networkx as nx

def Hkl_Polyene(n):                                 #A program that receives n and produces an adjacency matrix for n-polyene
    hM = np.ndarray((n,n))
    for i in range(0, hM.shape[0], 1):
        for j in range(0, hM.shape[1], 1):
            if i == j:
                hM[i][j] = 0            
            elif i == j+1 or j == i+1:
                hM[i][j] = -1
            else: hM[i][j] = 0 
    return hM     

def Hkl_Cyclic(n):                                  #A program that is similar to Hkl_Polyene but with ends joining for cyclic property                                
    hM = np.ndarray((n,n))
    for i in range(0, hM.shape[0], 1):
        for j in range(0, hM.shape[1], 1):
            if i == j:
                hM[i][j] = 0            
            elif i == j+1 or j == i+1:
                hM[i][j] = -1
            elif (i == 0 or j == 0) and (i == hM.shape[0]-1 or j == hM.shape[0]-1):
                hM[i][j] = -1
            else: hM[i][j] = 0 
    return hM 

def get_eig(_mtrx):                                 #Separate function that receives a matrix to determine its eigenvalue and vectors 
    eval, evec = LA.eig(_mtrx)
    evalist = []
    for i in range(0,eval.shape[0]):                #Organise the output of LA.eig(_mtrx)[1] in ascending order for faster user application
       evalist.append(eval[i])
    evalist.sort()
    return evalist, evec

def get_degen(_mtrx):
    evals = get_eig(_mtrx)[0]
    for i in range(0,len(evals)):
        evals[i] = round(evals[i],1)                #Computer distinguishes numbers with insignificant differences resulting from their own error thus round for grouping
    _dict = {}
    for j in evals:
        if j in _dict:
            continue
        else: _dict.update({j : evals.count(j)})
    return _dict


def Hkl_Platonic(n):                                #Networkx has standard graphs prepared for use.
    if n == 1:
        solid = nx.tetrahedral_graph()
    elif n == 2:
        solid = nx.cubical_graph()
    elif n == 3:
        solid = nx.dodecahedral_graph()
    elif n == 4:
        solid = nx.octahedral_graph()
    elif n == 5:
        solid = nx.icosahedral_graph()
    matrix = nx.to_numpy_matrix(solid)              #Use to_numpy_matrix() in networkx to convert the standard graph required to adjacency matrix
    return matrix   