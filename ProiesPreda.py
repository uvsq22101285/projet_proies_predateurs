#Import des librairies
from tkinter import *
import random as rd
import copy
from tkinter import messagebox as box 
import ast


#Variables

#Paramètres Partie
case = 30
taille_image = 32
Taille_canvas = (case * taille_image)-2
vitesse = 60


###########
#Proies
#nombres de proies initiales
Npro = 25
#Durée de vie en tour
Apro = 5

#########
#Variables temporaires utilisés dans les fonctions pour les proies
xpro = 0
ypro = 0

#liste des proies
liste_pro = []
liste_probis = []

###########
#Predateur
Npre = 12
Apre = 7
Epre = 5
xpre = 0
ypre = 0
dist_Max = 8

#Position objet
coordR = []
coordF = []

##Variables Temporaires pour les fonctions
gridtemp = []
newGrid = []
condition = False
compteur = 0
variable = 0


#liste des prédateurs
liste_preda = []

#Sauvegarde
save = []
savetemp = []

#Grille 
grid = [[[] for x in range(case)]for y in range(case)]


#############
#Fonction seulement 1er tour

#Donne des coordonnées random pour le spawn des premiers lapin
def Random():
    """
    Fonction qui choisit aléatoirement des coordonnées x et y
    type : int
    """
    global xpro,ypro
    xpro = rd.randint(0, case-1)
    ypro = rd.randint(0, case-1)

#Spawn des premiers lapins
def SpawnPro(x,y,grid):
    """
    Fonction qui fait apparaître les proies en fonction des paramêtres données
    x : coordonnées int
    y : coordonnées int
    grid : liste actuelle list
    """
    if grid[x][y] == []:
        grid[x][y] = ['R',Apro]

#Spawn des prédateurs
def SpawnPre(x,y,grid):
    """
    Fonction qui fait apparaître les prédateurs en fonction des paramêtres données
    x : coordonnées int
    y : coordonnées int
    grid : liste actuelle list
    """
    if grid[x][y] == []:
        grid[x][y] =['F',Apre,Epre]


#commencement de la partie
def Start(widget):
    """
    Fonction de départ qui permet de lancer le début de la simulation
    widget: button.tk
    """
    global coordF,gridtemp
    affGrid()
    for _ in range(Npro):
        Random()
        if grid[xpro][ypro] != []:
            while grid[xpro][ypro]!= []:
                Random()
        SpawnPro(xpro,ypro,grid)
        coordR.append([xpro,ypro])
    for _ in range(Npre):
        Random()
        if grid[xpro][ypro] != []:
            while grid[xpro][ypro]!= []:
                Random()
        SpawnPre(xpro,ypro,grid)
        coordF.append([xpro,ypro])

    gridtemp = grid.copy()
    widget.grid_forget()
    BtnNext.grid(column=1, row=1)

    affGrid()


    
###################

def saving():
    """
    Fonction qui sert à sauvegarder la matrice dans un fichier ficSauvegarde
    """
    fic = open('ficSauvegarde','w')
    for i in range(len(grid)):
           fic.write(str(grid[i])+'\n')
    fic.close() 

def loading():
    """
    Fonction qui sert à charger partie à partir d'un fichier ficSauvegarde
    """
    global grid
    grid =[]
    fic = open('ficSauvegarde','r')
    for line in fic:
        grid.append(ast.literal_eval(line))
    affGrid()

####ajout bordure plateau###
def bordureFill(g,l,b):
    """
    Fonction qui remplis les bords du plateau de bordures sous forme de '#'
    """
    for i in range(l):
        for j in range(l):
            g[i][0] = b
            g[i][-1] = b
            g[0][j] = b
            g[-1][j] = b
    return g
############

def NaissanceV2():
    """
    Fonction qui s'occupe de gérer l'accouplement des différents spécimens de la carte en respectant leurs conditions
    La proie ne peut pas s'accoupler si elle vient de naître 
    Le prédateur ne peut pas s'accoupler si il vient de naître et si il a une énergie inférieur à celle renseignée dans les réglages.
    """
    global xpro, ypro, grid
    
    accoupler_pro = []
    accoupler_pre = []
    for x in range(case):
        for y in range(case):
            xpro,ypro = 0,0
            if len(grid[x][y]) == 2:
                Detect(x,y,grid)
                if xpro != 0 :
                    if grid[xpro][ypro][1] != Apro:
                        if [xpro,ypro] not in accoupler_pro:
                            accoupler_pro.append([x,y])
                            SpawnProNaissance(x,y,xpro,ypro)
            elif len(grid[x][y]) == 3:
                Detect(x,y,grid)
                if xpro != 0:
                    #condition repro renard
                    if grid[xpro][ypro][1] != Apre and grid[xpro][ypro][2] > 5:
                        if [xpro,ypro] not in accoupler_pre:
                            accoupler_pre.append([x,y])
                            Random()
                            SpawnPre(xpro,ypro,grid)
                


    affGrid()               
                    

###marche pas
def SpawnProNaissance(x,y,xpro,ypro):
    """
    Fonction qui choisit aléatoirement 1 paire de coordonnées entre deux parents proies, pour faire apparaître aléatoirement une nouvelle proie autour du parent cible. 
    """
    global grid
    liste_x = [x, x+1,x-1]
    liste_xpro = [xpro,xpro+1,xpro-1]
    liste_y = [y, y+1, y-1]
    liste_ypro = [ypro,ypro+1,ypro-1]
    liste = [liste_x] + [liste_y] + [liste_xpro] + [liste_ypro]
    liste_final = []
    liste_combinaisonxy = [[x+1,y],[x+1,y-1],[x,y-1],[x-1,y-1],[x-1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
    liste_combinaisonxproypro = [[xpro+1,ypro],[xpro+1,ypro-1],[xpro,ypro-1],[xpro-1,ypro-1],[xpro-1,ypro],[xpro-1,ypro+1],[xpro,ypro+1],[xpro+1,ypro+1]]
    liste_free = []

    choix = []
    choix = liste[rd.randint(0,3)]
    for i in range(0,len(liste_combinaisonxy)):
        if choix == liste[0] or choix == liste[2]:
            if (grid[liste_combinaisonxy[i][0]][liste_combinaisonxy[i][1]]) == []:
                liste_free.append([liste_combinaisonxy[i][0],liste_combinaisonxy[i][1]])
        else:
            if (grid[liste_combinaisonxproypro[i][0]][liste_combinaisonxproypro[i][1]]) == []:
                liste_free.append([liste_combinaisonxproypro[i][0],liste_combinaisonxproypro[i][1]])

    if len(liste_free)>0:
        liste_final.append(liste_free[rd.randint(0,len(liste_free)-1)][0])
        liste_final.append(liste_free[rd.randint(0,len(liste_free)-1)][1])
        SpawnPro(liste_final[0],liste_final[1],grid)


####Marche
def Detect(x,y,grid):
    """
    Fonction qui permet de détecter la présence de proies ou de prédateurs 
    Cette fonction est notament utilisée pour l'accouplement
    """
    global xpro, ypro, liste_pro
    liste_pro = []
    random = []
    liste_combinaison = [[x+1,y],[x+1,y-1],[x,y-1],[x-1,y-1],[x-1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
    if len(grid[x][y]) == 2:
        for i in range(0,len(liste_combinaison)):
            if grid[liste_combinaison[i][0]][liste_combinaison[i][1]] != [] and grid[liste_combinaison[i][0]][liste_combinaison[i][1]] != '#':
                if len(grid[liste_combinaison[i][0]][liste_combinaison[i][1]]) == 2:
                    xpro,ypro = liste_combinaison[i][0],liste_combinaison[i][1]
                    random.append([xpro,ypro])
    elif len(grid[x][y]) == 3:
        for i in range(0,len(liste_combinaison)):
            if grid[liste_combinaison[i][0]][liste_combinaison[i][1]] != [] and grid[liste_combinaison[i][0]][liste_combinaison[i][1]] != '#':
                if len(grid[liste_combinaison[i][0]][liste_combinaison[i][1]]) == 3:
                    xpro,ypro = liste_combinaison[i][0],liste_combinaison[i][1]
                    random.append([xpro,ypro])
    if random != []:
        chiffre = rd.randint(0,len(random)-1)
        xpro = random[chiffre][0]
        ypro = random[chiffre][1]


def Check(condition):
    """
    Permet de réduire à chaque tour les points de vie et l'énergie des spécimens concernés..
    Si la cible n'a plus d'énergies ou de point de vies, celle-ci la supprime du plateau
    """
    global liste_pro
    for x in range(case):
        for y in range(case):
            if grid[x][y] != '#':
                if len(grid[x][y]) == 2 and condition == 1:
                    liste_pro.append([x,y])
                if len(grid[x][y])-1>=condition:
                    if grid[x][y][condition] > 1 :
                        grid[x][y][condition] -= 1
                    else:
                        grid[x][y] = []


#####
#Fonctions déplacement lapin
def CalculPro(x,y, grid):
    """
    Permet de déterminer la paire de coordonnée où la proie va pouvoir se déplacer
    """
    global xpro, ypro
    liste_combinaisonxy = [[x+1,y],[x+1,y-1],[x,y-1],[x-1,y-1],[x-1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
    liste_temp = []
    liste_final = []
    xpro,ypro = x,y
    for i in range(0,len(liste_combinaisonxy)):
        if grid[liste_combinaisonxy[i][0]][liste_combinaisonxy[i][1]] == []:
            liste_temp.append([liste_combinaisonxy[i][0],liste_combinaisonxy[i][1]])
    if liste_temp != []:
        liste_final.append(liste_temp[rd.randint(0,len(liste_temp)-1)])
        xpro,ypro = liste_final[0][0],liste_final[0][1]
    
def CalculPre(x,y,grid):
    """
    Permet de déterminer la paire de coordonnée où le prédateur va pouvoir se déplacer
    """
    global xpre,ypre
    liste_combinaisonxy = [[x+1,y],[x+1,y-1],[x,y-1],[x-1,y-1],[x-1,y],[x-1,y+1],[x,y+1],[x+1,y+1]]
    liste_temp = []
    liste_final = []
    xpre,ypre = x,y
    for i in range(0,len(liste_combinaisonxy)):
        if grid[liste_combinaisonxy[i][0]][liste_combinaisonxy[i][1]] == []:
            liste_temp.append([liste_combinaisonxy[i][0],liste_combinaisonxy[i][1]])
    if liste_temp != []:
        liste_final.append(liste_temp[rd.randint(0,len(liste_temp)-1)])
        xpre,ypre = liste_final[0][0],liste_final[0][1]


#####
#Fonction déplacement renard
def Flair(x,y): #Fonction déplacement renard
    """
    Fonction qui simule une intelligence artificielle des prédateurs pour choisir le chemin le plus court pour les manger
    """
    global liste_pro,liste_probis,xpre,ypre,liste_preda
    dist = []
    if liste_pro != [] or liste_probis != []:
        for i in range(len(liste_pro)):
            if max(abs(liste_pro[i][0]-x),abs(liste_pro[i][1]-y)) <= dist_Max:
                dist.append([liste_pro[i][0]-x,liste_pro[i][1]-y])
        for u in range(len(liste_probis)):
            if max(abs(liste_probis[u][0]-x),abs(liste_probis[u][1]-y)) <= dist_Max:
                dist.append([liste_probis[u][0]-x,liste_probis[u][1]-y])

        if len(dist) > 1 :  
            minVal = max(abs(dist[0][0]),abs(dist[0][1]))
            minIndx = 0

            for j in range(len(dist)):
                if minVal > max(abs(dist[j][0]),abs(dist[j][1])):
                    minVal = max(abs(dist[j][0]),abs(dist[j][1]))
                    minIndx = j
            for k in range(2):
                if dist[minIndx][k]!=0:
                    dist[minIndx][k] =dist[minIndx][k]//abs(dist[minIndx][k])
            xpre,ypre = dist[minIndx][0]+x,dist[minIndx][1]+y
            liste_preda.append([xpre,ypre])
    else:
        CalculPre(x,y,grid)


def newgrid():
    """
    Fonction qui créer basiquement une nouvelle grille de jeu
    type : list
    """
    global newGrid
    newGrid = [[[] for x in range(case)]for y in range(case)]
    bordureFill(newGrid,case,'#')
#####

def Move():
    """
    Fonction qui va permettre d'organiser le déplacement de chacune des espèces sur le terrain
    Elle prendra en compte les paires de coordonnées obtenu à travers la fonction Flair (pour les prédateurs) 
    et la fonction CalculPro (pour les proies)
    """
    global xpro, ypro,xpre,ypre, grid, gridtemp,liste_pro,liste_probis
    gridtemp = copy.deepcopy(grid)
    temp = []
    newgrid()
    for x in range(case):
        for y in range(case):
            if len(grid[x][y]) == 2 :
                xpro,ypro = 0,0
                temp = grid[x][y].copy()
                CalculPro(x,y,grid)
                grid[x][y] = []
                if grid[xpro][ypro] == [] and newGrid[xpro][ypro] == []:
                    newGrid[xpro][ypro] = temp.copy()
                    del liste_pro[liste_pro.index([x,y])]
                    liste_probis.append([xpro,ypro])
                else:
                    newGrid[x][y] = temp.copy()
                temp = []

            if len(grid[x][y]) == 3 :
                temp = grid[x][y].copy()
                Flair(x,y)
                grid[x][y] = []
                if grid[xpre][ypre] == [] and newGrid[xpre][ypre] == []:
                    newGrid[xpre][ypre] = temp.copy()
                elif len(grid[xpre][ypre]) == 2 or len(newGrid[xpre][ypre]) == 2:
                    grid[xpre][ypre] = []
                    energie = rd.randint(0,5)
                    newGrid[xpre][ypre] = temp.copy()
                    newGrid[xpre][ypre][2] += energie
                    if liste_pro.count([xpre,ypre]) > 0:
                        del liste_pro[liste_pro.index([xpre,ypre])]
                    else:
                        del liste_probis[liste_probis.index([xpre,ypre])]

                else:
                    newGrid[x][y] = temp.copy()
                temp = []
    grid = copy.deepcopy(newGrid)
    affGrid()
                    

def Restart(widget):
    """
    Fonction pour les boutons de l'interface Tkinter
    Elle permet de relancer la simulation
    Elle réintialise les précédentes variables.
    """
    global grid, save, compteur
    compteur = 0
    grid = [[[] for x in range(case)]for y in range(case)]
    widget.grid(row = 1, column=1)
    Start(BtnStart)
    affGrid()
    save = []

def Retour():
    """
    Fonction pour les boutons de l'interface Tkinter
    Elle permet de revenir en arrière jusqu'au lancement de la partie
    Si le retour en arrière est impossible un message d'erreur apparaîtra
    """
    global grid, gridtemp,save
    if save != []:
        grid = save[-1]
        del save[-1]
    else:
        box.showerror("Erreur Retour","Pas de Retour possible")
    affGrid()

def Next():
    """
    Fonction pour les boutons de l'interface Tkinter
    Elle permet le passage de chaque tour
    Elle permet l'appelle de toutes les fonctions qui assurent le bon déroulement de la partie 
    """
    global coordF, coordR,liste_pro,liste_probis,liste_preda,save,savetemp
    coordF,coordR=[],[]
    save.append(grid)
    savetemp = copy.deepcopy(save)   
    Check(1)
    Check(2)
    Move()
    NaissanceV2()
    Win()
    save = copy.deepcopy(savetemp)
    
    liste_pro,liste_probis,liste_preda=[],[],[]


def Selection(x):
    """
    Fonction pour les boutons de l'interface Tkinter
    Elle permet l'organisation des boutons de réglages et le changement précis des variables qui permettent le bon déroulement de la partie
    """
    global Npro,Npre,Apro,Apre,Epre,dist_Max

    if x == 1 :
        Npro = int(variable.get())
    elif x == 2 :
        Npre = int(variable.get())
    elif x == 3:
        Apro = int(variable.get())
    elif x == 4:
        Apre = int(variable.get())
    elif x == 5:
        Epre = int(variable.get())
    elif x == 6:
        dist_Max = int(variable.get())



def Reglages():
    """
    Fonction pour les boutons de l'interface Tkinter
    Menu qui regroupe les différents réglages qui permettent le bon déroulement de la partie
    Veuillez lire le readme pour connaître l'utilité de chaque variable
    """
    global variable
    fenetre = Toplevel()
    variable = Entry(fenetre, text ="Variable")
    variable.grid(column=0, row=0)
    BtnNpro = Button(fenetre, text='Nombre proies', command=lambda: Selection(1))
    BtnNpro.grid(column =0,row=1)
    BtnNpre = Button(fenetre, text='Nombre prédateurs', command=lambda: Selection(2))
    BtnNpre.grid(column =0,row=2)
    BtnApro = Button(fenetre, text='Vie des proies', command=lambda: Selection(3))
    BtnApro.grid(column =0,row=3)
    BtnApro = Button(fenetre, text='Vie des prédateurs', command=lambda: Selection(4))
    BtnApro.grid(column =0,row=4)
    BtnEpro = Button(fenetre, text="Energie prédateurs", command=lambda: Selection(5))
    BtnEpro.grid(column =0,row=5)
    BtnEproLabel = Label(fenetre, text="(Au dessus de 9 pas de changement graphique)")
    BtnEproLabel.grid(column = 1, row=5)
    BtnFlair = Button(fenetre, text='Distance Flair', command= lambda: Selection(6))
    BtnFlair.grid(column=0,row=6)

def Auto():
    """
    Fonction pour les boutons de l'interface Tkinter
    Elle permet le fonctionnement automatique de la simulation
    La vitesse de la simulation est réglable dans les paramètres de la partie
    """
    global compteur
    if compteur == 0:
        Start(BtnStart)
        compteur = 1
    Next()
    if condition == False:
        root.after(vitesse, Auto)

def Pause(widget):
    """
    Fonction pour les boutons de l'interface Tkinter
    Elle permet d'interrompre sans supprimer la progression de la simulation
    Disparaît lors de son utilisation
    Réapparaît après l'utilisation du bouton Reprendre
    """
    global condition
    condition = True
    widget.grid_forget()
    BtnReprendre.grid(column=2, row=2)

def Reprendre(widget):
    """
    Fonction pour les boutons de l'interface Tkinter
    Elle permet de reprendre la progression de la simulation
    Disparaît lors de son utilisation
    Réapparaît après l'utilisation du bouton Pause
    """
    global condition 
    condition = False
    Auto()
    widget.grid_forget()
    BtnPause.grid(column=2, row=2)

def RestartAuto():
    """
    Fonction pour les boutons de l'interface Tkinter
    Elle permet de relancer,une fois utiliser, la simulation depuis le début
    Elle appelle la fonction Auto()
    """
    global compteur,condition, grid
    compteur,condition = 0, False
    grid = [[[] for x in range(case)]for y in range(case)]
    Auto()

def Win():
    """
    Fonction qui conditionne la victoire
    Affiche une messagebox contenant le nom de l'espèce victorieuse
    """
    global condition
    preda = []
    pro = []
    for x in range(case):
        for y in range(case):
            if len(grid[x][y]) == 2:
                pro.append([x,y])
            elif len(grid[x][y]) == 3:
                preda.append([x,y])
    if pro == []:
        box.showinfo("Victoire","Les Prédateurs ont gagné !")
        condition = True
    elif preda == []:
        box.showinfo("Victoire","Les Proies ont survécu")
        condition = True

def affGrid():
    """"
    Fonction qui permet l'affichage et l'actualisation du plateau de jeu
    Permet de charger chaque image en fonction du type de la case, des caractéristiques ou de du spécimen qui y habite
    """
    bordureFill(grid,case,'#')
    for x in range(case):
        for y in range(case):
            canvas.create_image(x*32,y*32,image=sol,anchor=NW)
            if len(grid[x][y]) == 2:
                canvas.create_image(x*32,y*32,image=rabbit, anchor=NW)
                coordR.append([x,y])
                if grid[x][y][1] > 8:
                    canvas.create_image(x*32,y*32,image=Image9, anchor=NW)
                elif grid[x][y][1] == 8:
                    canvas.create_image(x*32,y*32,image=Image8, anchor=NW)
                elif grid[x][y][1] == 7:
                    canvas.create_image(x*32,y*32,image=Image7, anchor=NW)
                elif grid[x][y][1] == 6:
                    canvas.create_image(x*32,y*32,image=Image6, anchor=NW)
                elif grid[x][y][1] == 5:
                    canvas.create_image(x*32,y*32,image=Image5, anchor=NW)
                elif grid[x][y][1] == 4:
                    canvas.create_image(x*32,y*32,image=Image4, anchor=NW)
                elif grid[x][y][1] == 3:
                    canvas.create_image(x*32,y*32,image=Image3, anchor=NW)
                elif grid[x][y][1] == 2:
                    canvas.create_image(x*32,y*32,image=Image2, anchor=NW)
                elif grid[x][y][1] == 1:
                    canvas.create_image(x*32,y*32,image=Image1, anchor=NW)
                
                    
            if len(grid[x][y]) == 3:
                canvas.create_image(x*32,y*32,image=fox, anchor=NW)
                coordF.append([x,y])
                
                #Partie Vie
                if grid[x][y][1] > 8:
                    canvas.create_image(x*32,y*32,image=Image9, anchor=NW)
                elif grid[x][y][1] == 8:
                    canvas.create_image(x*32,y*32,image=Image8, anchor=NW)
                elif grid[x][y][1] == 7:
                    canvas.create_image(x*32,y*32,image=Image7, anchor=NW)
                elif grid[x][y][1] == 6:
                    canvas.create_image(x*32,y*32,image=Image6, anchor=NW)
                elif grid[x][y][1] == 5:
                    canvas.create_image(x*32,y*32,image=Image5, anchor=NW)
                elif grid[x][y][1] == 4:
                    canvas.create_image(x*32,y*32,image=Image4, anchor=NW)
                elif grid[x][y][1] == 3:
                    canvas.create_image(x*32,y*32,image=Image3, anchor=NW)
                elif grid[x][y][1] == 2:
                    canvas.create_image(x*32,y*32,image=Image2, anchor=NW)
                elif grid[x][y][1] == 1:
                    canvas.create_image(x*32,y*32,image=Image1, anchor=NW)

                #Partie Energie
                if grid[x][y][2] > 8:
                    canvas.create_image(x*32,y*32,image=Energie9, anchor=NW)
                elif grid[x][y][2] == 8:
                    canvas.create_image(x*32,y*32,image=Energie8, anchor=NW)
                elif grid[x][y][2] == 7:
                    canvas.create_image(x*32,y*32,image=Energie7, anchor=NW)
                elif grid[x][y][2] == 6:
                    canvas.create_image(x*32,y*32,image=Energie6, anchor=NW)
                elif grid[x][y][2] == 5:
                    canvas.create_image(x*32,y*32,image=Energie5, anchor=NW)
                elif grid[x][y][2] == 4:
                    canvas.create_image(x*32,y*32,image=Energie4, anchor=NW)
                elif grid[x][y][2] == 3:
                    canvas.create_image(x*32,y*32,image=Energie3, anchor=NW)
                elif grid[x][y][2] == 2:
                    canvas.create_image(x*32,y*32,image=Energie2, anchor=NW)
                elif grid[x][y][2] == 1:
                    canvas.create_image(x*32,y*32,image=Energie1, anchor=NW)
            if grid[x][y] == '#':
                canvas.create_image(x*32,y*32,image=mur, anchor=NW)
    canvas.grid()
    


root = Tk()
root.title('Chasse')
canvas = Canvas(root, width = Taille_canvas, height = Taille_canvas,bg='white')
canvas.grid(column =0,rowspan=7)
BtnStart = Button(root,text='Simulation Manuelle', command=lambda: Start(BtnStart))
BtnStart.grid(column=1, row=1)
BtnRestart = Button(root, text='Relance Manuelle', command=lambda: Restart(BtnStart))
BtnRestart.grid(row=3, column=1)
BtnNext = Button(root, text='Tour Suivant', command=Next)
BtnRetour = Button(root, text='Retour Manuelle', command=Retour).grid(column=1,row=2)
BtnAuto = Button(root, text= 'Simulation',command=Auto).grid(column=2,row=1)
BtnReglages = Button(root, text= 'Réglages',command=Reglages).grid(column=1,row=0)
BtnPause = Button(root,text= 'Pause',command=lambda: Pause(BtnPause))
BtnPause.grid(column=2,row=2)
BtnReprendre = Button(root,text= 'Reprendre',command=lambda: Reprendre(BtnReprendre))
BtnRestartAuto = Button(root,text= 'Relancer la simulation',command=RestartAuto)
BtnRestartAuto.grid(column=2,row=3)
BtnSauvegarde = Button(root, text='Sauvegarde',command=saving).grid(column=1, row=4)
BtnLoad = Button(root, text='Charger',command=loading).grid(column=2,row=4)


#Images Projet
sol = PhotoImage(file ="carré_sol.png")
rabbit = PhotoImage(file="rabbit.png")
fox = PhotoImage(file="fox.png")
mur = PhotoImage(file='Mur2.png')
Image0 = PhotoImage(file="0.png")
Image1 = PhotoImage(file="1.png")
Image2 = PhotoImage(file="2.png")
Image3 = PhotoImage(file="3.png")
Image4 = PhotoImage(file="4.png")
Image5 = PhotoImage(file="5.png")
Image6 = PhotoImage(file="6.png")
Image7 = PhotoImage(file="7.png")
Image8 = PhotoImage(file="8.png")
Image9 = PhotoImage(file="9.png")
Energie0 = PhotoImage(file="Energie0.png")
Energie1 = PhotoImage(file="Energie1.png")
Energie2 = PhotoImage(file="Energie2.png")
Energie3 = PhotoImage(file="Energie3.png")
Energie4 = PhotoImage(file="Energie4.png")
Energie5 = PhotoImage(file="Energie5.png")
Energie6 = PhotoImage(file="Energie6.png")
Energie7 = PhotoImage(file="Energie7.png")
Energie8 = PhotoImage(file="Energie8.png")
Energie9 = PhotoImage(file="Energie9.png")

root.mainloop()