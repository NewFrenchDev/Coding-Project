import shutil
import glob
import os
import time

#path
CUR_DIR = os.path.dirname(__file__)

#Files extension
extensions = {".mp3": "Musique",
              ".wav": "Musique",
              ".mp4": "Videos",
              ".avi": "Videos",
              ".jpeg": "Images",
              ".jpg": "Images",
              ".png": "Images",
              ".pdf": "Documents",
              ".ipynb": "Notebooks",
              ".exe": "Software"}

fichiers = glob.glob(os.path.join(f'{CUR_DIR}', "*"))
for fichier in fichiers:
    extension = os.path.splitext(fichier)[-1]
    folder = extensions.get(extension)
    if folder:
        folder_path = os.path.join(f'{CUR_DIR}', folder)
        os.makedirs(f'{CUR_DIR}/{folder}', exist_ok=True)
        shutil.move(fichier, folder_path)

print("Files have been moved successfully!")
time.sleep(2)