#1
from new_MVP.table import Table


def etat_commande(self):
    """
    Retourne l'état actuel de la commande.

    PRE : La commande doit exister et son état doit être valide.
    POST : Retourne l'état actuel de la commande ('C' pour Commandée, 'P' pour Prête).
    """
    return self._etat_commande

def etat_commande(self, etat):
    """
    Modifie l'état de la commande.

    PRE : etat doit être une chaîne de caractères valide ('C' ou 'P').
    POST : Modifie l'état de la commande en fonction de la valeur donnée.
    RAISE : ValueError si etat n'est pas une chaine de caractères compris dans "C" ou "P"
    """
    if isinstance(etat, str) and etat in ["C", "P"]:
        self._etat_commande = etat
    else:
        raise ValueError("L'état de la commande doit être 'C-commandée' ou 'P-prête'.")


#2
def ajouter_plat(self, plat):
    """
    Ajoute un plat à la commande.

    PRE : plat est un objet de type Plat valide.
    POST : Ajoute le plat à la liste des plats de la commande.
    RAISE : ValueError si le plat fourni n'est pas de type Plat.
    """
    if isinstance(plat, Plat):
        self._plats.append(plat)
    else:
        raise ValueError("Le plat fourni n'est pas de type Plat, il est donc invalide.")


#3
def retirer_ingredient(self, nom):
    """
    Retire un ingrédient de la liste des ingrédients du plat.

    PRE : nom est une chaîne de caractères représentant l'ingrédient à retirer.
    POST : Retire l'ingrédient spécifié de la liste des ingrédients du plat, si celui-ci existe.
    RAISE : ValueError si l'ingrédient n'est pas du bon type ou pas dans la liste des ingrédients du plat.
    """
    if isinstance(nom, str) and nom in self._liste_ingredients:
        self._liste_ingredients.remove(nom)
    else:
        raise ValueError(f"L'ingrédient {nom} n'a pas été trouvé.")

#4
def etat_plat(self):
    """
    Retourne l'état actuel du plat.

    PRE : L'état du plat doit être valide.
    POST : Retourne l'état actuel du plat ('C' pour Commandé, 'P' pour Préparé, 'S' pour Servi).
    """
    return self._etat_plat

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

#5
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
