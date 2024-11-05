class Table:
    def __init__(self, num_table, nbr_place=4, etat_table="libre", num_commande=None):
        self._nbr_place = nbr_place
        self._num_table = num_table
        self._etat_table = etat_table
        self._num_commande = num_commande
        self._table_merged = [] # Tables fusionnées avec la Table en question

    @property
    def nbr_place(self):
        return self._nbr_place

    @nbr_place.setter
    def nbr_place(self, places):
        if places >= 0:
            self._nbr_place = places
        else:
            raise ValueError("Le nombre de places ne peut pas être négatif")

    # Getter et Setter pour _etat_table
    @property
    def etat_table(self):
        return self._etat_table

    @etat_table.setter
    def etat_table(self, etat):
        if etat in ["libre", "occupe", "nettoyage", "fusionne"]:
            self._etat_table = etat
        else:
            raise ValueError("L'état de la table doit être 'libre', 'occupe' ou 'fusionne'")

    # Getter pour _num_table (pas de setter car il ne devrait pas être modifié)
    @property
    def num_table(self):
        return self._num_table

    # Getter et Setter pour _num_commande
    @property
    def num_commande(self):
        return self._num_commande

    @num_commande.setter
    def num_commande(self, commande):
        self._num_commande = commande

    def regrouper_table(self, *table):
        plus_petit_num_table = self # Table avec le plus petit num_table
        table_to_merge = [self] # tableau des Tables à fusionner
        for i in table:
            table_to_merge.append(i)
            if i._num_table < plus_petit_num_table._num_table:
                plus_petit_num_table = i
        place_en_plus = 0 # place des tables à regrouper
        for i in table_to_merge:
            if i._num_table != plus_petit_num_table._num_table:
                place_en_plus += i._nbr_place
                i._nbr_place -= i._nbr_place
                i._etat_table = "fusionne"
                self._table_merged.append(i)
        plus_petit_num_table._nbr_place += place_en_plus # Rajout des places récupérées à la Table "Principale"

    def defusionner_table(self):
        for i in self._table_merged:
            i._etat_table = "libre"
            i._nbr_place = int(self._nbr_place/(len(self._table_merged)+1))
        self._nbr_place = int(self._nbr_place/(len(self._table_merged)+1))
        self._table_merged = []
