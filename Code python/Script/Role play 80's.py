import random

###initialisation
#ennemy
ENNEMY_HEALTH = 50
#hero
HERO_HEALTH = 50
#material
NUMBER_POTION = 3

#game status
running = True
passing = False

while running:

    #Generate random stats
    ennemy_attack = random.randrange(5, 16)
    hero_attack = random.randrange(5,11)
    health_potion = random.randrange(15, 50)

    #If both are alive
    if ENNEMY_HEALTH and HERO_HEALTH:

        #Hero phase
        if not passing:

            #User choice
            user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2)?")
            if not user_choice.isdigit() or not user_choice in ["1", "2"]:
                print("La valeur entrée est incorrect...")
                continue
            #Attack phase
            if user_choice == "1":
                ENNEMY_HEALTH -= hero_attack
                print(f"Vous avez infligé {hero_attack} points de dégâts à l'ennemi ⚔️")    
            #Health recovery phase
            else:
                passing = True
                if NUMBER_POTION:
                    HERO_HEALTH += health_potion
                    NUMBER_POTION -= 1
                    if HERO_HEALTH > 50:
                        HERO_HEALTH = 50
                    print(f"Vous récupérez {health_potion} point de vie ❤️ ({NUMBER_POTION}🧪 restantes)")
                else:
                    print("Vous n'avez plus de potion...")
                    continue
        #Standby phase
        else:
            passing = False
            print("Vous passez votre tour...")

        #Ennemy phase        
        if ENNEMY_HEALTH > 0:
            HERO_HEALTH -= ennemy_attack
            if HERO_HEALTH < 0:
                HERO_HEALTH = 0
                print(f"L'ennemi vous a infligé {ennemy_attack} points de dégâts ⚔️")
        else:
            ENNEMY_HEALTH = 0

        #Stats
        print(f"L'ennemi vous a infligé {ennemy_attack} points de dégâts ⚔️")          
        print(f"Il vous reste {HERO_HEALTH} points de vie.")
        print(f"Il reste {ENNEMY_HEALTH} points de vie à l'ennemi.")
        print("-------------------------------------------------------")

    elif not HERO_HEALTH:
        print("Tu as perdu... \nFin du jeu.")
        break

    else:
        print("Tu as gagné! \nFin du jeu.")
        break



