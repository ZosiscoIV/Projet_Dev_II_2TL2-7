import json
from datetime import datetime

from table import Table #, regrouper_table, defusionner_table
from commande import Commande
from plat import Plat
from client import Client
from reservation import Reservation


# Liste pour stocker les tables
tables = []

# Liste de réservation
reservations = []


# Compteur pour le numero de commande
compteur_commande = 1

# annee_actuelle
annee_actuelle = datetime.now().year

# mois_actuel
mois_actuel = datetime.now().month

# jour_actuel
jour_actuel = datetime.now().day


# Acces au fichier menu.json
with open('menu.json', 'r') as file:
    menu = json.load(file)
    # print(menu)


# Initialisation de 20 tables (numérotées de 1 à 20) comme libres
for i in range(1, 21):
    table = Table(i)
    tables.append(table)

# Choix de la table
def choix_table(mes=""):
    num = input(f"Entrez un numéro de table {mes}: ")
    # Vérification que le numéro de table est valide
    while not num.isdigit() or (int(num) <= 0 or int(num) > 20):
        if mes:
            if num == "stop":
                return num
        num = input(f"Numéro invalie, entrez un autre numéro de table {mes}: ")
    return int(num)


# Choix du moment de la réservation
def choix_rdv():
    # Demande à l'utilisateur l'année de la réservation
    annee = input("Entrez l'année'\n")
    #Vérification de l'année
    while not annee.isdigit() or int(annee) < annee_actuelle:
        annee = input("Entrée invalide, entrez à nouveau l'année\n")

    # Demande à l'utilisateur le mois de la réservation
    mois = input("Entrez le mois\n")
    # Vérification du mois
    while not mois.isdigit() or (int(mois) < 1 or int(mois) > 12) or int(mois) < mois_actuel:
        mois = input("Entrée invalide, entrez à nouveau le mois\n")

    # Demande à l'utilisateur le jour de la réservation
    jour = input("Entrez le jour\n")
    # Vérification du jour
    while not jour.isdigit() or (int(jour) <= 0 or int(jour) > 31) or int(jour) < jour_actuel:
        jour = input("Entrée invalide, entrez à nouveau le jour'\n")

    # Demande à l'utilisation l'heure de la réservation
    heure_minute = input("Entrez l'heure format (HH:MM)'\n")
    # Vérification de l'heure, si elle elle valide, séparation des heures et minutes sinon erreur et on redemande
    while True:
        try:
            heure, minute = map(int, heure_minute.split(":"))
            if 0 <= heure <= 23 and 0 <= minute <= 59:
                break
            else:
                print("L'heure doit être entre 00:00 et 23:59.")
        except ValueError:
            print("Le format doit être HH:MM avec des nombres valides.")
        heure_minute = input("Entrez l'heure au format (HH:MM) :\n")

    # Trasformation des intup en format date
    rendez_vous = datetime(year=int(annee), month=int(mois), day=int(jour), hour=int(heure), minute=int(minute))

    return rendez_vous

# Retrouver la réservation en fonction du nom
def trouver_reservation():
    res = None
    nom_client_pour_changer_sa_reservation = input("Entrez le nom du client\n")
    # Vérification du nom
    verif = input(f"Etes vous sûr du nom \033[4m{nom_client_pour_changer_sa_reservation}\033[0m : O-oui, N-non\n")
    while verif.upper() != "O":
        nom_client_pour_changer_sa_reservation = input("Entrez à nouveau le nom du client\n")
        verif = input(
            f"Etes vous sûr du nom \033[4m{nom_client_pour_changer_sa_reservation}\033[0m : O-oui, N-non\n")
    # Recherche l'objet de la reservation dont le nom a été donné
    for i in reservations:
        if i.client.nom == nom_client_pour_changer_sa_reservation:
            res = i
            break
    return res

def fusion_table():
    liste_tables= []
    while True:
        n = input("Entrez un numéro de table ou 'stop' pour arrêter\n ")
        if n.lower() == "stop":
            break
        # Vérification que le numéro de table est valide
        while not n.isdigit() or (int(n) <= 0 or int(n) > 20):
            n = input("Numéro invalie, entrez un autre numéro de table ou 'stop' pour arrêter \n ")
            if n.lower() == "stop":
                break
        if n.lower() == "stop":
            break
        for i in tables:
            if i.num_table == int(n):
                liste_tables.append(i)
                break
    return liste_tables


# Boucle principale pour interagir avec l'utilisateur
while True:
    # Affichage des options et choix de l'action par l'utilisateur
    action = input("1) Changer état table 2) Voir toutes les tables 3) Créer une commande 4) Gérer une réservation \n")
    while action not in ["1", "2", "3", "4"]:
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
                    commande.ajouter_plat(Plat(plat_a_ajouter["nom"], plat_a_ajouter["liste_ingredients"], plat_a_ajouter["prix"]))
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

    # Gerer les réservations
    elif action == 4:
        while True:
            demande = input("1) Ajouter réservation 2) Modifier une réservation 3) Annuler une réservation 4) Afficher toutes les réservations 5) Fusionner et défusionner une table 6) Retour \n ")
            while demande not in ["1", "2", "3", "4", "5", "6"]:
                demande = input("Action invalie, entrez une autre action\n")
            demande = int(demande)

            # Ajouter une réservation
            if demande == 1:

                # Demande le nom du client et vérification
                nom_client = input("Entrez le nom du client\n")
                verif_nom = input(f"Etes vous sûr du nom \033[4m{nom_client}\033[0m : O-oui, N-non\n")
                while verif_nom.upper() != "O":
                    nom_client = input("Entrez à nouveau le nom du client\n")
                    verif_nom = input(f"Etes vous sûr du nom \033[4m{nom_client}\033[0m : O-oui, N-non\n")

                # Demande le numéro de téléphone du client et vérification
                tel = input("Entrez le numéro de téléphone du client\n")
                verif_tel = input(f"Etes vous sûr du téléphone \033[4m{tel}\033[0m : O-oui, N-non\n")
                while verif_tel.upper() != "O":
                    tel = input("Entrez à nouveau le numéro de téléphone du client\n")
                    verif_tel = input(f"Etes vous sûr du téléphone \033[4m{tel}\033[0m : O-oui, N-non\n")

                # Demande les informations du rdv de la réservation et vérification
                rdv = choix_rdv()
                verif_rdv = input(f"Etes vous sûr du rendez-vous \033[4m{rdv.strftime("%d/%m/%Y à %H:%M")}\033[0m : O-oui, N-non\n")
                while verif_rdv.upper() != "O":
                    rdv = choix_rdv()
                    verif_rdv = input(f"Etes vous sûr du rendez-vous \033[4m{rdv.strftime("%d/%m/%Y à %H:%M")}\033[0m : O-oui, N-non\n")

                # Demande le nombre de personnes
                quantite_pers = input("Entrez le nombre de personnes pour la réservation\n")
                while not quantite_pers.isdigit() or (int(quantite_pers) <= 0 or int(quantite_pers) > 50):
                    quantite_pers = input("Entrez à nouveau le nombre de personnes pour la réservation\n")

                # Demande le numéro de table auquel il faut mettre la réservation
                numero_table = choix_table()

                # Création de l'intance client
                client = Client(nom_client, tel)
                # Création de l'intance reservation
                reservation = Reservation(client,rdv,quantite_pers,numero_table)
                # Ajout de la réservation à la liste des réservations
                reservations.append(reservation)
                # Mettre l'état de la table en réservé
                tables[numero_table - 1].etat_table = "R"

            # Modification de la réservation
            elif demande == 2:
                reservation = trouver_reservation()
                # Demande ce qui doit êre modifier si pas trouvé il y a une erreur
                if reservation:
                    changement = input("Vouler-vous changer le : 1) Rendez-vous 2) Nombre de personne 3) les deux \n")
                    while changement not in ["1", "2", "3"]:
                        changement = input("Entrée invalide, vouler-vous changer le : 1) Rendez-vous 2) Nombre de personne 3) les deux \n")
                    changement = int(changement)

                    # Changement uniquement du rendez-vous
                    if changement == 1:
                        rdv_nouveau = choix_rdv()
                        reservation.modifier(rdv = rdv_nouveau)

                    # Changement uniquement du nombre de personnes
                    elif changement == 2:
                        nbr_pers_nouveau = input("Entrez le nombre de personnes pour la réservation\n")
                        while not nbr_pers_nouveau.isdigit() or (int(nbr_pers_nouveau) <= 0 or int(nbr_pers_nouveau) > 50):
                            nbr_pers_nouveau = input("Entrez à nouveau le nombre de personnes pour la réservation\n")
                        reservation.modifier(nbr_pers = nbr_pers_nouveau)

                    # Changement du rendez-vous et du nombre de personnes
                    elif changement == 3:
                        rdv_nouveau = choix_rdv()
                        nbr_pers_nouveau = input("Entrez le nombre de personnes pour la réservation\n")
                        while not nbr_pers_nouveau.isdigit() or (int(nbr_pers_nouveau) <= 0 or int(nbr_pers_nouveau) > 50):
                            nbr_pers_nouveau = input("Entrez à nouveau le nombre de personnes pour la réservation\n")
                        reservation.modifier(rdv_nouveau,nbr_pers_nouveau)

                    else:
                        ValueError("Erreur dans la modification de la réservation")
                else:
                    ValueError("Le client n'a pas été trouvé")
                    print("Le client n'a pas été trouvé \n")

            # Annulation de la réservation
            elif demande == 3:
                reservation = trouver_reservation()
                # Enlève la réservation de la liste réservations
                reservations.remove(reservation)
                check_num = None
                # Si il y a une autre réservation pour la même table, son état reste comme il est, sinon on passe la table en libre
                for i in reservations:
                    if i.num_table == reservation.num_table:
                        check_num = i.num_table
                    else:
                        pass
                if check_num is None:
                    tables[reservation.num_table - 1].etat_table = "L"

            # Affichage des réservations
            elif demande == 4:
                # Tri sur les dates
                reservations = sorted(reservations, key = lambda t: t.rdv)
                for i in reservations:
                    print(f"Nom : {i.client.nom}, date: {i.rdv.strftime("%d/%m/%Y à %H:%M")}, le nombre de personne : {i.nbr_pers}, le n° de table : {i.num_table}")

            # Fusion ou défusion d'une table
            elif demande == 5:
                question = input("Voulez-vous 1) fusionner des tables 2) défusionner des tables \n")
                while question not in ["1", "2"]:
                    question = input("Entrée invalide, voulez-vous 1) fusionner des tables 2) défusionner des tables \n")
                if question == "1":
                    while True:
                        table_a_fuse = choix_table()
                        table_a_merge = []
                        table_a_merge = set(table_a_merge)
                        isDebile = False
                        while True:
                            table_a_ajouter = choix_table("à fusionner ou stop pour quitter ")
                            if table_a_ajouter == "stop":
                                break
                            if table_a_fuse == table_a_ajouter:
                                isDebile = True
                            table_a_merge.add(table_a_ajouter)
                        if len(table_a_merge) == 0:
                            print("Aucune tables à fusionner")
                            break
                        if isDebile:
                            table_a_merge.remove(table_a_fuse)
                        verif = input("Êtes vous sûr de vouloir fusionner la/les table(s) " + ', '.join(map(str, table_a_merge)) + " à la table " + str(table_a_fuse) + " : O-oui, N-non \n")
                        if verif.upper() == "O":
                            break
                    tables[table_a_fuse - 1].regrouper_table(table_a_merge)
                    print("Les tables ont bien été fusionnées")

                elif question == "2":
                    pass
                    # table_a_fuse = choix_table("")
                    # table_a_merge = []
                    # while True:
                    #     table_a_ajouter = choix_table("à fusionner ou stop pour quitter ")




                # question = input("Voulez-vous 1) fusionner des tables 2) défusionner des tables \n")
                # while question not in ["1", "2"]:
                #     question = input("Entrée invalide, voulez-vous 1) fusionner des tables 2) défusionner des tables \n")
                # if question == "1":
                #     liste_tables_a_fusionner = fusion_table()
                #
                #     liste_tables_a_fusionner[0].regrouper_table(liste_tables_a_fusionner[1:])
                #
                # elif question == "2":
                #     liste_tables_a_defusionner = fusion_table()
                #     liste_tables_a_defusionner[0].defusionner_table(liste_tables_a_defusionner[1:])
                #
                # else:
                #     print("erreur")
                #     ValueError("Erreur lors de la fusion ou de la défusion")

            elif demande == 6:
                break


            else:
                print("Erreur dans la réservation")

    # Cas ou l'action n'est pas une option valide
    else:
        print("Action invalide")