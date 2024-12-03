import unittest
from datetime import datetime

from src.commande import Commande
from src.table import Table
from src.reservation import Reservation
from src.plat import Plat
from src.client import Client


class TestMain(unittest.TestCase):
    def test_retirer_plat(self):
        com = Commande()
        plat1 = Plat("Bolo", ["Pate", "Bolo", "Persil"], 12.5)
        plat2 = Plat("Pizza", ["Pate","Tomate", "Fromage", "Jambon"], 9.7)
        plat3 = Plat("Steak", ["Steak", "Frites", "Salade", "Archiduc"], 27.1)
        com.ajouter_plat(plat1)
        com.ajouter_plat(plat2)
        com.ajouter_plat(plat3)

        self.assertEqual(len(com.plats), 3)
        self.assertEqual(com.plats[1].nom, "Pizza")

        com.retirer_plat(1)
        self.assertEqual(len(com.plats), 2)
        self.assertNotIn(plat2, com.plats)
        self.assertEqual(com.plats[0].nom, "Bolo")
        self.assertEqual(com.plats[1].nom, "Steak")

        with self.assertRaises(IndexError):
            com.retirer_plat("ttt")
        with self.assertRaises(IndexError):
            com.retirer_plat(1.5)
        with self.assertRaises(IndexError):
            com.retirer_plat(-1)
        with self.assertRaises(IndexError):
            com.retirer_plat(3)


    def test_nbr_place(self):
        table15 = Table(15)
        nbr = 5
        nbr0 = 0
        nbr_negatif = -5
        nbr_virgule = 5.4
        caract = 'ttt'

        table15.nbr_place = nbr
        self.assertEqual(table15.nbr_place,5)

        table15.nbr_place = nbr0
        self.assertEqual(table15.nbr_place,0)

        with self.assertRaises(ValueError):
            table15.nbr_place = nbr_negatif
        with self.assertRaises(ValueError):
            table15.nbr_place = nbr_virgule
        with self.assertRaises(ValueError):
            table15.nbr_place = caract

        self.assertEqual(table15.nbr_place, 0)  # L'état reste à 0, dernier état valide


    def test_etat_tables(self):
        table15 = Table(15)
        etat_valide = "O"
        etat_invalide_minuscule = "o"
        etat_invalide = "T"
        etat_nbr_entier = 5
        etat_nbr_virgule = 5.5

        table15.etat_table = etat_valide
        self.assertEqual(table15.etat_table,"O")

        with self.assertRaises(ValueError):
            table15.etat_table = etat_invalide_minuscule
        with self.assertRaises(ValueError):
            table15.etat_table = etat_invalide
        with self.assertRaises(ValueError):
            table15.etat_table = etat_nbr_entier
        with self.assertRaises(ValueError):
            table15.etat_table = etat_nbr_virgule
        
        self.assertEqual(table15.etat_table, "O")  # L'état reste le dernier valide



    def test_commande(self):
        table15 = Table(15)
        com = Commande()
        com_prete = Commande("P")
        com_caract = "ttt"
        com_nbr_entier = 5
        com_nbr_virgule = 5.5

        table15.commande = com
        self.assertEqual(table15.commande.etat_commande, "C")
        
        table15.commande = com_prete
        self.assertEqual(table15.commande.etat_commande, "P")

        with self.assertRaises(TypeError):
            table15.commande = com_caract
        with self.assertRaises(TypeError):
            table15.commande = com_nbr_entier
        with self.assertRaises(TypeError):
            table15.commande = com_nbr_virgule
        
        self.assertEqual(table15.commande.etat_commande, "P")  # L'état reste le dernier valide


    def test_modifier(self):
        pass
        cl = Client("Gaston", "06848595")
        res = Reservation(cl, datetime(2024, 12,5, 15,30), 4, 15)
        date = datetime(2024, 12,6, 15,30)
        date2 = datetime(2024, 12,7, 15,30)
        nombre_per = 5
        nombre_per2 = 6
        nombre_per0 = 0
        date_invalide = 9
        nombre_per_caract = "ttt"
        nombre_per_nbr_negatif = -5

        res.modifier(rdv=date)
        self.assertEqual(res.rdv, datetime(2024, 12,6, 15,30))

        res.modifier(nbr_pers=nombre_per)
        self.assertEqual(res.nbr_pers, 5)

        res.modifier(nbr_pers=nombre_per0)
        self.assertEqual(res.nbr_pers, 0)

        res.modifier(rdv=date2, nbr_pers=nombre_per2)
        self.assertEqual(res.rdv, datetime(2024, 12,7, 15,30))
        self.assertEqual(res.nbr_pers, 6)

        with self.assertRaises(ValueError):
            res.modifier(rdv=date_invalide)
        with self.assertRaises(ValueError):
            res.modifier(nbr_pers=nombre_per_caract)
        with self.assertRaises(ValueError):
            res.modifier(nbr_pers=nombre_per_nbr_negatif)
        with self.assertRaises(ValueError):
            res.modifier(rdv=date_invalide, nbr_pers=nombre_per_nbr_negatif)

        self.assertEqual(res.rdv, datetime(2024, 12,7, 15,30))
        self.assertEqual(res.nbr_pers, 6)


# if __name__ == '__main__':
#     unittest.main()