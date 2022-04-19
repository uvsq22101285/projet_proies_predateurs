#Lib
from random import randint
from tkinter import *
from unittest import case 

#Tkinter
root = Tk()
root.title('PythonGuides')
root.geometry('500x500')
canvas = Canvas(root, width = 640, height = 640,bg='green')

#load img
sol = PhotoImage(file ="carré_sol.png")
rabbit = PhotoImage(file ="rabbit.png")
fox = PhotoImage(file ="fox.png")

global grid
grid =[[0 for i in range(10)]for j in range(10)]
global coordP
coordP=[]
global coordF
coordF=[]

#Affichage case
def affGrid():
    global coordP
    global coordF
    for x in range(10):
        for y in range(10):
            canvas.create_image(x*64,y*64,image=sol,anchor=NW)
            if grid[x][y]==1:
                canvas.create_image(x*64,y*64,image=rabbit, anchor=NW)
                coordP.append([x,y])
            if grid[x][y]==2:
                canvas.create_image(x*64,y*64,image=fox, anchor=NW)
                coordF.append([x,y])
    canvas.grid()

#fait apparaître animal X fois
def SpawnA(nbr,animal):
    for X in range(nbr):
        r1 = [randint(0,9),randint(0,9)] #random case vide
        while grid[r1[0]][r1[1]] !=2:
            r1 = [randint(0,9),randint(0,9)]
        grid[r1[0]][r1[1]] = animal

def Check(condition):
    for x in range(case):
        for y in range(case):
            if len(grid[x][y])-1>=condition:
                if grid[x][y][condition] > 1 :
                    grid[x][y][condition] -= 1
                else:
                    grid[x][y] = []

def Flair(x,y): #Fonction déplacement renard
    global coordPro
    global xpre,ypre
    #calcul distances
    dist = []
    for i in range(len(coordPro)):
        dist.append([coordPro[i][0]-x,coordPro[i][1]-y])
    print()
    print(f'la distance de {[x,y]} entre chaque est {dist}')

    #calcul min dist
    minVal = max(abs(dist[0][0]),abs(dist[0][1]))
    print('minimum départ',minVal)
    minIndx = 0
    for j in range(len(dist)):
        if minVal > max(abs(dist[j][0]),abs(dist[j][1])):
            minVal = max(abs(dist[j][0]),abs(dist[j][1]))
            minIndx = j
    print(f'min arrivé {minVal} en {minIndx}')
    print(f'plus proche ?{coordPro[minIndx]}')
    for k in range(2):
        if dist[minIndx][k]!=0:
            dist[minIndx][k] =dist[minIndx][k]//abs(dist[minIndx][k])
    xpre = dist[minIndx][0]+x
    ypre = dist[minIndx][1]+y
    print(xpre,ypre)

def Start():
    global grid
    grid =[[0 for i in range(10)]for j in range(10)] #Besoin de supprimer les anciens avant
    SpawnA(1,1)
    SpawnA(1,2)
    affGrid()

#déplacement Fox
Start()

BtnRandom = Button(root,text='Random', command=Start)
BtnRandom.grid()
BtnMove = Button(root,text='Move >', command=find)
BtnMove.grid()
Label(root, text=print(grid))
root.mainloop()
