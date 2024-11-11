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

    def retirer_plat(self,plat):
        self._plats.remove(plat)
