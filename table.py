class Table:
    def __init__(self, num_table, nbr_place=4, etat_table="libre", num_commande=None):
        self.nbr_place = nbr_place
        self.num_table = num_table
        self.etat_table = etat_table
        self.__num_commande = num_commande
        self.table_merged = [] # Tables fusionnées avec la Table en question

    def regrouper_table(self, *table):
        plus_petit_num_table = self # Table avec le plus petit num_table
        table_to_merge = [self] # tableau des Tables à fusionner
        for i in table:
            table_to_merge.append(i)
            if i.num_table < plus_petit_num_table.num_table:
                plus_petit_num_table = i
        place_en_plus = 0 # place des tables à regrouper
        for i in table_to_merge:
            if i.num_table != plus_petit_num_table.num_table:
                place_en_plus += i.nbr_place
                i.nbr_place -= i.nbr_place
                i.etat_table = "fusionne"
                self.table_merged.append(i)
        plus_petit_num_table.nbr_place += place_en_plus # Rajout des places récupérées à la Table "Principale"

    def defusionner_table(self):
        for i in self.table_merged:
            i.etat_table = "libre"
            i.nbr_place = int(self.nbr_place/(len(self.table_merged)+1))
        self.nbr_place = int(self.nbr_place/(len(self.table_merged)+1))
        self.table_merged = []


    def changer_etat_table(self, etat):
        # if etat != "libre":
        self.etat_table = etat