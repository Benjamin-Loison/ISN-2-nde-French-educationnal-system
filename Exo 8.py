a=0

while a!= 8 and not mur_devant():
    while not bille_au_sol() and not mur_devant():
        avance()
    while bille_au_sol():
        prends()
        a=a+1
  
            
gauche()
gauche()
while not mur_devant():
    avance()