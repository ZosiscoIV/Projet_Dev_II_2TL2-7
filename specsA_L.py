#lien vers le projet : https://github.com/ZosiscoIV/Projet_Dev_II_2TL2-7/tree/main/new_MVP


###classe Commande 

def retirer_plat(self,index_plat):
    """ Retire un plat de la commande
    PRE : index_plat est un entier donnant la position du plat à retirer dans la liste des plats et ne peut pas être plus petit que 0 ou plus grand que la longueur de la liste plats
    POST : enlève le plat de la liste à l'indice donné
    RAISE : IndexError si l'indice est plus petit que 0 ou plus grand que la longueur de la liste plats
    """
    if isinstance(index_plat, int) and 0 <= index_plat < len(self.plats):
        self._plats.pop(index_plat)
    else:
        raise IndexError("Index du plat non valide")

###classe Table

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


###Classe Reservation

def modifier(self,rdv, nbr_pers):
    """ Modifie une réservation
    PRE : rdv est une date 
          nbr_pers est un entier positif ou nul
    POST : change le rdv et nbr_pers
    RAISE : ValueError si rdv n'est pas une date et le nombre de personne est négatif ou pas un entier 
    """
    if isinstance(rdv, datetime.date) and isinstance(nbr_pers, int) and nbr_pers >= 0 : 
        self._rdv = rdv
        self._nbr_pers = nbr_pers
    else:
        raise ValueError("rdv doit être une date et le nombre de personne est un entier positif ou nul")
