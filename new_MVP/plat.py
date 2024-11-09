class Plat:
    def __init__(self, nom, liste_ingredients, prix, etat_plat="commande"):
        self._nom = nom
        self._liste_ingredients = liste_ingredients
        self._prix = prix
        self._etat_plat = etat_plat


    def retirer_ingredient(self,nom):
         self._liste_ingredients.remove(nom)