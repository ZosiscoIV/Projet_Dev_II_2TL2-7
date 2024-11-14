#1
@property
def etat_commande(self):
    """
    Retourne l'état actuel de la commande.

    :return: str - L'état actuel de la commande. Peut être "C" (Commandée) ou "P" (Préparée).
    
    PRE: L'état de la commande a été initialisé avec une valeur valide ("C" ou "P").
    POST: Retourne l'état actuel de la commande.
    """
    return self._etat_commande

@etat_commande.setter
def etat_commande(self, etat):
    """
    Modifie l'état de la commande.

    :param etat: str - L'état de la commande. Doit être "C" ou "P".
    
    PRE: `etat` doit être "C" ou "P".
    POST: L'état de la commande est mis à jour avec la nouvelle valeur spécifiée.
    
    :raises ValueError: Si `etat` n'est pas "C" ou "P".
    """
    if etat in ["C", "P"]:
        self._etat_commande = etat
    else:
        raise ValueError("L'état de la commande doit être 'C' ou 'P'")




#2
def ajouter_plat(self, plat):
    """
    Ajoute un plat à la commande.

    :param plat: Plat - L'instance de plat à ajouter à la commande.
    
    PRE: `plat` doit être une instance valide de la classe Plat.
    POST: Le plat est ajouté à la liste des plats de la commande.
    """
    self._plats.append(plat)

#3
def retirer_ingredient(self, nom):
    """
    Retire un ingrédient de la liste des ingrédients du plat.

    :param nom: str - Le nom de l'ingrédient à retirer.
    
    PRE: `nom` doit être un ingrédient valide existant dans la liste des ingrédients du plat.
    POST: L'ingrédient spécifié est retiré de la liste des ingrédients du plat.
    
    :raises ValueError: Si l'ingrédient `nom` n'est pas dans la liste des ingrédients.
    """
    self._liste_ingredients.remove(nom)

#4
@property
def etat_plat(self):
    """
    Retourne l'état actuel du plat.

    :return: str - L'état actuel du plat. Peut être "C" (Commandé), "P" (Préparé), ou "S" (Servi).
    
    PRE: L'état du plat doit avoir été initialisé avec une valeur valide ("C", "P" ou "S").
    POST: Retourne l'état actuel du plat.
    """
    return self._etat_plat

@etat_plat.setter
def etat_plat(self, etat):
    """
    Modifie l'état du plat.

    :param etat: str - L'état du plat. Doit être "C", "P" ou "S".
    
    PRE: `etat` doit être une chaîne de caractères, et doit être "C", "P" ou "S".
    POST: L'état du plat est mis à jour avec la nouvelle valeur spécifiée.
    
    :raises ValueError: Si `etat` n'est pas "C", "P" ou "S".
    """
    if etat in ["C", "P", "S"]:
        self._etat_plat = etat
    else:
        raise ValueError("L'état du plat doit être 'C', 'P' ou 'S'")

#5
def regrouper_table(self, *table):
    """
    Fusionne plusieurs tables avec la table actuelle.

    :param table: Table - D'autres tables à fusionner avec la table actuelle.
    
    PRE: `table` contient des instances valides de la classe Table.
    POST: Les tables spécifiées sont fusionnées, et le nombre de places de la table actuelle est ajusté.
    
    :raises ValueError: Si les tables ne peuvent pas être fusionnées.
    """
    plus_petit_num_table = self  # Table avec le plus petit numéro
    table_to_merge = [self]  # Liste des tables
