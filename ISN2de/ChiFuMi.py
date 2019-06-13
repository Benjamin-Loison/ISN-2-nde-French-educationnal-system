#Importation de random, aléatoire
from random import randint

#Déclaration des constantes
## Si le joueur est en chair et en os mettre 1 ;) sinon 0 pour Intelligence Artificielle
joueur1=1
joueur2=0


#Procédures et fonctions
## Choix du joueur 1 et écris si c'est la Pierre, le Papier ou le Ciseaux
def afficher_choix1(joueur1):
    if joueur1 == 1:
        nombre=int(input())
    else:
        nombre=randint(1,3)
    print("Joueur 1:")
    if nombre == 1:
        print("Pierre")
    elif nombre == 2:
        print("Papier")
    else:
        print("Ciseaux")
    print("")
    return nombre

def afficher_choix2(joueur2):
    if joueur2 == 1:
        nombre=int(input())
    else:
        nombre=randint(1,3)
    print("Joueur 2:")
    if nombre == 1:
        print("Pierre")
    elif nombre == 2:
        print("Papier")
    else:
        print("Ciseaux")
    print("")
    return nombre

def augmenter_score(mon_coup,mon_score,ton_coup,ton_score):
    print("Résultat:")
    if mon_coup == 1 and ton_coup == 3:
        mon_score+=1
        print("La Pierre perd devant le Ciseaux.")
    elif mon_coup == 1 and ton_coup == 2:
        ton_score+=1
        print("La Pierre perd devant le Papier.")
    elif mon_coup == 2 and ton_coup == 1:
        mon_score+=1
        print("La Pierre gagne devant le Papier.")
    elif mon_coup == 2 and ton_coup == 3:
        ton_score+=1
        print("Le Papier perd devant le Ciseaux.")
    elif mon_coup == 3 and ton_coup == 1:
        ton_score+=1
        print("Le Ciseaux perd devant la Pierre.")
    elif mon_coup == 3 and ton_coup == 2:
        mon_score+=1
        print("Le Ciseaux gagne devant le Papier.")
    elif mon_coup == ton_coup:
        print("Egalité !")
    print("")
    return mon_score,ton_score

def affichage_resultat(mon_score,ton_score):
    print("Le score du joueur 1 est de",mon_score)
    print("Le score du joueur 2 est de",ton_score)
    print("")



#programme principal
coup_joueur1=0
coup_joueur2=0
score_joueur1=0
score_joueur2=0
while score_joueur1 < 10 and score_joueur2 < 10:
    print("Pierre: 1")
    print("Papier: 2")
    print("Ciseaux: 3")
    print("")
    coup_joueur1=afficher_choix1(joueur1)
    coup_joueur2=afficher_choix2(joueur2)
    score_joueur1,score_joueur2=augmenter_score(coup_joueur1,score_joueur1,coup_joueur2,score_joueur2)
    k=affichage_resultat(score_joueur1,score_joueur2)