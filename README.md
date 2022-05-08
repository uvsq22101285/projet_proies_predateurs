# projet_proies_predateurs
Projet qui simule une carte permettant la cohabitation de proies et de prédateurs

def zoom():
    mat=charger(nomImgCourante)
    matZ=[[(0,0,0,255) for i in range(2*nbrCol(mat))]for j in range (2*nbrLig(mat))]
    #créer une matrice de largeur et hauteur deux fois plus grande 
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)): 
          matZ[i][j] = mat[i//2][j//2]
    modify(matZ)

def shrink():
    mat=charger(nomImgCourante)
    matS=[[(0,0,0,255) for i in range(nbrCol(mat)//2)]for j in range (nbrLig(mat)//2)]
    #créer une matrice de largeur et hauteur deux fois plus grande 
    for i in range(nbrLig(matS)):
        for j in range(nbrCol(matS)): 
          pixelR = (mat[2*i][2*j][0] + mat[2*i+1][2*j][0] + mat[2*i][2*j+1][0]+mat[2*i+1][2*j+1][0])//4
          pixelG = (mat[2*i][2*j][1] + mat[2*i+1][2*j][1] + mat[2*i][2*j+1][1]+mat[2*i+1][2*j+1][1])//4
          pixelB = (mat[2*i][2*j][2] + mat[2*i+1][2*j][2] + mat[2*i][2*j+1][2]+mat[2*i+1][2*j+1][2])//4
          matS[i][j] = (pixelR,pixelG,pixelB,255)
    modify(matS)