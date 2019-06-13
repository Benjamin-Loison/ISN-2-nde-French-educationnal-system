import decimal
#déclaration procédure
def tabuler(fonction,borneInf,borneSup,pas):
    n=borneInf
    while n <= borneSup:
        print(n,fonction(n))
        n=n+pas

def maxmin(fonction,borneInf,borneSup,pas):
    n=borneInf
    min=fonction(borneSup)
    max=fonction(borneInf)
    while n<=borneSup:
        if fonction(n) > max:
            max=fonction(n)
        if fonction(n) <min:
            min=fonction(n)
        n=n+pas
    return min, max

def croissance(fonction, borneInf, borneSup, minf, maxf):
    if maxf == fonction(borneInf):
        print("Déroissant")
    if minf == fonction(borneInf):
        print("Croissant")
    if minf == maxf:
        print("Constant")



#corps programme principal
def fonction1(n):
    return ((2*n)**3)-3*n-1

tabuler(fonction1,2,5,0.5)
print("")
minf, maxf=maxmin(fonction1,2,5,0.5)
print("Le minimum de f est",minf)
print("Le maximun de f est",maxf)
croissance(fonction1,2,5,minf,maxf)