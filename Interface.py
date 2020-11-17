from tkinter import *
from jeuDeLaVie import *
from time import sleep
from random import *


master = Tk()

MatSizeX = 130
MatSizeY = 75
canWidth = 10
canHeight = 10

const_prop_a = 0
const_prop_b = 1


matrice_propagation = np.zeros((MatSizeX, MatSizeY))
print("shape0")
print(matrice_propagation.shape[0])
centerX=MatSizeX//2
centerY=MatSizeY//2



matrice_propagation[centerX, centerY] = 1
matrice_propagation[centerX+1, centerY+1] = 1


mat_voisin = neighbors(0, 0, matrice_propagation)
print("MAT VOISINS")
print(mat_voisin)


#def initialisation_jeu():



def initWindow(canWidth, canHeight):
    widthW = canWidth * MatSizeX + MatSizeX
    heightW = canHeight * MatSizeY + MatSizeY
    w = Canvas(master, width=widthW, height=heightW)
    w.pack()
    return w



def refreshGrille(w,canWidth, canHeight):
    widthW = canWidth * MatSizeX + MatSizeX
    heightW = canHeight * MatSizeY + MatSizeY

    for i in range(0, MatSizeY):
        begX = 0
        Y = i * canHeight + i
        endX = widthW
        w.create_line(begX, Y, endX, Y, fill="#476042")
    for i in range(0, MatSizeX):
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


def infection(prop_a, prop_b):
    for i in range(0, MatSizeX-1):
        for j in range(0, MatSizeY-1):
            personne = etat_case(i, j, parametres_cases)
            if personne[0] == 0:
                propagation = randint(prop_a, prop_b)
                infectes = compte_infectes(i, j, matrice_propagation)
                if infectes >= 1 and propagation == 1:
                    personne[0] = personne[0] + 1
                    matrice_propagation[i, j] = 1
                    temps_maladie = randint(4, 12)
                    personne[2] = temps_maladie
                    bool_mort = randint(0, 1)
                    personne[3] = bool_mort
            elif personne[0] == 1:
                personne[1] = personne[1] + 1
                if personne[3] == 1:
                    if personne[1] == personne[2]:
                        #matrice_propagation[i, j] = 3
                        personne[0] = 3
                elif personne[1] == personne[2]:
                    personne[0] = 2
            parametres_cases[i, j] = [personne[0], personne[1], personne[2], personne[3]]
    return parametres_cases



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
        color_case(matrice_propagation, w, canHeight)

def init_parametres_cases(MatSizeX, MatSizeY):
    parametres_cases = dict()
    for i in range (0, MatSizeX):
        for j in range (0,MatSizeY):
            parametres_cases[i,j] = [0, 0, 0, 0]
    return parametres_cases



def etat_case(i, j, parametres_cases):
    return (parametres_cases[i, j])

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

mainloop()



#w.create_line(50, 50, 100, 50, fill="#476042")


