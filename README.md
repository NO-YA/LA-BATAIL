# LA-BATAIL

Jeu de cartes en ligne de commande qui simule la **bataille** avec un jeu de cartes classique. Le joueur affronte l’ordinateur manche par manche.

Le jeu est écrit en **Python** et peut être lancé :

- en local avec `python jeux1.py`
- dans un conteneur **Docker**

---

## 1. Prérequis

- **Python 3** installé (3.10+ recommandé) pour l’exécution en local
- **Docker Desktop** installé et démarré si tu veux utiliser Docker

---

## 2. Lancer le jeu en local (sans Docker)

Depuis un terminal placé dans le dossier du projet :

```bash
cd "c:\\Users\\N.O.Y.A\\Documents\\LA-BATAIL"
python jeux1.py
```

Déroulement :

1. Le programme te demande : `Entrez votre nom de joueur :`
   - Tape ton nom (ou laisse vide pour utiliser "Joueur") puis appuie sur **Entrée**.
2. Le jeu indique que la partie commence, puis affiche chaque manche :
   - la carte du joueur
   - la carte de l’ordinateur
   - le score de cartes récupérées
3. À chaque manche, le programme affiche :

   ```text
   Appuyez sur Entrée pour continuer...
   ```

   - Appuie simplement sur **Entrée** pour passer à la manche suivante.
   - Si tu fais `Ctrl+C`, le programme s’arrête avec une erreur `KeyboardInterrupt` (c’est normal : tu interromps manuellement le programme).

À la fin, le jeu affiche le résultat final : victoire du joueur, de l’ordinateur ou match nul.

---

## 3. Lancer le jeu avec Docker

Le dépôt contient un `Dockerfile` qui permet d’exécuter le jeu dans un conteneur.

### 3.1. Construire l’image Docker

Dans le dossier du projet (`LA-BATAIL`) :

```bash
docker build -t bataille .
```

- `bataille` est le nom de l’image Docker (tu peux le changer si tu veux).

### 3.2. Lancer le conteneur

Toujours depuis le même dossier :

```bash
docker run -it --rm bataille
```

Explications :

- `-it` : permet d’interagir avec le programme (saisie du nom, appui sur Entrée entre les manches).
- `--rm` : supprime automatiquement le conteneur une fois la partie terminée.

Le comportement à l’intérieur du conteneur est le même qu’en local :

1. Le conteneur démarre et lance `python jeux1.py`.
2. Tu entres ton nom quand c’est demandé, puis tu appuies sur **Entrée** pour avancer dans la partie.
3. `Ctrl+C` interrompt également le programme avec une erreur `KeyboardInterrupt` (interruption manuelle).

---

## 4. Structure principale du projet

- `jeux1.py` : script Python principal contenant la logique du jeu de bataille.
- `Dockerfile` : définition de l’image Docker pour lancer automatiquement `jeux1.py`.
- `README.md` : ce fichier, expliquant comment utiliser le projet.
