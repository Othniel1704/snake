from fltk import *
from time import sleep
from random import randint

# dimensions du jeu
taille_case = 15
largeur_plateau = 40  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases


def case_vers_pixel(case):
    """
	Fonction recevant les coordonnées d'une case du plateau sous la 
	forme d'un couple d'entiers (ligne, colonne) et renvoyant les 
	coordonnées du pixel se trouvant au centre de cette case. Ce calcul 
	prend en compte la taille de chaque case, donnée par la variable 
	globale taille_case.
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case


def affiche_pommes(pommes):
    """
        Fonction permettant de créer une pomme et de l'afficher sur le
        plateau
    """
    for pomme in pommes:
        x, y = case_vers_pixel(pomme)
        cercle(x, y, taille_case/2,
               couleur='darkred', remplissage='red')
        rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
                  couleur='darkgreen', remplissage='darkgreen')


def affiche_serpent(serpent):
    """
        Fonction permettant de créer la tête du serpent (du joueur 1 si
        le mode multijoueur est activé) et de l'afficher sur le plateau
    """
    # on prend chaque element de la liste sepernt et on decinne un cercle
    for i in serpent :
        x, y = case_vers_pixel(i)  # à modifier !!!
        cercle(x, y, taille_case/2 + 1,
            couleur='black', remplissage='green')


def affiche_serpent1(serpent1):
    """
        Fonction permettant de créer la tête du serpent du joueur 2 et de
        l'afficher sur le plateau
    """
    for i in serpent1 :
        x, y = case_vers_pixel(i)
        cercle(x, y, taille_case/2 + 1,
            couleur='black', remplissage='blue')
    

def change_direction(direction, touche):
    """
        Fonction permettant de faire déplacer le serpent(du joueur 1 si
        le mode multijoueur est activé) en renvoyant la valeur reçu grâce
        au touche pressée. Ne peut pas renvoyer la valeur opposées a
        celle reçu juste avant
    """
    if touche == 'Up' and direction != (0, 1):
        # flèche haut pressée
        direction = (0, -1)
        return direction
    elif touche == 'Down' and direction != (0, -1):
        # flèche en bas
        direction = (0, 1)
        return direction
    elif touche == 'Right' and direction != (-1, 0):
        # flèche a droit
        direction = (1, 0)
        return direction
    elif touche == 'Left' and direction != (1, 0) :
        # flèche a gauche
        direction = (-1, 0)
        return direction
    else:
        # pas de changement !
        return direction

def change_direction1(direction1, touche):
    """
        Fonction permettant de faire déplacer le serpent du joueur 2 en
        renvoyant la valeur reçu grâce au touche pressée. Ne peut pas
        renvoyer la valeur opposées à celle reçu juste avant
    """
    if (touche == 'z' or touche == 'Z') and direction1 != (0, 1):
        # flèche haut pressée
        direction1 = (0, -1)
        return direction1
    elif touche == 's' or touche=='S' and direction1 != (0, -1):
        # flèche en bas
        direction1 = (0, 1)
        return direction1
    elif touche == 'd' or touche=='D' and direction1 != (-1, 0):
        # flèche a droit
        direction1 = (1, 0)
        return direction1
    elif touche == 'q' or touche=='Q' and direction1 != (1, 0):
        # flèche a gauche
        direction1 = (-1, 0)
        return direction1
    else:
        # pas de changement !
        return direction1

def Bouton_menu(Bouton, TEXTE):
    """
        Fonction qui créer et fait apparaitre un rectangle vert en entrant les
        coordonnées des quatres coins du rectangle et permet placer un texte
        dans le rectangle sur une fenetre
    """
    rectangle(Bouton[0][0] + 50, Bouton[0][1], Bouton[1][0]-50, Bouton[1][1]-25, \
              couleur='black', remplissage='green', epaisseur=1, tag='game')
    texte(Bouton[0][0] + 20, Bouton[0][1] + 10, TEXTE, couleur='black',taille=25, tag='game')


        # programme principal
if __name__ == "__main__":
    cree_fenetre(taille_case * largeur_plateau,
                     taille_case * hauteur_plateau)
    menu = True
    while menu :
        game = True
        ecran_debut = True
        pac_man = False
        multi = False
        vitesse = False

        efface_tout()
        # IMAGE = "fond_menu.png"
        # image(0, 0, IMAGE, ancrage='nw', tag="relou")
        Bouton=[[(150,150),(450,230)], [(150, 50),(450, 130)], [(150,250),(450,330)],[(150,350),(450,430)]]
        Bouton_menu(Bouton[3],'      Difficulté +')
        Bouton_menu(Bouton[2],'      Multijoueur')
        Bouton_menu(Bouton[1],'          Jouer')
        Bouton_menu(Bouton[0],'       Pac-man')

        
        while True: # TANT QUE UN BOUTON A PAS ETE PRESSE
            clique = attend_clic_gauche()
            if Bouton[1][0][0] <= clique[0] and clique[0] <= Bouton[1][1][0] and \
                    Bouton[1][0][1] <= clique[1] and clique[1] <=  Bouton[1][1][1]:
                break
            elif Bouton[0][0][0] <= clique[0] and clique[0] <= Bouton[0][1][0] and \
                    Bouton[0][0][1] <= clique[1] and clique[1] <= Bouton[0][1][1]:
                pac_man = not pac_man
                if pac_man == True :
                    texte(Bouton[0][0][0] + 20, Bouton[0][0][1] + 10, '       Pac-man', couleur='red',taille=25, tag='game')
                else :
                    texte(Bouton[0][0][0] + 20, Bouton[0][0][1] + 10, '       Pac-man', couleur='black',taille=25, tag='game')
            elif Bouton[2][0][0] <= clique[0] and clique[0] <= Bouton[2][1][0] and \
                    Bouton[2][0][1] <= clique[1] and clique[1] <= Bouton[2][1][1]:
                multi = not multi
                if multi == True :
                    texte(Bouton[2][0][0] + 20, Bouton[2][0][1] + 10, '      Multijoueur', couleur='red',taille=25, tag='game')
                else :
                    texte(Bouton[2][0][0] + 20, Bouton[2][0][1] + 10, '      Multijoueur', couleur='black',taille=25, tag='game')
            elif Bouton[3][0][0] <= clique[0] and clique[0] <= Bouton[3][1][0] and \
                    Bouton[3][0][1] <= clique[1] and clique[1] <= Bouton[3][1][1]:
                vitesse = not vitesse
                if vitesse == True :
                    texte(Bouton[3][0][0] + 20, Bouton[3][0][1] + 10, '      Difficulté +', couleur='red',taille=25, tag='game')
                else :
                    texte(Bouton[3][0][0] + 20, Bouton[3][0][1] + 10, '      Difficulté +', couleur='black',taille=25, tag='game')
                           

        while game:
            if game == False:
                break
        
            # initialisation du jeu
            taille_serpent = 1 # taille du serpent au debut du jeu
            taille_serpent1 = 1
            framerate = 10    # taux de rafraîchissement du jeu en images/s
            direction = (0, 0)  # direction initiale du serpent
            direction1 = (0, 0)
            pommes = [(randint(0, 39), randint(0, 29))] # liste des coordonnées des cases contenant des pommes
            serpent = [(20, 15)] # liste des coordonnées de cases adjacentes décrivant le serpent
            if multi == True:
                serpent1 = [(10, 20)]
          

            # boucle principale
            jouer = True
            while jouer:
                # affichage des objets
                efface_tout()
                if multi == True:
                    rectangle(0, 0, 600, 450, couleur='black', remplissage='white', epaisseur=3, tag='')
                    score = taille_serpent - 1 # le score au debut il depend de la taille du serpent
                    texte(50, 10, 'score:' + str(score), 'darkgreen', 'nw', 'Helvetica', 18, tag='')
                    score1 = taille_serpent1 - 1
                    texte(450, 10, 'score:' + str(score1), 'darkblue', 'nw', 'Helvetica', 18, tag='')
                    affiche_pommes(pommes)
                    affiche_serpent(serpent) # à modifier !
                    affiche_serpent1(serpent1)
                    mise_a_jour()
                else:
                    rectangle(0, 0, 600, 450, couleur='black', remplissage='white', epaisseur=3, tag='')
                    score = taille_serpent - 1 # le score au debut il depend de la taille du serpent
                    texte(50, 10, 'score:' + str(score), 'black', 'nw', 'Helvetica', 18, tag='')
                    affiche_pommes(pommes)
                    affiche_serpent(serpent) # à modifier !
                    mise_a_jour()

                # gestion des événements
                ev = donne_ev()
                ty = type_ev(ev)
                if ty == 'Quitte':
                    jouer = False
                elif ty == 'Touche':
                    print(touche(ev))
                    #print(serpent)
                    direction = change_direction(direction, touche(ev))
                    direction1 = change_direction1(direction1, touche(ev))
                    #deplacement du serpent
                """ajoute aux coordonnées du serpent la direction associé a l'évènement qui est stocker
                dans la liste serpent. Le serpent ne se déplace pas vraiment le serpent mais ajoute un autre
                cercle a chaque tour de boucle  pour résoudre ce probleme, on élimine a chaque tour le dernier
                élément de la liste serpent """

                #pac-man + limite jeu
                dx = serpent[0][0] + direction[0] # ajoue a l'abscisse
                dy = serpent[0][1] + direction[1] # ajoue a l'ordonné
                if pac_man == True:
                    if 0 > dx  :
                        dx = 40
                    elif dx > 39:
                        dx = 0
                    if  0 > dy:
                        dy = 30
                    elif dy > 29:
                        dy = 0
                else:
                    if dx < 0 or dx > 39 or dy < 0 or dy > 29: # delimite l'ere de jeu
                        jouer = False
                serpent.insert(0,(dx, dy)) # la liste serpent
                """
                    Permet au serpent de sortir de l'ère de jeu pour pouvoir revenir par l'opposés
                    de l'ère de jeu en ne mettant pas de limite pour l'ère de jeu si le mode Pac-man
                    est activé.
                """

                if multi == True :
                    dx1 = serpent1[0][0] + direction1[0] # ajoue a l'abscisse
                    dy1 = serpent1[0][1] + direction1[1] # ajoue a l'ordonné
                    if pac_man == True:
                        if 0 > dx1  :
                            dx1 = 40
                        elif dx1 > 39:
                            dx1 = 0
                        if  0 > dy1:
                            dy1 = 30
                        elif dy1 > 29:
                            dy1 = 0
                    else:
                        if dx1 < 0 or dx1 > 39 or dy1 < 0 or dy1 > 29: # delimite l'ere de jeu
                            jouer = False
                    serpent1.insert(0,(dx1, dy1)) # la liste serpent
            

                if (dx,dy) in pommes: # ajoute une pomme lorsque une est manger
                    pommes = [(randint(0, 39), randint(0, 29))]
                    taille_serpent += 1
                    
 
                if multi == True :
                    if (dx1, dy1) in pommes: # ajoute une pomme lorsque une est manger (serpent1)
                       pommes = [(randint(0, 39), randint(0, 29))]
                       taille_serpent1 += 1
             

                
                if len(serpent) > taille_serpent :
                    serpent.pop() # suprimme le dernier élément de la liste serpent
                corp_serpent = serpent + [] # liste des coordonnées du serpent sans la tete
                corp_serpent.remove(corp_serpent[0])

                if multi == True :
                    if len(serpent1) > taille_serpent1 :  #(serpent1)
                        serpent1.pop() # suprimme le dernier élément de la liste serpent
                    corp_serpent1 = serpent1 + [] # liste des coordonnées du serpent sans la tete
                    corp_serpent1.remove(corp_serpent1[0])
            
                if serpent[0] in corp_serpent : # si la tete du serpent touche son corps
                    jouer = False

                if multi == True :
                    if serpent1[0] in corp_serpent1 :
                        Jouer = False
                    if (dx,dy) in serpent1 or (dx1,dy1) in serpent:
                        jouer = False
                    if serpent[0] in serpent1:
                        jouer = False
                    if serpent1[0] in serpent:
                        jouer = False

                if vitesse == True :
                    framerate += 0.13*((score+1)%10 == 0)*vitesse
                    """
                        La vitesse de jeu augmente en fonctionne du score du joueur, plus le
                        score est élevé plus vitesse du jeu accélérera
                    """
                sleep(1 / framerate)

            ecran_fin = True 
            while ecran_fin: # écran de fin de jeu
                efface_tout()
                if multi == True:
                    texte(65, 5, 'GAME OVER', 'black', 'nw', 'segoe script', 50, tag='')
                    texte(100, 80, 'score joueur (1) : ' + str(score), 'green', 'nw', 'Helvetica', 35, tag='')
                    texte(100, 120, 'score joueur (2) : ' + str(score1), 'darkblue', 'nw', 'Helvetica', 35, tag='')
                    Bouton = [[(175, 370),(415, 450)],[(175, 270),(415, 350)], [(175, 175),(415, 255)]]
                    Bouton_menu(Bouton[2],'     Rejouer')
                    Bouton_menu(Bouton[1],'       Menu')
                    Bouton_menu(Bouton[0],'       quitter')
                    ecran_fin=False
                else :
                    texte(65, 10, 'GAME OVER', 'black', 'nw', 'segoe script', 50, tag='')
                    texte(175, 110, 'score: ' + str(score), 'darkgreen', 'nw', 'Helvetica', 45, tag='')
                    Bouton = [[(175, 370),(415, 450)],[(175, 270),(415, 350)], [(175, 175),(415, 255)]]
                    Bouton_menu(Bouton[2],'     Rejouer')
                    Bouton_menu(Bouton[1],'       Menu')
                    Bouton_menu(Bouton[0],'       quitter')                                                                                                                   
                    ecran_fin=False
            while True: # TANT QUE UN BOUTON A PAS ETE PRESSE
                clique = attend_clic_gauche()
                if Bouton[2][0][0] <= clique[0] and clique[0] <= Bouton[2][1][0] and \
                        Bouton[2][0][1] <= clique[1] and clique[1] <=  Bouton[2][1][1]:
                    break
                elif Bouton[1][0][0] <= clique[0] and clique[0] <= Bouton[1][1][0] and \
                        Bouton[1][0][1] <= clique[1] and clique[1] <= Bouton[1][1][1]:
                    game = False
                    break
                elif Bouton[0][0][0] <= clique[0] and clique[0] <= Bouton[0][1][0] and \
                        Bouton[0][0][1] <= clique[1] and clique[1] <= Bouton[0][1][1]:
                    ferme_fenetre()
    
                
            
            if ty == 'Quitte':
                 game = False
                 sleep(1 / framerate)



        # attente avant rafraîchissement
        sleep(1/framerate)

    # fermeture et sortie
    ferme_fenetre()



