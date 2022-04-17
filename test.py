#Lib
from random import randint
from tkinter import * 

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

def Start():
    global grid
    grid =[[0 for i in range(10)]for j in range(10)] #Besoin de supprimer les anciens avant
    SpawnA(1,1)
    SpawnA(1,2)
    affGrid()

#déplacement Fox
def find():
    global coordP
    global coordF
    print(coordF,coordP)
    dx = coordP[0][0]-coordF[0][0]
    dy = coordP[0][1]-coordF[0][1]
    print(dx,dy)
    dist=[dx,dy]
    for i in range(2):
        if dist[i]!=0:
            dist[i]=dist[i]//abs(dist[i])
    print(dist)
    if grid[coordF[0][0]+dist[0]][coordF[0][1]+dist[1]] == 0:
        grid[coordF[0][0]][coordF[0][1]] = 0
        grid[coordF[0][0]+dist[0]][coordF[0][1]+dist[1]] = 2
    coordP=[]
    coordF=[]
    affGrid()

Start()

BtnRandom = Button(root,text='Random', command=Start)
BtnRandom.grid()
BtnMove = Button(root,text='Move >', command=find)
BtnMove.grid()
Label(root, text=print(grid))
root.mainloop()
