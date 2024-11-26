class Plat:
    def __init__(self, nom, liste_ingredients, prix, etat_plat="C"):
        """
        Initialise un plat
        PRE : nom est une chaine de caractère
              liste_ingredients est une liste composé d'ingredients
              prix est le prix du plat
              etat_plat est un caractère ('C' pour Commandé, 'P' pour Préparé, 'S' pour Servi)
        POST : Crée une instance de Plat
        """
        self._nom = nom
        self._liste_ingredients = liste_ingredients
        self._prix = prix
        self._etat_plat = etat_plat

    @property
    def nom(self):
        """
        Retourne le nom du plat
        POST : Retourne  le nom du plat
        """
        return self._nom

    @property
    def liste_ingredients(self):
        """
        Retourne la liste d'ingrédients du plat
        POST : Retourne  la liste d'ingrédients du plat
        """
        return self._liste_ingredients

    def retirer_ingredient(self, nom):
        """
        Retire un ingrédient de la liste des ingrédients du plat.

        PRE : nom est une chaîne de caractères représentant un ingrédient à retirer.
        POST : Retire l'ingrédient spécifié de la liste des ingrédients du plat, si celui-ci existe.
        RAISE : ValueError si l'ingrédient n'est pas du bon type ou pas dans la liste des ingrédients du plat.
        """
        if isinstance(nom, str) and nom in self._liste_ingredients:
            self._liste_ingredients.remove(nom)
        else:
            raise ValueError(f"L'ingrédient {nom} n'a pas été trouvé.")

    @property
    def prix(self):
        """
         Retourne le prix du plat
         POST : Retourne  le prix du plat
         """
        return self._prix

    @property
    def etat_plat(self):
        """
        Retourne l'état actuel du plat.

        PRE : L'état du plat doit être valide.
        POST : Retourne l'état actuel du plat ('C' pour Commandé, 'P' pour Préparé, 'S' pour Servi).
        """
        return self._etat_plat

    @etat_plat.setter
    def etat_plat(self, etat):
        """
        Modifie l'état du plat.

        PRE : etat doit être une chaîne de caractères valide ('C' pour Commandé, 'P' pour Préparé, 'S' pour Servi).
        POST : Modifie l'état du plat en fonction de la valeur donnée.
        RAISE : ValueError si etat n'est pas une chaine de caractères compris dans "C", "P" ou "S"
        """
        if isinstance(etat, str) and etat in ["C", "P", "S"]:
            self._etat_plat = etat
        else:
            raise ValueError("L'état du plat doit être 'C-commandé', 'P-préparé' ou 'S-servi'.")