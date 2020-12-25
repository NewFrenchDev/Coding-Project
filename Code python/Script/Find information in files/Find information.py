import glob
import os
import json

CURRENT_PATH = os.path.dirname(__file__)

folder = f"{CURRENT_PATH}/dossier_exemple/**"
files = glob.glob(folder, recursive=True)

for element in files:
    filename = element.split('\\')[-1]
    if filename == "comptes_bancaires.json":
        with open(element, 'r', encoding='utf-8') as f:
            content = json.load(f)
            
        for bank, account in content.items():
            if bank == "Credit Mutuel":
                print(f'Le numero de compte de Credit Mutuel est {account.get("Numero de compte")}')

    if filename == "securite_sociale.txt":
        with open(element, 'r', encoding='utf-8') as f:
            line = f.readline()

        security_number = line.split(":")[1]
        print(f'Le numéro de sécurité social est {security_number}')