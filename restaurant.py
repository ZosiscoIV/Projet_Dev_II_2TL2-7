import sys
from table import Table
class Restaurant:
    def __init__(self):
        self.table = []
        self.table_libre = {}
        for i in range (1,21):
            new_table = Table(i)
            self.table.append(new_table) # [Table(1),Table(2), ...]
            self.table_libre[i] = new_table # {1:Table(1),2:Table(2), ...}

    def ouvrir(self):
        pass
        #main()

    def fermer(self):
        pass
        #sys.exit("Fermeture du restaurant")

    def calcul_stat(self,nbr):
        pass
