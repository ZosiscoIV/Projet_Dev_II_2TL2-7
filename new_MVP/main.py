from table import Table
from commande import Commande
from plat import Plat

# Listes pour stocker les tables libres et occupées
tables_libres = []
tables_occupees = []

# Initialisation de 20 tables (numérotées de 1 à 20) comme libres
for i in range(1, 21):
    table = Table(i)
    tables_libres.append(table)

# Boucle principale pour interagir avec l'utilisateur
while True:
    # Affichage des options et choix de l'action par l'utilisateur
    action = int(input("1) Nouvelle table 2) Voir tables vides 3) Changer état table\n"))

    if action == 1:
        # Choix de la table à occuper
        numero_table = int(input("Entrez un numéro de table : "))
        # Vérification que le numéro de table est valide
        while numero_table <= 0 or numero_table > 20:
            numero_table = int(input("Numéro invalie, entrez un autre numéro de table : "))
        # Recherche de l'index de la table choisie dans la liste des tables libres
        index_table_a_changer = None
        for i in range(len(tables_libres)):
            if tables_libres[i].num_table != numero_table:
                pass
            else:
                index_table_a_changer = i
        # Si elle est trouvée dans la liste des tables libres, passage dans les tables occupées
        if index_table_a_changer is not None:
            table_a_changer = tables_libres.pop(index_table_a_changer)
            tables_occupees.append(table_a_changer)
        else:
            print("La table est déjà occupée")

        # print(tables_occupees)
        # print(len(tables_libres))
        # for i in range(len(tables_occupees)):
        #     print(tables_occupees[i].num_table)

    # Non implémenté
    elif action == 2:
        pass
    # Non implémenté
    elif action == 3:
        pass
    # Cas ou l'action n'est pas une option valide
    else:
        print("Action invalide")