import random 
from collections import deque

# Cette ligne demande au joueur d'entrer le nom qu'il va utiliser durant la partie
nom_joueur = input("Entrez votre nom de joueur : ") or "Joueur"  # Si le joueur n'entre rien, utiliser "Joueur" par défaut

# Ordre des cartes
ordre_des_cartes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'AS']

# Valeur des cartes pour le système de points
valeur_cartes = {k: i+2 for i, k in enumerate(ordre_des_cartes)}

# Création du jeu de 52 cartes (4 types de carte x 13 valeurs de carte)
types_de_carte = ['Coeur', 'Carreau', 'Trèfle', 'Pique']  # Les 4 types de carte
deck_principal = [(ordre_carte, type_carte) 
             for type_carte in types_de_carte for ordre_carte in ordre_des_cartes
             ]  
random.shuffle(deck_principal)  # Mélange le jeu de cartes

# Distribution des cartes entre le joueur et l'ordinateur
deck_joueur = deque(deck_principal[::2])  # Le joueur reçoit les cartes aux indices pairs
deck_ordinateur = deque(deck_principal[1::2])  # L'ordinateur reçoit les cartes aux indices impairs

print(f"{nom_joueur}, la partie commence !")
print("Vous affrontez l'ordinateur.")

def comparer_cartes(carte_du_joueur, carte_ordinateur):
    """
    Compare deux cartes et retourne le gagnant ("joueur", "ordinateur") ou "bataille" en cas d'égalité.
    """
    index_joueur = ordre_des_cartes.index(carte_du_joueur[0])
    index_ordinateur = ordre_des_cartes.index(carte_ordinateur[0])

    if index_joueur > index_ordinateur:
        return "joueur"
    elif index_joueur < index_ordinateur:
        return "ordinateur"
    else:
        return "bataille"

def jouer_manche(deck_joueur, deck_ordinateur, numero_manche, nom_joueur):
    """
    Simule une manche du jeu avec points et gestion sécurisée de la bataille.
    """
    if not deck_joueur or not deck_ordinateur:
        return None, []

    carte_du_joueur = deck_joueur.popleft()
    carte_ordinateur = deck_ordinateur.popleft()
    butin = [carte_du_joueur, carte_ordinateur]

    print(f"\n^^^^ Manche {numero_manche} ^^^^")
    print(nom_joueur, "joue :", carte_du_joueur[0], "de", carte_du_joueur[1])
    print("L'ordinateur joue :", carte_ordinateur[0], "de", carte_ordinateur[1])

    gagnant = comparer_cartes(carte_du_joueur, carte_ordinateur)

    if gagnant == "bataille":
        print("Il y a bataille !")

        # Vérifier qu'il y a assez de cartes pour la bataille
        if len(deck_joueur) < 1 or len(deck_ordinateur) < 1:
            print("Un joueur n'a plus assez de cartes pour continuer la bataille !")
            return None, butin

        # Cartes face cachée
        butin.append(deck_joueur.popleft())
        butin.append(deck_ordinateur.popleft())

        # Rejouer pour départager
        gagnant_suivant, butin_supp = jouer_manche(deck_joueur, deck_ordinateur, numero_manche, nom_joueur)
        butin.extend(butin_supp)
        return gagnant_suivant, butin

    return gagnant, butin

# Boucle principale du jeu
cartes_recuperees = {"joueur": 0, "ordinateur": 0}
points = {"joueur": 0, "ordinateur": 0}  # Nouveau compteur de points
numero_manche = 1

while deck_joueur and deck_ordinateur:
    gagnant, butin = jouer_manche(deck_joueur, deck_ordinateur, numero_manche, nom_joueur)

    if gagnant:
        # Ajouter les cartes au compteur
        cartes_recuperees[gagnant] += len(butin)

        # Ajouter les points
        points[gagnant] += sum(valeur_cartes[c[0]] for c in butin)

        # Les cartes vont à la fin du deck du gagnant
        if gagnant == "joueur":
            deck_joueur.extend(butin)
        else:
            deck_ordinateur.extend(butin)

    # Affichage des résultats intermédiaires
    print(f"Cartes récupérées : {nom_joueur} {cartes_recuperees['joueur']} - Ordinateur {cartes_recuperees['ordinateur']}")
    print(f"Points : {nom_joueur} {points['joueur']} - Ordinateur {points['ordinateur']}")
    print(f"Cartes restantes : {nom_joueur} {len(deck_joueur)} | Ordinateur {len(deck_ordinateur)}")
    input("Appuyez sur Entrée pour continuer...")

    numero_manche += 1

# Résultat final
print("\n XXX Fin de la partie XXX")
print(f"Total des cartes récupérées : {nom_joueur} {cartes_recuperees['joueur']} - Ordinateur {cartes_recuperees['ordinateur']}")
print(f"Total des points : {nom_joueur} {points['joueur']} - Ordinateur {points['ordinateur']}")

if points["joueur"] > points["ordinateur"]:
    print(f"Félicitations, {nom_joueur}, vous avez gagné !")
elif points["joueur"] < points["ordinateur"]:
    print(f"Dommage, {nom_joueur}, l'ordinateur a gagné !")
else:
    print(f"Match nul, {nom_joueur} !")
