#Lib
from random import randint
from tkinter import * 

#Tkinter
root = Tk()
root.title('PythonGuides')
root.geometry('500x500')
canvas = Canvas(root, width = 640, height = 640,bg='green')

coordF=[]
coordP=[]
#load img
sol = PhotoImage(file ="carré_sol.png")
rabbit = PhotoImage(file ="rabbit.png")
fox = PhotoImage(file ="fox.png")

#Affichage case
def affGrid(grid):
    for x in range(10):
        for y in range(10):
            canvas.create_image(x*64,y*64,image=sol,anchor=NW)
            if grid[x][y] ==1:
                canvas.create_image(x*64,y*64,image=rabbit, anchor=NW)
                coordF.append([x,y])
            if grid[x][y] ==2:
                canvas.create_image(x*64,y*64,image=fox, anchor=NW)
                coordP.append([x,y])
    canvas.grid()

#fait apparaître animal X fois
def SpawnA(grid,nbr,animal): 
    for X in range(nbr):
        r1 = [randint(0,9),randint(0,9)] #random case vide
        while grid[r1[0]][r1[1]] !=0:
            r1 = [randint(0,9),randint(0,9)]
        grid[r1[0]][r1[1]] = animal

def Start():
    grid =[[0 for i in range(10)]for j in range(10)] #Besoin de supprimer les anciens avant
    SpawnA(grid,1,1)
    SpawnA(grid,1,2)
    affGrid(grid)
    find()
Start

#déplacement Fox
def find():
    dx = coordF[0][0]-coordP[0][0]
    dy = coordF[0][1]-coordP[0][1]
    print(dx,dy)
    dist=[dx,dy]
    for i in range(2):
        if dist[i]!=0:
            dist[i]=dist[i]/abs(dist[i])

    print(dist)

BtnRandom = Button(root,text='Random', command=Start)
BtnRandom.grid()
root.mainloop()