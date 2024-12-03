class Client:
    def __init__(self,nom,phone):
        self._nom = nom
        self._phone = phone

    @property
    def nom(self):
        return self._nom

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self,phone):
        self._phone = phone

    def contacter(self):
        return f"Le nom du client est {self.nom} et son telephone : {self.phone}"