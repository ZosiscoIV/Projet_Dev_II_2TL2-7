from commande import Commande


class Table:
    def __init__(self, num_table, nbr_place=4, etat_table="L", commande=None):
        """
        Initialise une table
        PRE : num_table est un entier positif
              nbr_table est un entier positif
              etat_table est un caractère dans ["O", "L", "N", "R", "F"]
              commande est un objet de Commande
        POST : Crée une instance de Commande
        """
        self._nbr_place = nbr_place
        self._num_table = num_table
        self._etat_table = etat_table
        self._commande = commande
        self._table_merged = [] # Tables fusionnées avec la Table en question

    @property
    def nbr_place(self):
        """
        Retourne le nombre de places de la table
        POST : Retourne  le nombre de places de la table
        """
        return self._nbr_place

    @nbr_place.setter
    def nbr_place(self, places):
        """ Change le nombre de place d'une table
        PRE : places est un entier positif
        POST : modifie le nombre de place à une table
        Raise : ValueError si places est plus petit que 0 ou n'est pas un entier
        """
        if isinstance(places, int) and places >= 0:
            self._nbr_place = places
        else:
            raise ValueError("Le nombre de places doit être un entier positif")

    # Getter et Setter pour _etat_table
    @property
    def etat_table(self):
        """
        Retourne l'état de la table
        POST : Retourne  l'état de la table
        """
        return self._etat_table

    @etat_table.setter
    def etat_table(self, etat):
        """ Change l'état d'une table
        PRE : etat est un carractère dans ["O", "L", "N", "R", "F"]
        POST : modifie l'état de la table
        Raise : ValueError si l'état est pas l'un de ces caractères ["O", "L", "N", "R", "F"]
        """
        if isinstance(etat, str) and etat in ["O", "L", "N", "R", "F"]:
            self._etat_table = etat
        else:
            raise ValueError("L'état de la table doit être O-occupé, L-libre, N-nettoyage, R-réservé, F-fusionné")

    # Getter pour _num_table (pas de setter car il ne devrait pas être modifié)
    @property
    def num_table(self):
        """
        Retourne le numéro de la table
        POST : Retourne  le numéro de la table
        """
        return self._num_table

    # Getter et Setter pour _num_commande
    @property
    def commande(self):
        """
        Retourne l'objet de Commande
        POST : Retourne  l'objet de Commande
        """
        return self._commande

    @commande.setter
    def commande(self, new_commande):
        """ Associe à la table une commande
        PRE : new_commande est un objet Commande
        POST : associe new_commande à la table
        RAISE : TypeError si new_commande n'est pas une instance de Commande
        """
        if isinstance(new_commande, Commande):
            self._commande = new_commande
        else:
            raise TypeError("La commande doit être une instance de Commande")

    def regrouper_table(self, *table):
        """
        Fusionne plusieurs tables en une seule, augmentant le nombre de places disponibles.

        PRE : `table` est une liste d'objets Table valides.
        POST : Fusionne les tables en une seule avec le nombre total de places, et change l'état des tables fusionnées à 'fusionné'.
        RAISE : ValueError lorsqu'une table n'est pas de type Table.
        """
        plus_petit_num_table = self  # Table avec le plus petit num_table
        table_to_merge = [self]  # Tableau des Tables à fusionner
        for i in table:
            if not isinstance(i, Table):
                raise ValueError("L'une des tables fournie n'est pas de type table.")
            table_to_merge.append(i)
            if i._num_table < plus_petit_num_table._num_table:
                plus_petit_num_table = i
        place_en_plus = 0  # Places des tables à regrouper
        for i in table_to_merge:
            if i._num_table != plus_petit_num_table._num_table:
                place_en_plus += i._nbr_place
                i._nbr_place -= i._nbr_place
                i._etat_table = "fusionné"
        plus_petit_num_table._nbr_place += place_en_plus  # Rajout des places récupérées à la Table principale

    def defusionner_table(self):
        """
        Défusionne un table
        POST : resépare les tables, remet l'état de la table en libre et le nombre de places d'origine.
        """
        for i in self._table_merged:
            i._etat_table = "libre"
            i._nbr_place = int(self._nbr_place/(len(self._table_merged)+1))
        self._nbr_place = int(self._nbr_place/(len(self._table_merged)+1))
        self._table_merged = []
