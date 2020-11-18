import numpy as np
import time
import os
from Interface import *


t=np.zeros((11,11))




t[5,5]=1
t[5,4]=1
t[5,6]=1
t[4,5]=1
t[6,5]=1


#print(t)

def compteurVoisins(mat, i, j):
    compteur = 0
    rows, cols = mat.shape
    if (i != 0 and j != 0 and mat[i-1,j-1]) == 1:
            compteur = compteur + 1
    if(i != 0 and mat[i-1,j] == 1):
            compteur = compteur + 1
    if(i != 0 and j != cols-1 and mat[i-1, j+1] == 1):
            compteur = compteur + 1
    if(j!= cols-1 and mat[i,j+1] == 1):
            compteur = compteur + 1
    if(i != rows-1 and j != cols-1 and mat[i+1, j+1] == 1):
            compteur = compteur + 1
    if(i != rows-1 and mat[i+1,j] == 1):
            compteur = compteur + 1
    if(i != rows-1 and j != 0 and mat[i+1, j-1] == 1):
            compteur = compteur + 1
    if(j != 0 and mat[i, j-1] == 1):
            compteur = compteur + 1
    return compteur


def neighbors(i, j):
    borne_i = matrice_propagation.shape[1]
    borne_j = matrice_propagation.shape[0]
    mat_voisins = np.zeros(8)
    if i == 0:
        mat_voisins[0] = 4
        mat_voisins[1] = 4
        mat_voisins[2] = 4
        if j == 0 :
            mat_voisins[3] = 4
            mat_voisins[5] = 4
        elif j >= borne_j:
            mat_voisins[4] = 4
            mat_voisins[7] = 4
    elif i >= borne_i:
        mat_voisins[5] = 4
        mat_voisins[6] = 4
        mat_voisins[7] = 4
        if j == 0:
            mat_voisins[0] = 4
            mat_voisins[3] = 4
        elif j >= borne_j:
            mat_voisins[2] = 4
            mat_voisins[4] = 4

    if j == 0:
        mat_voisins[0] = 4
        mat_voisins[3] = 4
        mat_voisins[5] = 4
    elif j >= borne_j:
        mat_voisins[2] = 4
        mat_voisins[4] = 4
        mat_voisins[7] = 4

    if i == 0 and j == 0:
        mat_voisins[0] = 4
        mat_voisins[1] = 4
        mat_voisins[2] = 4



    else:
        mat_voisins[0] = matrice_propagation[i-1, j-1]
        mat_voisins[1] = matrice_propagation[i-1, j]
        mat_voisins[2] = matrice_propagation[i-1, j+1]
        mat_voisins[3] = matrice_propagation[i, j-1]
        mat_voisins[4] = matrice_propagation[i, j+1]
        mat_voisins[5] = matrice_propagation[i+1, j-1]
        mat_voisins[6] = matrice_propagation[i+1, j]
        mat_voisins[7] = matrice_propagation[i+1, j+1]
    return mat_voisins


def compte_infectes(i, j):
    voisins_mat = neighbors(i, j)
    infectes = 0
    for voisin in voisins_mat:
        if voisin == 1 :
            infectes = infectes + 1
    return infectes

def iterations(t):
    temp=np.zeros((11,11))
    rows, cols = t.shape
    for i in range (0,rows):
        for j in range(0, cols):
            if t[i,j] == 0 and compteurVoisins(t,i,j) == 3:
                temp[i,j] = 1
            elif t[i,j] == 1 and compteurVoisins(t,i,j) == 2 or compteurVoisins(t,i,j) == 3:
                temp[i,j] = 1
            else:
                temp[i,j] = 0
    print(temp)
    return temp

