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
Fpro = 2
Apro = 10
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
                Detect(x,y,grid)
                if xpro == x and ypro == y:
                    continue
                else:
                    pass
                    
                    
def SpawnProNaissance(x,y,xpro,ypro):
    liste_x = [x, x+1,x-1]
    liste_xpro = [xpro,xpro+1,xpro-1]
    liste_y = [y, y+1, y-1]
    liste_ypro = [ypro,ypro+1,ypro-1]
    liste = [liste_x] + [liste_y] + [liste_xpro] + [liste_ypro]
    if liste[rd.randint(0,3)]:
        pass



def Detect(x,y,grid):
    global xpro, ypro
    compteur = 0
    liste_x = [x, x+1,x-1]
    liste_y = [y, y+1, y-1]
    xpro,ypro = x,y
    while len(grid[xpro][ypro]) != 2:
        compteur +=1
        xpro = liste_x[rd.randint(0,2)]
        ypro = liste_y[rd.randint(0,2)]
        if xpro == x and ypro == y:
            while xpro == x and ypro == y:
                xpro = liste_x[rd.randint(0,2)]
                ypro = liste_y[rd.randint(0,2)]
        elif compteur > 8:
            xpro,ypro = x,y
                

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
        if xpro == x and ypro == y:
            while xpro == x and ypro == y:
                xpro = liste_x[rd.randint(0,2)]
                ypro = liste_y[rd.randint(0,2)]
        else:
            xpro = liste_x[rd.randint(0,2)]
            ypro = liste_y[rd.randint(0,2)]
#####
#Fonction déplacement renard
def Flair():
    pass


def newgrid():
    global newGrid
    newGrid = [[[] for x in range(case)]for y in range(case)]
    bordureFill(grid,case,'#')
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
    Move()
    #Naissance()
   

def affGrid():
    bordureFill(grid,case,'#')
    for x in range(case):
        for y in range(case):
            canvas.create_image(x*64,y*64,image=sol,anchor=NW)
            if len(grid[x][y]) == 2:
                canvas.create_image(x*64,y*64,image=rabbit, anchor=NW)
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
rabbit = PhotoImage(file="rabbit.png")
fox = PhotoImage(file="fox.png")
mur = PhotoImage(file='Mur2.png')

root.mainloop()