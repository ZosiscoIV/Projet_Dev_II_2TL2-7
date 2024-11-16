import datetime


class Reservation:
    def __init__(self,num_reservation,nom_pers, rdv, nbr_pers, num_table):
        """
        Initialise une réservation
        PRE : num_reservation est un entier positif
              nom_pers est une chaine de caractère
              rdv est une date et une heure
              nbr_pers est un entier positif
              num_table est un entier positif
        POST : Crée une instance de Reservation
        """
        self._num_reservation = num_reservation
        self._nom_pers = nom_pers
        self._rdv = rdv
        self._nbr_pers = nbr_pers
        self._num_table = num_table

    def modifier(self, rdv, nbr_pers):
        """ Modifie une réservation
        PRE : rdv est une date
              nbr_pers est un entier positif ou nul
        POST : change le rdv et nbr_pers
        RAISE : ValueError si rdv n'est pas une date et le nombre de personne est négatif ou pas un entier
        """
        if isinstance(rdv, datetime.date) and isinstance(nbr_pers, int) and nbr_pers >= 0:
            self._rdv = rdv
            self._nbr_pers = nbr_pers
        else:
            raise ValueError("rdv doit être une date et le nombre de personne est un entier positif ou nul")

    def annuler(self):
        pass