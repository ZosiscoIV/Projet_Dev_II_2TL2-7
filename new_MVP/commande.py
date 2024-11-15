class Commande:
    def __init__(self,num_commande, etat_commande= "C"):
        self._num_commande = num_commande
        self._etat_commande = etat_commande # commande et pret
        self._plats = []

    @property
    def num_commande(self):
        return self._num_commande

    @property
    def etat_commande(self):
        return self._etat_commande

    @etat_commande.setter
    def etat_commande(self, etat):
        if etat in ["C", "P"]:
            self._etat_commande = etat
        else:
            raise ValueError("L'état de la commande doit être 'C-commandé', 'P-prête'")

    @property
    def plats(self):
        return self._plats

    def ajouter_plat(self,plat):
        self._plats.append(plat)

    def retirer_plat(self, index_plat):
        """ Retire un plat de la commande
        PRE : index_plat est un entier donnant la position du plat à retirer dans la liste des plats et ne peut pas être plus petit que 0 ou plus grand que la longueur de la liste plats
        POST : enlève le plat de la liste à l'indice donné
        RAISE : IndexError si l'indice est plus petit que 0 ou plus grand que la longueur de la liste plats
        """
        if isinstance(index_plat, int) and 0 <= index_plat < len(self.plats):
            self._plats.pop(index_plat)
        else:
            raise IndexError("Index du plat non valide")