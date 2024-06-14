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

    for item in config:
        src = item['src']
        dst = os.path.join(backup_dir, item['dst'])

        try:
            if os.path.isdir(src):
                shutil.copytree(src, dst)
                print(f"Le répertoire {src} a été sauvegardé vers {dst}.")
            elif os.path.isfile(src):
                shutil.copy2(src, dst)
                print(f"Le fichier {src} a été sauvegardé vers {dst}.")
            else:
                print(f"Le chemin {src} n'existe pas.")
        except PermissionError:
            print(f"Vous n'avez pas les permissions pour accéder à {src}.")
        except Exception as e:
            print(f"Une erreur est survenue lors de la sauvegarde de {src} vers {dst} : {e}")

# Exemple d'utilisation
config_file = 'config.json'
backup_files(config_file)


        
