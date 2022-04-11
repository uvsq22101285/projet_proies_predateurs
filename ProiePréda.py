#Contributors :  MOBRÉ Eliott - SUZANNE Jean-Alexandre


#########################################
# groupe MPCI 04
# Eliott MOBRE
# Jean-Alexandre SUZANNE
# https://github.com/uvsq22101285/projet_tas_de_sable
#########################################

#PARTIE TKINTER

######################

#LIBRAIRIES

from tkinter import *
from tkinter import messagebox as box
from PIL import ImageTk, Image
import random as r

init = 0
case = 30 #Nombre de cases
taille = 600/case #Taille des cases
Npro = 10 #Nombre de proies
Fpro = 3 #Fréquences d'apparition des proies


#CREATION DE LA GRILLE
grid = [[0 for x in range(case)]for y in range(case)]

#PARTIE TKINTER
root= Tk()
root.title('Chasse')
img = Image.open('poule.png')
img  = ImageTk.PhotoImage(img)
canvas = Canvas(root,height=600,width=600)
canvas.grid()
#backgroundLabel = Label(root,image=img)

def findColor(x,y,grid): #CHOISI LA COULEUR DE LA CASE
    if grid[x][y] == 0:
        return('green','DarkGreen')
    if grid[x][y] == 1:
        return('red','Darkred')

def spawnPro(): #APPARITION DES PROIES
    global grid, Npro
    n=0
    while n != Npro:
        rSpawnX = r.randint(0,case-1)
        rSpawnY = r.randint(0,case-1)
        if grid[rSpawnX][rSpawnY] ==0:
            grid[rSpawnX][rSpawnY] =1
            n+=1
    affGrid()

def BornPro(): #Naissance des proies
    global Npro
    Npro = Fpro
    spawnPro()
    affGrid()

def ReproPro(): #Reproduction des proies
    pass

def affGrid(): #AFFICHAGE DE LA CARTE
    global grid
    img = PhotoImage(file ="sol.png")
    for x in range(case):
        for y in range(case):
            canvas.create_image(taille*x,taille*y,taille+taille*x,taille+taille*y,image=img)
            canvas.grid()



def movePro():
    global grid, init
    newGrid = [[0 for x in range(case)]for y in range(case)]
    for x in range(case):
        for y in range(case):
            if grid[x][y]==1:
                n = r.randint(1,4)
                if n ==1 and grid[x-1][y]==0:
                    grid[x][y] = 0
                    newGrid[x-1][y] = 1
                elif n ==2 and grid[x][y-1]==0:
                    grid[x][y] = 0
                    newGrid[x][y-1] = 1
                elif n ==3 and grid[x+1][y]==0:
                    grid[x][y] = 0
                    newGrid[x+1][y] = 1
                elif n ==4 and grid[x][y+1]==0:
                    grid[x][y] = 0
                    newGrid[x][y+1] = 1
    grid = newGrid
    if init == 0:
        spawnPro()
    if init!= 0:
        BornPro()
    init+=1
   
    affGrid()


moveProBtn = Button(root,text='+',command=movePro).grid()


root.mainloop()