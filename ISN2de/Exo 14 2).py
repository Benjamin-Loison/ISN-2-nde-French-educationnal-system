from random import randint

nombre=0
alpha=0

for x in range(99):
    nombre=nombre+1
    print("+", end=" ")
    if nombre > 10:
        nombre=0
        print("")
        print("*")