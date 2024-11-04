import sys

class Restaurant:
    def __init__(self):
        self.table = []
        self.table_libre = {}
        for i in range (1,21):
            new_table = Table(i,self.table)
            self.table.append(new_table)
            self.table_libre[i] = new_table

    def ouvrir(self):
        main()

    def fermer(self):
        sys.exit("Fermeture du restaurant")

    def calcul_stat(self,nbr):
        pass


class Table:
    def __init__(self, num_table,tables, nbr_place=4, etat_table="libre", num_commande=None):
        self.nbr_place = nbr_place
        self.tables = tables
        self.num_table = num_table
        self.etat_table = etat_table
        self.__num_commande = num_commande
        self.table_merged = [] #tables fusionnées avec la table en question

    def regrouper_table(self, *table):
        plus_petit_num_table = self
        table_to_merge = []
        table_to_merge.append(self)
        for i in table:
            table_to_merge.append(i)
            if i.num_table < plus_petit_num_table.num_table:
                plus_petit_num_table = i
        place_en_plus = 0
        for i in table_to_merge:
            if i.num_table != plus_petit_num_table.num_table:
                place_en_plus += i.nbr_place
                i.nbr_place -= i.nbr_place
                i.etat_table = "fusionne"
                self.table_merged.append(i)
        plus_petit_num_table.nbr_place += place_en_plus

    def defusionner_table(self):
        for i in self.table_merged:
            i.etat_table = "libre"
            i.nbr_place = int(self.nbr_place/(len(self.table_merged)+1))
        self.nbr_place = int(self.nbr_place/(len(self.table_merged)+1))


    def changer_etat_table(self, etat):
        if etat != "libre":
            self.etat_table = etat



class Reservation:
    def __init__(self,num_reservation,nom_pers, rdv, nbr_pers, num_table):
        self.__num_reservation = num_reservation
        self.__nom_pers = nom_pers
        self.__rdv = rdv
        self.__nbr_pers = nbr_pers
        self.__num_table = num_table

    def modifier(self,rdv, nbr_pers):
        self.__rdv = rdv
        self.__nbr_pers = nbr_pers

    def annuler(self):
        pass


class Commande:
    def __init__(self,num_commande, plats, etat_commande):
        self.__num_commande = num_commande
        self.__plats = plats
        self.__etat_commande = etat_commande

    def ajouter_plat(self,plat):
        self.__plats.append(plat)

    def changer_etat_commande(self,etat_commande):
        self.__etat_commande = etat_commande

class Client:
    def __init__(self,nom,phone):
        self.__nom = nom
        self.__phone = phone

    def contacter(self):
        pass

class Plat:
    def __init__(self, nom, liste_ingredients, prix, etat_plat):
        self.__nom = nom
        self.__liste_ingredients = liste_ingredients
        self.__prix = prix
        self.__etat_plat = etat_plat

    def retirer_ingredient(self,nom):
        pass

class Statistique:
    def __init__(self):
        pass



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