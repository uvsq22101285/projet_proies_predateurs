#Import des librairies
from tkinter import *
import random as rd
from PIL import ImageTk, Image




#Variables





#Nombre de case fois lui même 
case = 12
taille_case= 600/case


###########
#Proies
#nombres de proies initiales
Npro = 10
#fréquences d'apparition des lapins à chaque tour
Fpro =1
#Durée de vie en tour
Apro = 5

#########
#Variables temporaires utilisés dans les fonctions pour les proies
xpro = 0
ypro = 0

###########
#Predateur
Npre = 5
Apre = 5
Epre = 5 
xpre = 0
ypre = 0

#Position objet
coordR = []
coordF = []

##test
compteur = 0
newGrid = []
liste_pro = []

#Grille 
grid = [[[] for x in range(case)]for y in range(case)]


#############
#Fonction seulement 1er tour

#Donne des coordonnées random pour le spawn des premiers lapin
def Random():
    global xpro,ypro
    xpro = rd.randint(0, case-1)
    ypro = rd.randint(0, case-1)

#Spawn des premiers lapins
def SpawnPro(x,y,grid):
    if grid[x][y] == []:
        grid[x][y] = ['R',Apro]

#Spawn des prédateurs
def SpawnPre(x,y,grid):
    if grid[x][y] == []:
        grid[x][y] =['F',Apre,Epre]


#commencement de la partie
def Start(widget):
    affGrid()
    for _ in range(Npro):
        Random()
        if grid[xpro][ypro] != []:
            while grid[xpro][ypro]!= []:
                Random()
        SpawnPro(xpro,ypro,grid)
    for _ in range(5):
        Random()
        if grid[xpro][ypro] != []:
            while grid[xpro][ypro]!= []:
                Random()
        SpawnPre(xpro,ypro,grid)
    
    widget.grid_forget()
    BtnNext.grid(column=0, row=1)
    affGrid()


###################

####ajout bordure plateau###
def bordureFill(g,l,b):
    for i in range(l):
        for j in range(l):
            g[i][0] = b
            g[i][-1] = b
            g[0][j] = b
            g[-1][j] = b
    return g
############


def Naissance():
    global Fpro
    for _ in range(Fpro):
        Random()
        SpawnPro(xpro,ypro,grid)
    affGrid()

def NaissanceV2():
    global xpro, ypro, grid
    
    for x in range(case):
        for y in range(case):
            if len(grid[x][y]) == 2:
                xpro,ypro = 0,0
                #print('avant detect',xpro,ypro)
                Detect(x,y,grid)
                print('après detect',xpro,ypro)
                if xpro != 0 :
                    print('gui1')
                    if grid[xpro][ypro][1] != 5:
                        print('gui2')
                        print(liste_pro)
                        if [xpro,ypro] not in liste_pro:
                            print('gui3')
                            SpawnProNaissance(x,y,xpro,ypro)

    affGrid()               
                    

###marche pas
def SpawnProNaissance(x,y,xpro,ypro):
    global grid, liste_pro
    liste_x = [x, x+1,x-1]
    liste_xpro = [xpro,xpro+1,xpro-1]
    liste_y = [y, y+1, y-1]
    liste_ypro = [ypro,ypro+1,ypro-1]
    liste = [liste_x] + [liste_y] + [liste_xpro] + [liste_ypro]
    liste_final = [0,0]


    while grid[liste_final[0]][liste_final[1]] != []:
        #condition fausse 
        if liste[rd.randint(0,3)] == liste[0] or liste[rd.randint(0,3)] == liste[2]:
            print('guispawnx',grid[liste_final[0]][liste_final[1]],liste_final)
            liste_final= []
            liste_final.append([[liste_x[rd.randint(0,2)]],[liste_y[rd.randint(0,2)]]])
            if (liste_final[0] == x and liste_final[1] == y ) or (liste_final[0] == xpro and liste_final[1] == ypro ):
                print('guispawnx1')
                while (liste_final[0] == x and liste_final[1] == y ) or (liste_final[0] == xpro and liste_final[1] == ypro ):
                    liste_final = []
                    liste_final.append([[liste_x[rd.randint(0,2)]],[liste_y[rd.randint(0,2)]]])
                    print('guispawnx2')
        else:
            liste_final = []
            liste_final.append([[liste_xpro[rd.randint(0,2)]],[liste_ypro[rd.randint(0,2)]]])
            print('guispawnxpro',grid[liste_final[0]][liste_final[1]],liste_final)
            if (liste_final[0] == x and liste_final[1] == y ) or (liste_final[0] == xpro and liste_final[1] == ypro ):
                print('guispawnxpro1')
                while (liste_final[0] == x and liste_final[1] == y ) or (liste_final[0] == xpro and liste_final[1] == ypro ):
                    liste_final = []
                    liste_final.append([[liste_xpro[rd.randint(0,2)]],[liste_ypro[rd.randint(0,2)]]])
                    print('guispawnxpro2')



    #liste_pro.append([liste_final[0],liste_final[1]])
    print('Voici la liste final=',liste_final)
    #SpawnPro(liste_final[0],liste_final[1],grid)


####Marche
def Detect(x,y,grid):
    global xpro, ypro,liste
    #compteur = 0
    liste_pro.append([x,y])
    print(f'Lapin de base aux coordonnées x={x} et y={y}')
    liste_combinaison = [[x+1,y],[x+1,y-1],[x,y-1],[x-1,y-1],[x-1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
    for i in range(0,len(liste_combinaison)-1):
        if grid[liste_combinaison[i][0]][liste_combinaison[i][1]] != [] and grid[liste_combinaison[i][0]][liste_combinaison[i][1]] != '#':
            if len(grid[liste_combinaison[i][0]][liste_combinaison[i][1]]) == 2:
                xpro = liste_combinaison[i][0]
                ypro = liste_combinaison[i][1]
                print(f'Lapin trouvé aux coordonnées x={xpro} et y={ypro}')
            #else:
                #print('Pas de lapin')
    #print(liste)


def Check(condition):
    for x in range(case):
        for y in range(case):
            if grid[x][y] != '#':
                if len(grid[x][y])-1>=condition:
                    if grid[x][y][condition] > 1 :
                        grid[x][y][condition] -= 1
                    else:
                        grid[x][y] = []
    #print(grid)


#####
#Fonctions déplacement lapin
def CalculPro(x,y, grid):
    global xpro, ypro
    liste_x = [x, x+1,x-1]
    liste_y = [y, y+1, y-1]
    xpro,ypro = x,y
    while grid[xpro][ypro] != []:
        xpro = liste_x[rd.randint(0,2)]
        ypro = liste_y[rd.randint(0,2)]
        if xpro == x and ypro == y:
            while xpro == x and ypro == y:
                xpro = liste_x[rd.randint(0,2)]
                ypro = liste_y[rd.randint(0,2)]
#####
#Fonction déplacement renard
def Flair():
    pass


def newgrid():
    global newGrid
    newGrid = [[[] for x in range(case)]for y in range(case)]
    bordureFill(newGrid,case,'#')
#####



def Move():
    global xpro, ypro,xpre,ypre, grid
    temp = []
    newgrid()
    for x in range(case):
        for y in range(case):
            if len(grid[x][y]) == 2 :
                xpro = 0
                ypro = 0
                temp = grid[x][y].copy()
                CalculPro(x,y,grid)
                grid[x][y] = []
                newGrid[xpro][ypro] = temp.copy()
                temp = []
            if len(grid[x][y]) == 3 :
                temp = grid[x][y].copy()
                Flair()
                grid[x][y] = []
                newGrid[xpre][ypre] = temp.copy()
                temp = []

    grid = newGrid
    affGrid()
                    


def Restart():
    global grid
    grid = [[[] for x in range(case)]for y in range(case)]
    affGrid()

def Automatique():
    for _ in range(10): #à modifer 
        root.after(3000,Next())


def Next():
    Check(1)
    Check(2)
    #Move()
    NaissanceV2()
    #Naissance()
   

def affGrid():
    bordureFill(grid,case,'#')
    for x in range(case):
        for y in range(case):
            canvas.create_image(x*64,y*64,image=sol,anchor=NW)
            if len(grid[x][y]) == 2:
                if grid[x][y][1] == 5 :
                    canvas.create_image(x*64,y*64,image=rabbit5, anchor=NW)
                    coordR.append([x,y])
                elif grid[x][y][1] == 4 :
                    canvas.create_image(x*64,y*64,image=rabbit4, anchor=NW)
                    coordR.append([x,y])
                elif grid[x][y][1] == 3 :
                    canvas.create_image(x*64,y*64,image=rabbit3, anchor=NW)
                    coordR.append([x,y])
                elif grid[x][y][1] == 2 :
                    canvas.create_image(x*64,y*64,image=rabbit2, anchor=NW)
                    coordR.append([x,y])
                elif grid[x][y][1] == 1 :
                    canvas.create_image(x*64,y*64,image=rabbit1, anchor=NW)
                    coordR.append([x,y])
            if len(grid[x][y]) ==3:
                canvas.create_image(x*64,y*64,image=fox, anchor=NW)
                coordF.append([x,y])
            if grid[x][y] == '#':
                canvas.create_image(x*64,y*64,image=mur, anchor=NW)
    canvas.grid()
    


root = Tk()
root.title('Chasse')
canvas = Canvas(root, width = 760, height = 760,bg='green')
canvas.grid(columnspan=1)
BtnStart = Button(root,text='Start', command=lambda: Start(BtnStart))
BtnStart.grid(column=0, row=1)
BtnRestart = Button(root, text='Restart', command=Restart)
BtnRestart.grid(row=0, column=1)
BtnNext = Button(root, text='Next', command=Next)
BtnAuto = Button(root, text='Auto', command=Automatique).grid(column=1,row=1)

#Images Projet
sol = PhotoImage(file ="carré_sol.png")
rabbit1 = PhotoImage(file="rabbit1.png")
rabbit2 = PhotoImage(file="rabbit2.png")
rabbit3 = PhotoImage(file="rabbit3.png")
rabbit4 = PhotoImage(file="rabbit4.png")
rabbit5 = PhotoImage(file="rabbit5.png")
fox = PhotoImage(file="fox.png")
mur = PhotoImage(file='Mur2.png')

root.mainloop()