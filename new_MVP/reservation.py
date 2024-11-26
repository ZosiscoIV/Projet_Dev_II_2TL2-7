import datetime


class Reservation:
    def __init__(self,client, rdv, nbr_pers, num_table):
        """
        Initialise une réservation
        PRE : client est un objet Client
              rdv est une date et une heure
              nbr_pers est un entier positif
              num_table est un entier positif
        POST : Crée une instance de Reservation
        """
        self._client = client
        self._rdv = rdv
        self._nbr_pers = nbr_pers
        self._num_table = num_table

    @property
    def client(self):
        """
        Retourne l'objet client
        POST : Retourne  l'objet client
        """
        return self._client

    @property
    def rdv(self):
        """
        Retourne la date et heure du rendez vous
        POST : Retourne  la date et heure du rendez vous
        """
        return self._rdv

    @property
    def nbr_pers(self):
        """
        Retourne le nombre de personnes de la reservation
        POST : Retourne  le nombre de personnes
        """
        return self._nbr_pers

    @property
    def num_table(self):
        """
        Retourne le numéro de table de la reservation
        POST : Retourne  le numéro de table
        """
        return self._num_table

    def modifier(self, rdv = None, nbr_pers = None):
        """ Modifie une réservation
        PRE :
        POST : change le rdv et/ou nbr_pers
        RAISE : ValueError si rdv n'est pas une date ou le nombre de personne est négatif ou pas un entier
        """
        if rdv is None:
            rdv = self._rdv
        else:
            if not isinstance(rdv, datetime.date):
                raise ValueError("rdv doit être une date")

        if nbr_pers is None:
            nbr_pers = self._nbr_pers
        else:
            if not (isinstance(nbr_pers, int) and nbr_pers >= 0):
                raise ValueError("Le nombre de personnes doit être un entier positif ou nul")

        self._rdv = rdv
        self._nbr_pers = nbr_pers

