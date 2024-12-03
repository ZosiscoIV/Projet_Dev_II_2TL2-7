import json
from datetime import datetime

from src.table import Table
from src.commande import Commande
from src.plat import Plat
from src.client import Client
from src.reservation import Reservation


import unittest

class Test(unittest.TestCase):

    def test_commande(self):
        cmd1 = Commande('P')
        cmd2 = Commande('C')
        self.assertEqual(cmd1.etat_commande, 'P')
        self.assertEqual(cmd2.etat_commande, 'C')


        with self.assertRaises(ValueError):
            cmd3 = Commande('D')


if __name__ == '__main__':
    unittest.main()
