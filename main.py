from restaurant import Restaurant
from table import Table
from reservation import Reservation
from commande import Commande
from client import Client
from plat import Plat





def main():
    print("okay")
    print(Fourchette.table)

Fourchette = Restaurant()
#Fourchette.ouvrir()
Fourchette.table[0].changer_etat_table("occupe")
print(Fourchette.table[0].etat_table)
Fourchette.table[3].regrouper_table(Fourchette.table[6],Fourchette.table[7])
print(Fourchette.table[3].nbr_place, Fourchette.table[3].etat_table)
print(Fourchette.table[6].nbr_place, Fourchette.table[6].etat_table, Fourchette.table[7].nbr_place, Fourchette.table[7].etat_table)
Fourchette.table[3].defusionner_table()
print(Fourchette.table[3].nbr_place, Fourchette.table[3].etat_table)
print(Fourchette.table[6].nbr_place, Fourchette.table[6].etat_table, Fourchette.table[7].nbr_place, Fourchette.table[7].etat_table)