import os

#Current path
CURRENT_DIRECTORY = os.path.dirname(__file__)

#Structure to create
d = {"Films": ["Le seigneur des anneaux",
			   "Harry Potter",
			   "Moon",
			   "Forrest Gump"],
	 "Employes": ["Paul",
	 		      "Pierre",
				  "Marie"],
	 "Exercices": ["les_variables",
	 			   "les_fichiers",
				   "les_boucles"]}

#Create structure folder
for principal_folder, subfolders in d.items():
    for subfolder in subfolders:
        os.makedirs(f'{CURRENT_DIRECTORY}/{principal_folder}/{subfolder}', exist_ok=True)

