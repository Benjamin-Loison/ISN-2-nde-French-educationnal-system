from random import randint

#Procédure et fonctions
def grand(V1,V2,V3):
    if V1 > V2:
        if V3>V1:
            return V3
        else:
            return V1
    elif V3>V2:
        return V3
    else:
        return V2

#programme pricnipal
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)

V=grand(a,b,c)
if a==b==c:
    print("Les nombres sont égaux")
else:
    print("Le plus grand nombre est", V)