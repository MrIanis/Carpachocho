import os
import shutil
import json

def backup_files(config_file):
    # Vérifier si le fichier de configuration existe
    if not os.path.isfile(config_file):
        print(f"Le fichier de configuration {config_file} n'existe pas.")
        return

    try:
        # Ouvrir et lire le fichier de configuration
        with open(config_file, 'r') as f:
            config = json.load(f)
    except PermissionError:
        print(f"Vous n'avez pas les permissions pour lire le fichier {config_file}.")
        return
    except json.JSONDecodeError:
        print(f"Le fichier {config_file} n'est pas un fichier JSON valide.")
        return

    # Créer le répertoire de sauvegarde s'il n'existe pas
    backup_dir = 'backup'
    if not os.path.isdir(backup_dir):
        os.makedirs(backup_dir)

        
