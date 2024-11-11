import json

from table import Table
from commande import Commande
from plat import Plat


# Liste pour stocker les tables
tables = []
# tables_libres = []
# tables_occupees = []
# tables_nettoyage = []
# tables_reservees = []
# tables_fusionnees = []

compteur_commande = 1

with open('menu.json', 'r') as file:
    menu = json.load(file)
    print(menu)


# Initialisation de 20 tables (numérotées de 1 à 20) comme libres
for i in range(1, 21):
    table = Table(i)
    tables.append(table)

def choix_table():
    # Choix de la table à changer son état
    num = int(input("Entrez un numéro de table : "))
    # Vérification que le numéro de table est valide
    while num <= 0 or num > 20:
        num = int(input("Numéro invalie, entrez un autre numéro de table : "))
    return num

# Boucle principale pour interagir avec l'utilisateur
while True:
    # Affichage des options et choix de l'action par l'utilisateur
    action = int(input("1) Changer état table 2) Voir toutes les tables 3) Créer une commande \n"))

    if action == 1:
        numero_table = choix_table()

        # Choix de l'état de la table choisie et le changer
        table_a_changer = tables[numero_table-1]
        nouvel_etat_table = input("Choisissez l'état : O-occupé, L-libre, N-nettoyage, R-réservé, F-fusionné \n")
        # Vérification que l'état est valide
        while nouvel_etat_table not in ["O", "L", "N", "R", "F"]:
            nouvel_etat_table = input("Etat invalie, entrez un autre état : O-occupé, L-libre, N-nettoyage, R-réservé, F-fusionné \n")

        table_a_changer.etat_table = nouvel_etat_table

    # affiche les tables avec les couleurs en fonction de leur état
    elif action == 2:
        tables_a_afficher = []
        for i in tables:
            tables_a_afficher.append((i.num_table, i.etat_table))

        str_tables_a_afficher = ""
        for i in tables_a_afficher:
            if str(i[1]) == "O":
                str_tables_a_afficher += f"\033[31mTable{str(i[0])}\033[0m"  + ", " # Rouge
            elif str(i[1]) == "L":
                str_tables_a_afficher += f"\033[32mTable{str(i[0])}\033[0m"  + ", " # Vert
            elif str(i[1]) == "N":
                str_tables_a_afficher += f"\033[33mTable{str(i[0])}\033[0m"  + ", " # Jaune
            elif str(i[1]) == "R":
                str_tables_a_afficher += f"\033[34mTable{str(i[0])}\033[0m"  + ", " # Bleu
            elif str(i[1]) == "F":
                str_tables_a_afficher += f"\033[35mTable{str(i[0])}\033[0m"  + ", " # Mauve
            else:
                print("Erreur lors de l'affichage des tables")
        str_tables_a_afficher = str_tables_a_afficher[:-2]
        print(str_tables_a_afficher)

    # Non implémenté
    elif action == 3:
        numero_table = choix_table()
        if tables[numero_table-1].commande is None:
            commande = Commande(compteur_commande)
            tables[numero_table-1].commande = commande
        else:
            commande = tables[numero_table-1].commande

        demande = int(input("1) Entrer plat 2) Retirer plat 3) Changer état commande \n "))

        if demande == 1:
            string = ""
            for i in range(len(menu)):
                string += str(i + 1) + ") " + menu[i]["nom"] + " "

            plat = int(input("Entrez un plat : " + string  + "\n "))
            while plat not in [1,2,3]:
                plat = int(input("Entrez à nouveau le plat choisi : 1) Bolo 2) Pizza 3) Steak"))
            plat_a_ajouter = menu[plat - 1]
            commande.ajouter_plat(Plat(plat_a_ajouter["nom"],plat_a_ajouter["liste_ingredients"],plat_a_ajouter["prix"]))

        elif demande == 2:
            print(commande.plats)







    # Cas ou l'action n'est pas une option valide
    else:
        print("Action invalide")