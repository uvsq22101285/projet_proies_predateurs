#Import des librairies
from tkinter import *
import random as rd
from PIL import ImageTk, Image




#Variables
#nombres de proies initiales
Npro = 10
#fréquences d'apparition des lapins à chaque tour
Fpro = 1

#Nombre de case fois lui même 
case = 12
taille_case= 600/case
Apro = 5
xpro = 0
ypro = 0

#Position objet
coordR = []
coordF = []



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

#placement des 10 proies
def Start(widget):
    affGrid()
    for _ in range(1):
        Random()
        if grid[xpro][ypro] != []:
            while grid[xpro][ypro]!= []:
                Random()
        SpawnPro(xpro,ypro,grid)
    widget.grid_forget()
    BtnNext.grid()
    affGrid()

###################

####Test####
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

def Check(type):
    #global coordR
    for x in range(case):
        for y in range(case):
            if grid[x][y] != '#':
                if len(grid[x][y])!=0:
                    if grid[x][y][type] > 1 :
                        grid[x][y][type] -= 1
                    else:
                        grid[x][y] = []

def Autour(x,y):
    liste_x = [x-1,x+1,x]
    liste_y = [y-1,y+1,y]
    x = liste_x[rd.randint(0,len(liste_x)-1)]
    y = liste_y[rd.randint(0,len(liste_y)-1)]
    return x,y


def Move():
    global grid
    temp = []
    coordtemp = []
    for x in range(case):
        for y in range(case):
            if len(grid[x][y]) == 2:
                liste_x = [x-1,x+1,x]
                liste_y = [y-1,y+1,y]
                temp =grid[x][y].copy()
                grid[x][y] = []
                coordtemp.append(x)
                coordtemp.append(y)
                x = liste_x[rd.randint(0,len(liste_x)-1)]
                y = liste_y[rd.randint(0,len(liste_y)-1)]
                print(x,y)
                print(grid[x][y])
                if grid[x][y] != []:
                    while grid[x][y] != []:
                        x = coordtemp[0]
                        y = coordtemp[1]
                        x = liste_x[rd.randint(0,len(liste_x)-1)]
                        y = liste_y[rd.randint(0,len(liste_y)-1)]
                        if x == coordtemp[0] and y == coordtemp[1]:
                            x = coordtemp[0]
                            y = coordtemp[1]
                            x = liste_x[rd.randint(0,len(liste_x)-1)]
                            y = liste_y[rd.randint(0,len(liste_y)-1)]

                grid[x][y] = temp.copy()
                temp=[]
                coordtemp = []
    affGrid()

                
def Restart():
    global grid
    grid = [[[] for x in range(case)]for y in range(case)]
    affGrid()



def Next():
    Check(1)
    #Check(2)
    Move()
    Naissance()
    affGrid()
    

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
canvas.grid()
BtnStart = Button(root,text='Start', command=lambda: Start(BtnStart))
BtnStart.grid()
BtnRestart = Button(root, text='Restart', command=Restart)
BtnRestart.grid(row=0, column=1)
BtnNext = Button(root, text='Next', command=Next)


#Images Projet
sol = PhotoImage(file ="carré_sol.png")
rabbit = PhotoImage(file="rabbit.png")
fox = PhotoImage(file="fox.png")
mur = PhotoImage(file='Mur2.png')

root.mainloop()