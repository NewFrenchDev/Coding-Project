import shutil
import glob
import os
import time

#path
CUR_DIR = os.path.dirname(__file__)

#Create folders if not exist
os.makedirs(f'{CUR_DIR}/Musique', exist_ok=True)
os.makedirs(f'{CUR_DIR}/Videos', exist_ok=True)
os.makedirs(f'{CUR_DIR}/Images', exist_ok=True)
os.makedirs(f'{CUR_DIR}/Documents', exist_ok=True)
os.makedirs(f'{CUR_DIR}/Notebooks', exist_ok=True)
os.makedirs(f'{CUR_DIR}/Software', exist_ok=True)

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
        shutil.move(fichier, folder_path)

print("Files have been moved successfully!")
time.sleep(2)