heure=8
minute=53
seconde=45

while 0 < seconde:
    seconde=seconde-1
    print(heure, "h", minute, "m", seconde, "s")
    if seconde == 0 and minute > 0:
        minute=minute-1
        seconde=seconde+60
    elif seconde == 0 and minute == 0 and heure > 0:
        heure=heure-1
        minute=minute+60
        seconde=seconde+60

print("Compte à rebours écoulé !")