import random
import time

#Initialisation
running = True
nombre_mystère = random.randrange(101)
nombre_tentative = 5

#constante
TITLE = "***Le jeu du nombre mystère***"
INDICATION = "Il te reste {nombre} essais"


print(TITLE)
print(INDICATION.format(nombre=nombre_tentative))

while running:

    if nombre_tentative:
        try:
            user_input = int(input("Devine le nombre : "))
        except:
            print("Veuillez entrer un nombre valide.")
            continue

        if user_input < nombre_mystère:
            print(f"Le nombre mystère est plus grand que {user_input}")
            nombre_tentative -= 1
            print(INDICATION.format(nombre=nombre_tentative))

        elif user_input > nombre_mystère:
            print(f"Le nombre mystère est plus petit que {user_input}")
            nombre_tentative -= 1
            print(INDICATION.format(nombre=nombre_tentative))
            
        else:
            print(f"Bravo! Le nombre mystère était bien {nombre_mystère}")
            running = False
            
    else:
        print(f'Dommage! Le nombre mystère était {nombre_mystère}')
        running = False
        
print("Fin du jeu.")
time.sleep(2)