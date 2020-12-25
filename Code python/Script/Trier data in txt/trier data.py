import os

CURRENT_PATH = os.path.dirname(__file__)

liste_prenom = []

with open(f"{CURRENT_PATH}/prenoms.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
    for liste in lines:
        liste = liste.replace(".", ",")
        liste = liste.replace(" ", ",")
        liste = liste.split(",")
        for element in liste[:]:
            element = element.strip(',. \n')
            if element != "":
                liste_prenom.append(element)
    liste_prenom.sort()
    print(liste_prenom)

with open(f"{CURRENT_PATH}/prenoms_triés.txt", "w", encoding='utf-8') as f:
    for element in liste_prenom:
        f.write(f'{element}')
        if liste_prenom.index(element) != len(liste_prenom) - 1:
            f.write('\n')

