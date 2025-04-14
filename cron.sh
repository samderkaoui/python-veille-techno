#!/bin/bash

# Installer cronie (le service cron)
echo "[+] Installation de cronie..."
sudo dnf install -y cronie

# Activer et démarrer le service crond
echo "[+] Activation et démarrage de crond..."
sudo systemctl enable crond --now

# Ajouter une tâche crontab pour l'utilisateur 'packer'
echo "[+] Ajout du cronjob..."
# On récupère la crontab actuelle, ajoute la tâche, et la recharge
(crontab -l -u packer 2>/dev/null; echo "0 10 * * * bash /home/packer/python-veille-techno/update_feeds.sh") | crontab -u packer -

echo "[✅] Installation terminée. Le script sera exécuté toutes les 5 minutes."
