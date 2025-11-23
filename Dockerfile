FROM python:3.11-slim

# Crée un dossier de travail dans le conteneur
WORKDIR /app

# Copie tout le projet dans le conteneur
COPY . /app

# Commande par défaut : lancer le jeu de cartes
CMD ["python", "jeux1.py"]
