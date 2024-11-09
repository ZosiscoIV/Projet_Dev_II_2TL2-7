class Commande:
    def __init__(self,num_commande, plats, etat_commande):
        self._num_commande = num_commande
        self._plats = plats
        self._etat_commande = etat_commande

    def ajouter_plat(self,plat):
        self._plats.append(plat)

    def changer_etat_commande(self,etat_commande):
        self._etat_commande = etat_commande