class Plat:
    def __init__(self, nom, liste_ingredients, prix, etat_plat="commande"):
        self._nom = nom
        self._liste_ingredients = liste_ingredients
        self._prix = prix
        self._etat_plat = etat_plat

    @property
    def nom(self):
        return self._nom

    @property
    def liste_ingredients(self):
        return self._liste_ingredients

    def retirer_ingredient(self,nom):
         self._liste_ingredients.remove(nom)

    @property
    def prix(self):
        return self._prix

    @property
    def etat_plat(self):
        return self._etat_plat

    @etat_plat.setter
    def etat_plat(self, etat):
        if etat in ["C", "P", "S"]:
            self._etat_plat = etat
        else:
            raise ValueError("L'état du plat doit être C-commandé, P-préparé, S-servi")
