# projet_proies_predateurs
Projet qui simule une carte permettant la cohabitation de proies et de prédateurs

Ce projet a été réalisé pour fonctionner avec des images garder un côté simple à comprendre.
Voici la fiche d'utilisation du projet : 

UNE PARTIE MANUELLE:

    - Simulation Manuelle va, comme son nom l'indique, lancez la simulation. Vous passerez les tours 1 par 1.
    - Tour Suivant, est un bouton qui apparaît une fois le bouton de Simulation Manuelle enclanché.
      Il vous permettra de gérer à votre manière le passage de chaque tour.
    - Relance Manuelle, vous permettra si votre partie ne va pas dans le sens que vous souhaitez de relancer
      une nouvelle partie !

UNE PARTIE AUTOMATIQUE:

    - Simulation, va lancer de manière automatique la partie et passera les tours à votre place.
      La simulation dure jusqu'à ce qu'un vainqueur se déclare ou si vous appuyez sur Pause.
    - Pause, est, comme son nom l'indique, un moyen de pouvoir arrêter en cours de simulation, sans supprimer,
      la partie actuelle.
    - Reprendre, ce bouton apparaît lorsque vous avez appuyez sur Pause, il vous permet de reprendre la simulation
    - Relancer la simulation vous permet de redémarrer la simulation automatiquement une fois cliquer

REGLAGES : 

La zone de texte sert à entrer une valeur que souhaitez appliquer aux différents paramètres de votre carte, de vos proies et des prédateurs. 
Pour appliquez une valeur il faut tout d'abord écrire la valeur que vous souhaitez appliquer (Par exemple vous souhaitez faire apparaître 10 lapins dès le début, vous allez
entrer 10 puis cliquer sur Nombre proies).
Si la partie est déjà lancée et que vous souhaitez changer les paramètres il suffit de cliquer sur Relancer la Simulation.

Voici les différents paramètres disponibles :

    - Nombre Proies, vous permet de gérer le nombre de Proies au lancement/relancement d'une partie.
    - Nombre Prédateurs, vous permet de gérer le nombre de Prédateurs au lancement/relancement d'une partie.
    - Vie des Proies, vous permet de gérer le nombre de vie que vous souhaitez donner aux proies dès leur apparition/naissance. Ce nombre de vie est exprimé en tour.
    - Vie des Prédateurs, vous permet de gérer le nombre de vie que vous souhaitez donner aux prédateurs dès leur apparition/naissance. Ce nombre de vie est exprimé en tour.
    - Energie des proies, spécifique aux prédateurs, cette énergie leur permet, si elle est suffisante, de pouvoir s'accoupler, et si celle-ci est trop basse, de décédé.
    - Distance Flair vous permet de gérer à quelle distance maximal les Prédateurs peuvent détecter les Proies.

PARTIE GRAPHIQUE :

Ici nous allons vous détaillez à quelle rôle est attribué quelle image : 

<img src="https://github.com/uvsq22101285/projet_proies_predateurs/blob/main/fox.png" alt="Le prédateur"/>

Ce logo représente un Prédateur, il peut se déplacer, manger et se reproduire.
Il se nourrit de Proies et leurs objectif est de manger toutes les proies en restant la seule espèce sur le terrain 

<img src="https://github.com/uvsq22101285/projet_proies_predateurs/blob/main/rabbit.png" alt="La proie"/>

Ce logo représente une Proie, il peut seulement se déplacer et se reproduire, son Objectif : Rester en vie ! 

<img src="https://github.com/uvsq22101285/projet_proies_predateurs/blob/main/carr%C3%A9_sol.png" alt="Le sol"/>

Ce logo représente le plateau sur lequel les spécimens se déplace et survive !

<img src="https://github.com/uvsq22101285/projet_proies_predateurs/blob/main/Mur2.png" alt="Le sol"/>

Ce logo représente les bordures du plateau, elles ne peuvent être franchies ! 

<img src="https://github.com/uvsq22101285/projet_proies_predateurs/blob/main/Energie0.png" alt="Le sol"/>

Ce logo représente l'énergie qui est une caractéristique spécifique aux prédateurs, elle n'excédera pas la valeur de 9 unités d'énergie graphique par manque de place graphique
mais la valeur d'énergie supplémentaire sera tout de fois bien présente. Ce logo se situe en haut à droite des prédateurs.

<img src="https://github.com/uvsq22101285/projet_proies_predateurs/blob/main/0.png" alt="Le sol"/>

Ce logo représente le nombre de vies en tour qui reste à la proie ou au prédateur concerné. Ce logo se situe en haut à gauche des proies ou des prédateurs.







