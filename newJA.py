#Import des librairies
from tkinter import *
import random as rd
from PIL import ImageTk, Image




#Variables
#nombres de proies initiales
Npro = 10
#fréquences d'apparition des lapins à chaque tour
Fpro = 1


case = 10
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
    for _ in range(10):
        Random()
        SpawnPro(xpro,ypro,grid)
    print(grid)
    widget.grid_forget()
    BtnNext = Button(root, text='Next', command=Next)
    BtnNext.grid()
    affGrid()

###################

def Naissance():
    global Fpro
    for _ in range(Fpro):
        Random()
        SpawnPro(xpro,ypro,grid)

def Check(type):
    #global coordR
    for x in range(case):
        for y in range(case):
            if len(grid[x][y])!=0:
                if grid[x][y][type] > 1 :
                    grid[x][y][type] -= 1
                else:
                    grid[x][y] = []

def Move():
    pass
    

def Next():
    Check(1)
    #Check(2)
    Naissance()
    affGrid()
    

def affGrid():
    for x in range(case):
        for y in range(case):
            canvas.create_image(x*64,y*64,image=sol,anchor=NW)
            if len(grid[x][y]) == 2:
                canvas.create_image(x*64,y*64,image=rabbit, anchor=NW)
                coordR.append([x,y])
            if len(grid[x][y]) ==3:
                canvas.create_image(x*64,y*64,image=fox, anchor=NW)
                coordF.append([x,y])
    canvas.grid()
    


root = Tk()
root.title('Chasse')
canvas = Canvas(root, width = 640, height = 640,bg='green')
canvas.grid()
BtnStart = Button(root,text='Start', command=lambda: Start(BtnStart))
BtnStart.grid()



#Images Projet
sol = PhotoImage(file ="carré_sol.png")
rabbit = PhotoImage(file="rabbit.png")
fox = PhotoImage(file="fox.png")

root.mainloop()