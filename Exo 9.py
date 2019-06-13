while not mur_devant() :
    avance()
    while mur_devant() and not mur_a_droite():
        gauche()
        gauche()
        gauche()
        avance()
    while not mur_a_droite() and not mur_devant():
        gauche()
        gauche()
        gauche()
        avance()
    while mur_devant() and mur_a_droite():
        gauche()
    while not mur_devant() and not mur_a_droite():
        avance()
    while mur_devant() and not mur_a_droite():
        gauche()
        gauche()
        gauche()
        avance()