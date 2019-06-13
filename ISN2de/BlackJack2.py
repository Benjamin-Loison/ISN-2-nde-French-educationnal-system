from random import randint

def des_joueur(des):
    nombre2=0
    nombre3=0
    nombre1=randint(1,6)
    if des == 2:
        nombre2=randint(1,6)
    elif des == 3:
        nombre2=randint(1,6)
        nombre3=randint(1,6)
    nombre=nombre1+nombre2+nombre3
    return nombre

def affichage_score(mon_score,ton_score,continu):
    if continu == 0:
        print("Mon score: ",mon_score)
        print("Ton score: ",ton_score)
        print("")

def fin_de_partie(mon_score,ton_score):
    if mon_score > 21 or ton_score > 21:
        print("Partie perdue !")
    elif mon_score > 21 and ton_score > 21:
        print("Partie nulle !")
    elif mon_score == 21:
        print("Partie gagné par moi !")
    elif ton_score == 21:
        print("Partie gagné par toi !")

def continuer(des):
    if des == 0:
        return 1
    else:
        return 0
#programme principal
mon_score=0
ton_score=0
mon_score_temp=0
ton_score_temp=0
continu=0

while mon_score < 21 and ton_score < 21 and continu == 0:
    des=int(input("Nombre de dés"))
    continu=continuer(des)
    mon_score_temp=des_joueur(des)
    mon_score=mon_score+mon_score_temp
    des=randint(1,3)
    ton_score_temp=des_joueur(des)
    ton_score=ton_score+ton_score_temp
    affichage_score(mon_score,ton_score,continu)

fin_de_partie(mon_score,ton_score)