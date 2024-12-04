import json
from datetime import datetime

from src.table import Table
from src.commande import Commande
from src.plat import Plat
from src.client import Client
from src.reservation import Reservation


import unittest

class Test(unittest.TestCase):

    def test_init_commande(self):

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


if __name__ == '__main__':
    unittest.main()