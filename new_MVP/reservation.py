import datetime


class Reservation:
    def __init__(self,num_reservation,nom_pers, rdv, nbr_pers, num_table):
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
        RAISE :
        """
        if isinstance(rdv, datetime.date) and isinstance(nbr_pers, int) and nbr_pers >= 0:
            self._rdv = rdv
            self._nbr_pers = nbr_pers
        else:
            raise ValueError("rdv doit être une date et le nombre de personne est un entier positif ou nul")

    def annuler(self):
        pass