from restaurant import Restaurant
from old_MVP.client import Client
from plat import Plat





def main():
    print("okay")
    print(Fourchette.table)

# Utilisation de la classe Restaurant et des méthodes de Table
Fourchette = Restaurant()

# Utiliser changer_etat_table pour mettre la table 0 en "occupe"
Fourchette.table[0].etat_table = "occupe"
print(Fourchette.table[0].etat_table)  # Utiliser le getter pour obtenir l'état de la table

# Regrouper les tables (fusionner table 3 avec table 6 et table 7)
Fourchette.table[3].regrouper_table(Fourchette.table[6], Fourchette.table[7])
print(Fourchette.table[3].nbr_place, Fourchette.table[3].etat_table)  # Vérification des places et état de table 3

# Vérifier l'état et le nombre de places des tables fusionnées (table 6 et table 7)
print(Fourchette.table[6].nbr_place, Fourchette.table[6].etat_table,
      Fourchette.table[7].nbr_place, Fourchette.table[7].etat_table)

# Défuser les tables fusionnées avec la table principale (table 3)
Fourchette.table[3].defusionner_table()

# Vérifier les attributs de la table 3 et des tables défusionnées (table 6 et table 7)
print(Fourchette.table[3].nbr_place, Fourchette.table[3].etat_table)
print(Fourchette.table[6].nbr_place, Fourchette.table[6].etat_table,
      Fourchette.table[7].nbr_place, Fourchette.table[7].etat_table)

# Creation d'un client
client1 = Client("M. Le Chicon", "0888 77 66 55")

# Contacter le client 1
print(client1.contacter())

# Creation d'un plat
platBolo = Plat("bolo",["pates", "bolo", "persil"], 12.50)

# Retirer l'element persil et print les autres ingrédients
platBolo.retirer_ingredient("persil")
print(platBolo._liste_ingredients)
