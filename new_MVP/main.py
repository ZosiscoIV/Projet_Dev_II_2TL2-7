import json

from table import Table
from commande import Commande
from plat import Plat


# Liste pour stocker les tables
tables = []


# Compteur pour le numero de commande
compteur_commande = 1

# Acces au fichier nemu.json
with open('menu.json', 'r') as file:
    menu = json.load(file)
    # print(menu)


# Initialisation de 20 tables (numérotées de 1 à 20) comme libres
for i in range(1, 21):
    table = Table(i)
    tables.append(table)

# Choix de la table
def choix_table():
    num = input("Entrez un numéro de table : ")
    # Vérification que le numéro de table est valide
    while not num.isdigit() or (int(num) <= 0 or int(num) > 20):
        num = input("Numéro invalie, entrez un autre numéro de table : ")
    return int(num)

# Boucle principale pour interagir avec l'utilisateur
while True:
    # Affichage des options et choix de l'action par l'utilisateur
    action = input("1) Changer état table 2) Voir toutes les tables 3) Créer une commande \n")
    while action not in ["1", "2", "3"]:
        action = input("Action invalie, entrez une autre action\n")
    action = int(action)

    if action == 1:
        numero_table = choix_table()

        # Choix de l'état de la table choisie et le changer
        table_a_changer = tables[numero_table-1]
        nouvel_etat_table = input("Choisissez l'état : O-occupé, L-libre, N-nettoyage, R-réservé, F-fusionné \n")
        # Vérification que l'état est valide
        while nouvel_etat_table.upper() not in ["O", "L", "N", "R", "F"]:
            nouvel_etat_table = input("Etat invalie, entrez un autre état : O-occupé, L-libre, N-nettoyage, R-réservé, F-fusionné \n")

        table_a_changer.etat_table = nouvel_etat_table.upper()

    # Affiche les tables avec les couleurs en fonction de leur état
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

    # Créer une commande
    elif action == 3:
        # Obtenir le numéro de table auquel il faut associer la commande
        numero_table = choix_table()

        # Créer la Commande au numéro de table si elle n'existe pas ou la récupérer
        if tables[numero_table-1].commande is None:
            commande = Commande(compteur_commande)
            tables[numero_table-1].commande = commande
            # Augmenter le compteur du numéro de commande
            compteur_commande += 1
        else:
            commande = tables[numero_table-1].commande

        while True:
            # Demande à l'utilisateur ce qu'il veut faire
            demande = input("1) Ajouter plat 2) Retirer plat 3) Afficher la commande 4) Retour \n ")
            while demande not in ["1","2","3","4"]:
                demande = input("Action invalie, entrez une autre action\n")
            demande = int(demande)
            # Ajouter un plat dans la commande
            if demande == 1:
                # Chaine de tous les plats présents dans menu
                string_menu = ""
                for i in range(len(menu)):
                    string_menu += str(i + 1) + ") " + menu[i]["nom"] + " "
                print("Menu : " + string_menu)
                while True:
                    # Choix du plat
                    plat = input("Entrez un numéro de plat ou 'stop' pour arrêter\n ")
                    # Vérification du numéro du plat choisi
                    if plat.lower() == "stop":
                        break
                    while not plat.isdigit() or (int(plat) <= 0 or int(plat) > len(menu)):
                        plat = input("Entrez un numéro valide de plat ou 'stop' pour arrêter\n ")
                        if plat.lower() == "stop":
                            break
                    if plat.lower() == "stop":
                        break
                    # Ajouter le plat à la commande
                    plat_a_ajouter = menu[int(plat) - 1]
                    commande.ajouter_plat(
                        Plat(plat_a_ajouter["nom"], plat_a_ajouter["liste_ingredients"], plat_a_ajouter["prix"]))
                    print(f"Le plat {plat_a_ajouter["nom"]} à été ajouté")

            # Retirer un plat dans Commande
            elif demande == 2:
                plats_commandes = commande.plats
                if len(plats_commandes) >= 1:
                    string_plats_commandes = ""
                    for i in range(len(plats_commandes)):
                        string_plats_commandes += str(i + 1) + ") " + plats_commandes[i].nom + " "
                    # Choix du plat à retirer
                    plat_a_retirer = input("Entrez un plat à retirer : " + string_plats_commandes + "\n ")
                    # Vérification du numéro du plat choisi
                    while not plat_a_retirer.isdigit() or (int(plat_a_retirer) <= 0 or int(plat_a_retirer) > len(plats_commandes)):
                        plat_a_retirer = input("Entrez à nouveau le plat à retirer : " + string_plats_commandes + "\n ")
                    commande.retirer_plat(int(plat_a_retirer)-1)
                else:
                    print("Pas de plat à retirer dans la commande")


            # Afficher la commande
            elif demande == 3:
                plats_commandes = commande.plats
                if len(plats_commandes) >= 1:
                    string_plats_commandes = f"Commande n°{commande.num_commande} : "
                    for i in range(len(plats_commandes)):
                        string_plats_commandes += str(i + 1) + ") " + plats_commandes[i].nom + " "
                    print(string_plats_commandes)
                else:
                    print("Pas de plats dans la commande")

            elif demande == 4:
                break

            else:
                print("Erreur dans la commande")



    # Cas ou l'action n'est pas une option valide
    else:
        print("Action invalide")