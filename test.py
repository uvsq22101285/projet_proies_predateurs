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

def flare():
    for x in range(nbrCase):
        for y in range(nbrCase):
            if len(grid[x][y]) == 3:
                listP=[]
                for j in range(len(coordP)):
                    dx = coordP[j][0]-x
                    dy = coordP[j][1]-y
                    listP.append(max(abs(dx),abs(dy)))
                minVal = listP[0]
                indx = 0
    #return index min
                for k in range(len(listP)):
                    if listP[k] < minVal:
                        minVal = listP[k]
                        indx = k 
                print('cible',coordP[k])        
    #coord min
                dx =coordP[indx][0]-x
                dy =coordP[indx][1]-y
                dist=[dx,dy]
                print('dist',dist)
                for n in range(2):
                    if dist[n]!=0:
                        dist[n]= dist[n]//abs(dist[n]) #deplace de 1
                return(x+dist[0],y+dist[1])

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

def chasse():
    for i in range(len(coordF)):
        listP=[]
        for j in range(len(coordP)):
            dx = coordP[j][0]-coordF[i][0]
            dy = coordP[j][1]-coordF[i][1]
            listP.append(max(abs(dx),abs(dy)))
        minVal = listP[0]
        indx = 0
        #return index min
        for k in range(len(listP)):
            if listP[k] < minVal:
                minVal = listP[k]
                indx = k         
        #coord min
        dx =coordP[indx][0]-coordF[i][0]
        dy =coordP[indx][1]-coordF[i][1]
        dist=[dx,dy]
        for n in range(2):
            if dist[n]!=0:
                dist[n]= dist[n]//abs(dist[n]) #deplace de 1
        print('dist',dist)
    #calculer dist min
    print(coordF,coordP)
    for i in range(len(coordF)):
        listP=[]
        for j in range(len(coordP)):
            dx = coordP[j][0]-coordF[i][0]
            dy = coordP[j][1]-coordF[i][1]
            listP.append(max(abs(dx),abs(dy),dx,dy))
        #trouver position du min
        minVal = listP[0]
        indx = 0
        for k in range(len(listP)):
            if listP[k] < minVal:
                minVal = listP[k]
                indx = k
        dx =coordP[indx][0]-coordF[i][0]
        dy =coordP[indx][1]-coordF[i][1]
        dist=[dx,dy]
        for n in range(2):
            if dist[n]!=0:
                dist[n]= dist[n]//abs(dist[n]) #deplace de 1
        grid[coordF[i][0]+dist[0]][coordF[i][1]+dist[1]] = grid[coordF[i][0]][coordF[i][1]]
        grid[coordF[i][0]][coordF[i][1]] = []

Start()

BtnRandom = Button(root,text='Random', command=Start)
BtnRandom.grid()
BtnMove = Button(root,text='Move >', command=find)
BtnMove.grid()
Label(root, text=print(grid))
root.mainloop()
