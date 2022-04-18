<<<<<<< HEAD
'''TEST IMAGE'''
from tkinter import *  
from PIL import ImageTk,Image
''''''''''
im = Image.open("carré_sol.png")
print(im.size)
new_size = im.resize((32,32))
new_size.show()
'''''''''
root = Tk()
root.title('PythonGuides')
root.geometry('500x500')

canvas = Canvas(root, width = 640, height = 640,bg='black')
img = PhotoImage(file ="carré_sol.png")
img2 = PhotoImage(file ="rabbit.png")
img3 = PhotoImage(file ="fox.png")
img4 = PhotoImage(file="tomato.png")
img5 = PhotoImage(file="migrant.png")
img6 = PhotoImage(file="police-officer-head.png")
img7 = PhotoImage(file="water-flask.png")
img8 = PhotoImage(file="rolling-bomb.png")

for x in range(20):
    for y in range(20):
        canvas.create_image(x*64,y*64,image=img,anchor=NW)

canvas.create_image(64,0, image=img3, anchor=NW)
canvas.create_image(0,0,image=img2, anchor=NW)
canvas.create_image(0,64,image=img4, anchor=NW)
canvas.create_image(64,64,image=img5, anchor=NW)
canvas.create_image(64,128,image=img6, anchor=NW)
canvas.create_image(128,128,image=img7, anchor=NW)
canvas.create_image(128,64,image=img8, anchor=NW)


canvas.grid()

root.mainloop()
=======
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

def flare(x,y):
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
Start()

BtnRandom = Button(root,text='Random', command=Start)
BtnRandom.grid()
BtnMove = Button(root,text='Move >', command=find)
BtnMove.grid()
Label(root, text=print(grid))
root.mainloop()
>>>>>>> ea9ff7b01ef90bc4bedb19552ec18742b386dedd
