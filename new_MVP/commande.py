from plat import Plat


class Commande:
    def __init__(self,num_commande, etat_commande= "C"):
        """
        Initialise une commande
        PRE : num_commande est un entier positif
              etat_commande est un caractère ("C" pour commandée, "P" pour prête)
        POST : Crée une instance de Commande
        """
        self._num_commande = num_commande
        self._etat_commande = etat_commande # commande et pret
        self._plats = []

    @property
    def num_commande(self):
        """
        Retourne le numéro de commande
        POST : Retourne  le numéro de commande
        """
        return self._num_commande

    @property
    def etat_commande(self):
        """
        Retourne l'état actuel de la commande.

        PRE : La commande doit exister et son état doit être valide.
        POST : Retourne l'état actuel de la commande ('C' pour Commandée, 'P' pour Prête).
        """
        return self._etat_commande

    @etat_commande.setter
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

    @property
    def plats(self):
        """
        Retourne les plats de la commande
        POST : Retourne  les plats de commande
        """
        return self._plats

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