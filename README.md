# Scan Port Localhost

Petit outil en Python permettant de tester si un port est ouvert ou fermé
sur la machine locale (localhost).

## Fonctionnement
- L'utilisateur saisit un numéro de port 
(port les plus importants sont detaillé dans le fichier ports.md)
- Le script tente une connexion TCP
- Le résultat indique si le port est ouvert ou fermé

## Exemple
```bash
python -m http.server 8000
python port_scan.py
Entrez un numéro de port à tester : 8000
Port 8000 : OUVERT
python port_scan.py
Entrez un numéro de port à tester : 410
Port 410 : FERME