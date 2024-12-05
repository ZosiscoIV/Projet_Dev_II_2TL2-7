import json
from datetime import datetime

from src.table import Table
from src.commande import Commande
from src.plat import Plat
from src.client import Client
from src.reservation import Reservation


import unittest

class Test(unittest.TestCase):

    def test_init_commande_et_increment_compteur(self):

        Commande.compteur = 1

        cmd1 = Commande("C")
        cmd2 = Commande("P")
        cmd3 = Commande()

        self.assertEqual(cmd1.etat_commande, "C")
        self.assertEqual(cmd2.etat_commande, "P")
        self.assertEqual(cmd3.etat_commande, "C")
        self.assertEqual(cmd1.num_commande, 1)
        self.assertEqual(cmd2.num_commande, 2)
        self.assertEqual(cmd3.num_commande, 3)
        self.assertEqual(Commande.compteur, 4)


    def test_etat_commande(self):

        Commande.compteur = 1

        cmd1 = Commande("C")
        cmd2 = Commande("P")

        cmd1.etat_commande = "P"
        self.assertEqual(cmd1.etat_commande, "P")
        cmd2.etat_commande = "C"
        self.assertEqual(cmd2.etat_commande, "C")

        with self.assertRaises(ValueError):
            cmd2.etat_commande = "CP"
        with self.assertRaises(ValueError):
            cmd1.etat_commande = "Pm"
        with self.assertRaises(ValueError):
            cmd2.etat_commande = "t"
        with self.assertRaises(ValueError):
            cmd2.etat_commande = "T"
        with self.assertRaises(ValueError):
            cmd2.etat_commande = "c"
        with self.assertRaises(ValueError):
            cmd2.etat_commande = "p"
        with self.assertRaises(ValueError):
            cmd2.etat_commande = 42
        with self.assertRaises(ValueError):
            cmd2.etat_commande = ""
        with self.assertRaises(ValueError):
            cmd2.etat_commande = None

    def test_ajouter_plat(self):

        plat1 = Plat("Bolo", ["Pate", "Bolo", "Persil"], 12.5)
        plat2 = Plat("Pizza", ["Pate","Tomate", "Fromage", "Jambon"], 9.7)
        plat3 = Plat("Steak", ["Steak", "Frites", "Salade", "Archiduc"], 27.1)


        cmd3 = Commande()
        self.assertEqual(cmd3.plats, [])
        cmd3.ajouter_plat(plat1)
        self.assertEqual(cmd3.plats[0], plat1)

        with self.assertRaises(ValueError):
            cmd3.ajouter_plat(42)


        cmd4 = Commande()

        cmd4.ajouter_plat(plat1)
        cmd4.ajouter_plat(plat2)

        cmd4.ajouter_plat(plat3)
        self.assertEqual(cmd4.plats[2], plat3)

        with self.assertRaises(ValueError):
            cmd4.ajouter_plat(42)



    def test_retirer_plat(self):

        plat1 = Plat("Bolo", ["Pate", "Bolo", "Persil"], 12.5)
        plat2 = Plat("Pizza", ["Pate", "Tomate", "Fromage", "Jambon"], 9.7)
        plat3 = Plat("Steak", ["Steak", "Frites", "Salade", "Archiduc"], 27.1)

        cmd5 = Commande("C")
        cmd5.ajouter_plat(plat1)
        self.assertEqual(cmd5.plats[0], plat1)

        with self.assertRaises(IndexError):
            cmd5.retirer_plat(19)
        with self.assertRaises(IndexError):
            cmd5.retirer_plat(plat1)

        cmd5.retirer_plat(0)
        self.assertEqual(cmd5.plats, [])


        cmd6 = Commande("C")

        with self.assertRaises(IndexError):
            cmd6.retirer_plat(0)

        cmd6.ajouter_plat(plat1)
        cmd6.ajouter_plat(plat2)
        cmd6.ajouter_plat(plat3)

        self.assertEqual(cmd6.plats[0], plat1)
        self.assertEqual(cmd6.plats[1], plat2)
        self.assertEqual(cmd6.plats[2], plat3)

        cmd6.retirer_plat(1)

        self.assertEqual(cmd6.plats[0], plat1)
        self.assertEqual(cmd6.plats[1], plat3)

        cmd6.ajouter_plat(plat3)
        self.assertEqual(cmd6.plats[2], plat3)

        cmd6.retirer_plat(1)
        self.assertEqual(cmd6.plats[1], plat3)
        with self.assertRaises(IndexError):
            cmd6.retirer_plat(2)

        with self.assertRaises(IndexError):
            cmd6.retirer_plat(-1)





if __name__ == '__main__':
    unittest.main()