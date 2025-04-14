#!/usr/bin/env python3

import os
import shutil
from datetime import datetime
import subprocess

def archive_current_feeds():
    """Archive les flux RSS actuels dans un répertoire daté."""
    
    # Vérifiez si les fichiers actuels existent
    if not os.path.exists("flux") or not os.path.exists("index.html"):
        print("Aucun fichier à archiver. Exécutez d'abord veille.py.")
        return False
    
    # Créez le dossier archives s'il n'existe pas
    archives_dir = "./archives"
    os.makedirs(archives_dir, exist_ok=True)
    
    # Créez un répertoire d'archives avec le format jour/mois/année
    now = datetime.now()
    # Format qui garantit un tri chronologique (YYYY-MM-DD) mais affiche JJ/MM/AAAA
    current_date = now.strftime("%Y-%m-%d_%H-%M-%S")  # Pour le tri
    display_date = now.strftime("%d/%m/%Y")  # Pour l'affichage
    # Combine les deux formats pour permettre un tri correct et un affichage clair
    archive_folder_name = f"{current_date}_{display_date.replace('/', '-')}"
    archive_path = os.path.join(archives_dir, archive_folder_name)
    
    # Vérifiez si ce dossier existe déjà (normalement impossible avec l'horodatage)
    if os.path.exists(archive_path):
        print(f"Le dossier d'archives {archive_path} existe déjà.")
        return False
    
    # Créez le répertoire d'archives
    os.makedirs(archive_path)
    
    # Déplacez le dossier flux et index.html vers les archives
    try:
        shutil.move("index.html", os.path.join(archive_path, "index.html"))
        shutil.copytree("flux", os.path.join(archive_path, "flux"))
        shutil.rmtree("flux")
        print(f"Archivage effectué avec succès dans {archive_path}")
        return True
    except Exception as e:
        print(f"Erreur lors de l'archivage: {str(e)}")
        return False

def update_feeds():
    """Lance le script veille.py pour générer de nouveaux flux."""
    try:
        print("Mise à jour des flux RSS...")
        subprocess.run(["python3", "veille.py"], check=True)
        print("Mise à jour des flux RSS terminée avec succès.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la mise à jour des flux: {str(e)}")
        return False

if __name__ == "__main__":
    if archive_current_feeds():
        update_feeds()
    else:
        print("L'archivage a échoué. Les flux n'ont pas été mis à jour.")
