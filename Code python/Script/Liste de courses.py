#Constante
CHOICE = "Choisissez parmi les 5 options suivantes :"
ADD = "1. Ajouter un élément à la liste de courses"
REMOVE = "2. Retirer un élément à la liste de courses"
DISPLAY = "3. Afficher les éléments de la liste de courses"
CLEAR = "4. Vider la liste de courses"
QUIT = "5. Quitter le programme"

#Initialisation
liste = []
running = True

while running:
    for element in [CHOICE, ADD, REMOVE, DISPLAY, CLEAR, QUIT]:
        print(element)
    user_choice = input("Votre choix : ")

    if user_choice == "1":
        element_added = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste.append(element_added.capitalize())
        print(f"L'élément {element_added} a bien été ajouté à la liste.")
        print("_________________________________________________________________________\n")
    elif user_choice == "2":
        element_removed = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        try:
            liste.remove(element_removed.capitalize())
            print(f"L'élément {element_removed} a bien été retiré de la liste.")
        except:
            print("L'élément n'est pas présent dans la liste.")
        print("_________________________________________________________________________\n")
    elif user_choice == "3":
        if liste:
            for element in liste:
                print(f'{liste.index(element) + 1}. {element}')
        else:
            print("Votre liste est vide.")
        print("_________________________________________________________________________\n")
    elif user_choice == "4":
        liste.clear()
        print("La liste à été vidée.")
        print("_________________________________________________________________________\n")
    elif user_choice == "5":
        running = False
        print("Au revoir!")
    else:
        print("Aucun choix sélectionné, veuillez entrer l'un des nombres correspondant aux options.")
        print("_________________________________________________________________________\n")
