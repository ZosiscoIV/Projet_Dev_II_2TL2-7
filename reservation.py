class Reservation:
    def __init__(self,num_reservation,nom_pers, rdv, nbr_pers, num_table):
        self._num_reservation = num_reservation
        self._nom_pers = nom_pers
        self._rdv = rdv
        self._nbr_pers = nbr_pers
        self._num_table = num_table

    def modifier(self,rdv, nbr_pers):
        self._rdv = rdv
        self._nbr_pers = nbr_pers

    def annuler(self):
        pass