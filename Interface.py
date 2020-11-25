from tkinter import *
import numpy as np
from time import sleep
from random import *


master = Tk()

MatSizeX = 100
MatSizeY = 50
canWidth = 10
canHeight = 10

#Probabilités d'être infecté : const_prop_a chances sur const_prop_b

const_prop_a = 1
const_prop_b = 8

#Probabilités de mourir pendant l'infection

const_mort_a = 1
const_mort_b = 5

#Temps de maladie

const_maladie_a = 4
const_maladie_b = 5





matrice_propagation = np.zeros((MatSizeX, MatSizeY))

centerX=MatSizeX//2
centerY=MatSizeY//2



matrice_propagation[centerX, centerY] = 1
#atrice_propagation[centerX+1, centerY+1] = 1




#def initialisation_jeu():




def neighbors(i, j):
    borne_i = matrice_propagation.shape[1]
    borne_j = matrice_propagation.shape[0]
    mat_voisins = [0, 0, 0, 0, 0, 0, 0, 0]
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
        if voisin == 1:
            infectes = infectes + 1
    return infectes


def initWindow(canWidth, canHeight):
    widthW = canWidth * (MatSizeX-1) + MatSizeX-1
    heightW = canHeight * (MatSizeY-1) + MatSizeY- 1
    w = Canvas(master, width=widthW, height=heightW)
    w.pack()
    return w



def refreshGrille(w,canWidth, canHeight):
    widthW = canWidth * MatSizeX + MatSizeX
    heightW = canHeight * MatSizeY + MatSizeY

    for i in range(0, MatSizeY-1):
        begX = 0
        Y = i * canHeight + i
        endX = widthW
        w.create_line(begX, Y, endX, Y, fill="#476042")
    for i in range(0, MatSizeX-1):
        X = i * canWidth + i
        begY = 0
        endY = heightW
        w.create_line(X, begY, X, endY, fill="#476042")



def color_case(matrice_propagation, w, canHeight):
    pas = canHeight+1
    for i in range(0, MatSizeX):
        for j in range(0, MatSizeY):
            if matrice_propagation[i, j] == 0:
                w.create_rectangle(pas*i, pas*j, pas*i+pas, pas*j+pas,  fill='green')
            if matrice_propagation[i, j] == 1:
                w.create_rectangle(pas*i, pas*j, pas*i+pas, pas*j+pas, fill='red')
            if matrice_propagation[i, j] == 2:
                w.create_rectangle(pas*i, pas*j, pas*i+pas, pas*j+pas, fill='blue')
            if matrice_propagation[i, j] == 3:
                w.create_rectangle(pas*i, pas*j, pas*i+pas, pas*j+pas, fill='black')


def color_caseV2(w, canHeight):
    pas = canHeight+1
    for i in range(0, MatSizeX):
        for j in range(0, MatSizeY):
            if parametres_cases[i, j][0] == 0:
                w.create_rectangle(pas*i, pas*j, pas*i+pas, pas*j+pas,  fill='green')
            if parametres_cases[i, j][0] == 1:
                w.create_rectangle(pas*i, pas*j, pas*i+pas, pas*j+pas, fill='red')
            if parametres_cases[i, j][0] == 2:
                w.create_rectangle(pas*i, pas*j, pas*i+pas, pas*j+pas, fill='blue')
            if parametres_cases[i, j][0] == 3:
                w.create_rectangle(pas*i, pas*j, pas*i+pas, pas*j+pas, fill='black')


def infection(prop_a, prop_b):
    temp_parametres_cases = parametres_cases
    for i in range(0, MatSizeX-1):
        for j in range(0, MatSizeY-1):
            personne = etat_case(i, j, temp_parametres_cases)
            infectes = compte_infectes(i, j)
            if personne[0] == 0:
                propagation = randint(prop_a, prop_b)
                if infectes >= 1 and propagation == 1:
                    personne[0] = 1
                    temps_maladie = randint(const_maladie_a, const_maladie_b)
                    personne[2] = temps_maladie
                    bool_mort = randint(const_mort_a, const_mort_b)
                    personne[3] = bool_mort
                    matrice_propagation[i, j] = 1
            elif personne[0] == 1:
                personne[1] = personne[1] + 1
                if personne[3] == 1:
                    if personne[1] == personne[2]:
                        matrice_propagation[i, j] = 3
                        personne[0] = 3
                elif personne[1] == personne[2]:
                    personne[0] = 2
                    matrice_propagation[i, j] = 2
            temp_parametres_cases[i, j] = [personne[0], personne[1], personne[2], personne[3]]
    return temp_parametres_cases



def refreshMatParamsCases(a, b, c, d, indexi, indexj):
    temp_param_i_j = [a, b, c, d]
    temp_parametres_cases = dict()
    for i in range (0, MatSizeX):
        for j in range (0,MatSizeY):
            temp_parametres_cases[i,j] = parametres_cases[i, j]
    temp_parametres_cases[indexi, indexj] = temp_param_i_j
    return temp_parametres_cases

def refreshMatPropIndex(etat):
    temp_matrice_propagation = [etat, 0, temps_maladie, bool_mort]
    return temp_matrice_propagation[0]


def refreshMatProp(parametres_cases):
    temp_matrice_propagation = np.zeros((MatSizeX, MatSizeY))
    for i in range(0, MatSizeX):
        for j in range(0, MatSizeY):
            etat = etat_case(i, j, parametres_cases)
            temp_matrice_propagation[i, j] = etat[0]
    print("TEMP")
    print(temp_matrice_propagation)
    return temp_matrice_propagation


def boucle(w, matrice_propagation, canWidth, canHeight, iter):
    for i in range(0, iter):
        print("ITÉRATION : ")
        print(i)
        w.update()
        w.delete('all')
        w.after(1, refreshGrille(w, canWidth, canHeight))
        parametres_cases = infection(const_prop_a, const_prop_b)
        matrice_propagation = refreshMatProp(parametres_cases)
        color_caseV2(w, canHeight)

def init_parametres_cases(MatSizeX, MatSizeY):
    parametres_cases = dict()
    for i in range (0, MatSizeX):
        for j in range (0,MatSizeY):
            parametres_cases[i,j] = [0, 0, 0, 0]
    return parametres_cases



def etat_case(i, j, parametres_cases):
    return (parametres_cases[i, j])

def compteEachCase():
    morts = 0
    sains = 0
    gueris = 0
    for i in range(0, MatSizeX-1):
        for j in range(0, MatSizeY-1):
            if matrice_propagation[i,j] == 0:
                sains = sains + 1
            elif matrice_propagation[i,j] == 2:
                gueris = gueris + 1
            elif matrice_propagation[i,j] == 3:
                morts = morts + 1
    
    nbIndividu = (MatSizeX-1) * (MatSizeY-1)
    tauxInfect = ((nbIndividu-sains)/nbIndividu) * 100
    tauxMort = (morts / nbIndividu) * 100
    print('sains : '+ str(sains) + '\n')
    print ('gueris : '+ str(gueris) + '\n')
    print ('morts : ' + str(morts) + '\n');
    print ('taux d\'infection : '+ str(tauxInfect)+'%'+'\n')
    print ('taux de mortalité : '+ str(tauxMort)+'%'+'\n')

#def main():


parametres_cases = init_parametres_cases(MatSizeX, MatSizeY)
parametres_cases[centerX, centerY] = [1, 0, 7, 1]
parametres_cases[centerX+1, centerY+1] = [1, 0, 5, 1]
#case = etat_case(0, 0, parametres_cases)

#print(matrice_propagation.shape[0])
#print (case[0])
w = initWindow(canWidth,canHeight)
refreshGrille(w, canWidth, canHeight)
color_case(matrice_propagation, w, canHeight)
w.update()
boucle(w, matrice_propagation, canWidth, canHeight, 300)
compteEachCase()



#w.create_line(50, 50, 100, 50, fill="#476042")


