from random import randint

def des_joueur1(des):
    nombre1=randint(1,6)
    if des == 2:
        nombre2=randint(1,6)
    elif des == 3:
        nombre2=randint(1,6)
        nombre3=randint(1,6)
    nombre=nombre1+nombre2+nombre3
    return nombre

def des_joueur2(des):
    nombre1=randint(1,6)
    if des == 2:
        nombre2=randint(1,6)
    elif des == 3:
        nombre2=randint(1,6)
        nombre3=randint(1,6)
    nombre=nombre1+nombre2+nombre3
    return nombre

mon_score=0
ton_score=0
mon_score_temp=0
ton_score_temp=0

while mon_score < 21 and ton_score < 21:
    des=int(input())
    mon_score_temp=des_joueur1(des)
    mon_score=mon_score+mon_score_temp
    des=randint(1,3)
    ton_score_temp=des_joueur2(des)
    ton_score=ton_score+ton_score_temp
    print("Mon score: ",mon_score)
    print("Ton score: ",ton_score)
    print("")

if mon_score > 21 or ton_score > 21:
    print("Partie perdue !")
elif mon_score > 21 and ton_score > 21:
    print("Partie nulle !")
else:
    print("Partie gagné !")