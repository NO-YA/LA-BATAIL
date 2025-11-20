import random 
from collections import deque

# Cette ligne demande au joueur d'entrer le nom qu'il va utiliser durant la partie
nom_joueur = input("Entrez votre nom de joueur : ") or "Joueur"  # Si le joueur n'entre rien, utiliser "Joueur" par défaut

# Ordre des cartes
ordre_des_cartes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'AS']

# Création du jeu de 52 cartes (4 types de carte x 13 valeurs de carte)
types_de_carte = ['Coeur', 'Carreau', 'Trèfle', 'Pique']  # Les 4 types de carte
deck_principal = [(ordre_carte, type_carte) 
             for type_carte in types_de_carte for ordre_carte in ordre_des_cartes
             ]  
# Génère toutes les combinaisons (ordre_carte, type_carte)
random.shuffle(deck_principal)  # Mélange le jeu de cartes

# Distribution des cartes entre le joueur et l'ordinateur
deck_joueur = deque(deck_principal[::2])  # Le joueur reçoit les cartes aux indices pairs
deck_ordinateur = deque(deck_principal[1::2])  # L'ordinateur reçoit les cartes aux indices impairs

print(f"{nom_joueur}, la partie commence !")
print("Vous affrontez l'ordinateur.")

def comparer_cartes(carte_du_joueur, carte_ordinateur):
    """
    Compare deux cartes et retourne le gagnant ("joueur", "ordinateur") ou "bataille" en cas d'égalité.
    Les types de carte ne sont pas pris en compte.
    """
    index_joueur = ordre_des_cartes.index(carte_du_joueur[0])  # Trouve l'indice de la carte du joueur
    index_ordinateur = ordre_des_cartes.index(carte_ordinateur[0])  # Trouve l'indice de la carte de l'ordinateur

    if index_joueur > index_ordinateur:
        return "joueur"
    elif index_joueur < index_ordinateur:
        return "ordinateur"
    else:
        return "bataille"

def jouer_manche(deck_joueur, deck_ordinateur, numero_manche, nom_joueur):
    """
    Simule une manche du jeu.
    - Chaque joueur joue la carte du dessus de son deck.
    - En cas d'égalité, une bataille est déclenchée.
    - Retourne le gagnant de la manche ("joueur" ou "ordinateur") et les cartes jouées (butin).
    """

    # Chaque joueur joue une carte
    carte_du_joueur = deck_joueur.popleft()  # Le joueur prend la première carte de son deck
    carte_ordinateur = deck_ordinateur.popleft()  # L'ordinateur fait de même
    butin = [carte_du_joueur, carte_ordinateur]  # Les cartes jouées sont stockées dans butin

    # Affichage des cartes jouées et du numéro de la manche
    print(f"\n^^^^ Manche {numero_manche} ^^^^")
    print(nom_joueur, "joue :", carte_du_joueur[0], "de", carte_du_joueur[1])
    print("L'ordinateur joue :", carte_ordinateur[0], "de", carte_ordinateur[1])

    # Comparaison des cartes (les types de carte ne sont pas pris en compte)
    gagnant = comparer_cartes(carte_du_joueur, carte_ordinateur)

    if gagnant == "bataille":
        print("Il y a bataille !")
        # Chaque joueur pose une carte face cachée
        butin.extend([deck_joueur.popleft(), deck_ordinateur.popleft()])
        # On relance une manche pour départager la bataille
        return jouer_manche(deck_joueur, deck_ordinateur, numero_manche, nom_joueur)
    else:
        return gagnant, butin

# Boucle principale du jeu
cartes_recuperees = {"joueur": 0, "ordinateur": 0}  # Compteur de cartes récupérées par chaque joueur
numero_manche = 1  # Compteur de manches

while deck_joueur and deck_ordinateur:  # Continue tant que les deux decks ont des cartes
    # Jouer une manche
    gagnant, butin = jouer_manche(deck_joueur, deck_ordinateur, numero_manche, nom_joueur)

    if gagnant:  # Si la manche a un gagnant, ajouter les cartes à son score
        cartes_recuperees[gagnant] += len(butin)
    # Affichage des résultats de la manche
    print(f"Cartes récupérées : {nom_joueur} {cartes_recuperees['joueur']} - Ordinateur {cartes_recuperees['ordinateur']}")
    print(f"Cartes restantes : {nom_joueur} {len(deck_joueur)} | Ordinateur {len(deck_ordinateur)}")
    input("Appuyez sur Entrée pour continuer...")  # Attendre que l'utilisateur appuie sur Entrée

    # Passer à la manche suivante
    numero_manche += 1

# Résultat final
print("\n XXX Fin de la partie XXX")
print(f"Total des cartes récupérées : {nom_joueur} {cartes_recuperees['joueur']} - Ordinateur {cartes_recuperees['ordinateur']}")
if cartes_recuperees["joueur"] > cartes_recuperees["ordinateur"]:  # Le joueur a plus de cartes
    print(f"Félicitations, {nom_joueur}, vous avez gagné !")
elif cartes_recuperees["joueur"] < cartes_recuperees["ordinateur"]:  # L'ordinateur a plus de cartes
    print(f"Dommage, {nom_joueur}, l'ordinateur a gagné !")
else:  # Égalité
    print(f"Match nul, {nom_joueur} !")